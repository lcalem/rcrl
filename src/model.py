import random


class CubeModel(object):
    
    def __init__(self, possible_actions):
        self.actions = possible_actions

    def get_next_action(self, state):
        return random.choice(self.actions)