import sys

from environment import CubeEnvironment
from model import CubeModel


def train(n_episodes):

    env = CubeEnvironment()
    action_space = env.get_action_space()
    model = CubeModel(action_space)

    for episode in range(n_episodes):
        prev_state = env.init_cube()

        action = model.get_next_action(prev_state)
        state, reward, solved = env.take_action(action)


def evaluate():
    pass


if __name__ == '__main__':
    n_episodes = 300
    train(n_episodes)
