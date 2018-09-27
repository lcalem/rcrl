import numpy as np


class PrioritizedExperienceReplay():
    '''
    alpha: tradeoff between sampling high priority transitions and random sampling
    beta: used to compute importance sampling weights, increased from beta_start to 1.0 over the course of beta_steps
    TL;DR of PER: https://medium.com/arxiv-bytes/summary-prioritized-experience-replay-e5f9257cef2d
    TODO: hindsight experience replay
    '''
    
    def __init__(self, max_size=500000, min_size=50000, alpha=0.6, beta_start=0.4, beta_steps=100000):
        self._min_size = min_size
        self.max_size = max_size
        self.replay_memory = []
        self.priorities = np.zeros((max_size,), dtype=np.float32)
        
        self.alpha = alpha
        self.beta = beta_start
        self.beta_incr = (1.0 - beta_start) / beta_steps
        
        self.index = 0
        self.priorities[0] = 1.0**alpha  # init the first max prob
        
        # for monitoring
        self._nb_done_transitions = 0
        
    @property
    def min_size(self):
        return self._min_size
    
    @property
    def nb_done_transitions(self):
        return self._nb_done_transitions
        
    def update_beta(self):
        self.beta = min(1.0, self.beta + self.beta_incr)
        
    def get_probabilities(self):
        '''
        turn current priorities in probabilities
        '''
        size = len(self.replay_memory)
        end_index = size if size < self.max_size else self.index
        
        prios = self.priorities[:end_index]
        probs = prios / prios.sum()
        return probs
        
    def insert(self, transition):
        
        # add the transition to the memory
        if len(self.replay_memory) < self.max_size:
            self.replay_memory.append(transition)
        else:
            self.replay_memory[self.index] = transition
            
        # update priorities and index
        self.priorities[self.index] = self.priorities.max()
        self.index = (self.index + 1) % self.max_size
        
        if transition.done:
            self._nb_done_transitions += 1
        
    def sample(self, batch_size):
        '''
        sample a batch of transitions
        '''
        current_size = len(self.replay_memory)
        
        # samples
        probs = self.get_probabilities()
        indices = np.random.choice(current_size, batch_size, p=probs)
        samples = [self.replay_memory[i] for i in indices]
        # samples = random.sample(self.replay_memory, batch_size)
        
        # importance sampling weights
        prob_min = probs.min()
        max_weight = (prob_min * current_size)**(-self.beta)

        is_weights  = (current_size * probs[indices]) ** (-self.beta)
        is_weights /= max_weight  # to ensure it is not > 1
        
        self.update_beta()
        return samples, is_weights
    
    def __len__(self):
        return len(self.replay_memory)