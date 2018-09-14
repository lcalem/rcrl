import sys

from environment import CubeEnvironment
from model import CubeModel


def train(n_episodes, n_steps, replay_size=500000):
    '''
    n_episodes: max nb of episodes for learning
    n_steps: max nb of moves in an episode
    '''

    env = CubeEnvironment()
    action_space = env.get_action_space()
    model = CubeModel(action_space)

    replay_memory = list()

    for episode in range(n_episodes):
        prev_state = env.init_cube()

        for i in range(n_steps):

            action = model.get_next_action(prev_state)
            state, reward, solved = env.take_action(action)
            model.learn_shit(state, reward, solved)

            if solved:
                print("c'est bon c'est fini lol")
                break
            
            prev_state = state


def evaluate():
    pass


if __name__ == '__main__':
    n_episodes = 300
    n_steps = 100
    train(n_episodes, n_steps)
