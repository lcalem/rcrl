import sys

from environment import CubeEnvironment
from model import CubeModel


def train(n_episodes):

    env = CubeEnvironment()
    model = CubeModel()

    for episode in range(n_episodes):
        prev_state = env.init_cube()

        action = model.get_next_action(init_state)
        state, reward, solved = env.take_action(action)


def evaluate():
    pass


if __name__ == '__main__':
    n_episodes = 300
    train(n_episodes)
