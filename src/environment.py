import random

import numpy as np

from permutation_matrices import CUBE_R, CUBE_U, RIGHT


# TODO frozendict
COLORS = {
    0: 'Green',
    1: 'White',
    2: 'Blue',
    3: 'Yellow',
    4: 'Red',
    5: 'Orange'
}

SOLVED_CUBE = np.array([
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 1, 1, 1, 1, 1, 1,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 
    3, 3, 3, 3, 3, 3, 3, 3, 3,        
    4, 4, 4, 4, 4, 4, 4, 4, 4,
    5, 5, 5, 5, 5, 5, 5, 5, 5
])

ACTIONS = {
    "R": RIGHT,
    "R'": np.matmul(np.matmul(RIGHT, RIGHT), RIGHT),
    "L": np.matmul(np.matmul(np.matmul(np.matmul(CUBE_U, CUBE_U), RIGHT), CUBE_U), CUBE_U),
    "L'": 0,
    "F": 0,
    "F'": 0,
    "U": 0,
    "U'": 0,
    "D": 0,
    "D'": 0,
    "B": 0, 
    "B'": 0,
    "r": CUBE_R,
    "u": CUBE_U
}

class ActionError(Exception):
    pass


class CubeEnvironment(object):
    '''
    '''

    possible_actions = ACTIONS.keys()

    def __init__(self):
        self.cube_state = None

    def init_cube(self, cube_repr=None):
        '''
        re-init the cube state to a random valid configuration or a specific representation if cube_repr is given
        returns the initial state
        '''
        if cube_repr:
            if self.check_valid_state(cube_repr):
                self.cube_state = cube_repr
            else:
                raise Exception("Cube repr is not valid")
        else:
            self.cube_state = self.generate_random_cube()

        return self.cube_state

    def get_action_space(self):
        return self.possible_actions

    def generate_random_cube(self, n_random=10):
        '''
        generates a random valid cube representation
        does NOT store it as the current cube representation

        1. takes a valid cube
        2. makes n random moves
        '''
        cube = np.ndarray.copy(SOLVED_CUBE)
        for n in range(n_random):
            action = random.choice(self.possible_actions)
            cube = apply_action(action)

    def check_valid_state(self, cube_state):
        '''
        checks if the given cube_state is possible given a standard cube
        TODO For now: trust me dude
        '''
        print(type(cube_state))
        assert isinstance(cube_state, np.ndarray)
        print(cube_state.shape)
        return True

    def take_action(self, action):
        '''
        apply the given action to change the current cube state
        returns state, reward, and a boolean specifying if the cube is solved or not
        '''
        self.cube_state = apply_action(self.cube_state, action)

        solved = self.check_solved(self.cube_state)
        reward = SOLVED_REWARD if solved else STEP_REWARD

        return self.cube_state, reward, solved

    def apply_action(self, cube_state, action):
        if action not in self.possible_actions:
            raise ActionError("Invalid cube action %s" % action)

        return np.matmul(cube_state, ACTIONS[action])

    def check_solved(self, cube_state):
        '''
        checks if the given cube state is the solved state
        '''
        return np.array_equal(cube_state, SOLVED_CUBE)

        
