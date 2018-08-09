import numpy as np
import pytest

from environment import CubeEnvironment


SOLVED_CUBE = np.matrix([
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 1, 1, 1, 1, 1, 1,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 
    3, 3, 3, 3, 3, 3, 3, 3, 3,        
    4, 4, 4, 4, 4, 4, 4, 4, 4,
    5, 5, 5, 5, 5, 5, 5, 5, 5
])


def test_rotations():
    '''
    starts with a known cube representation, take an action and checks that the 
    resulting state matches what we expect after this state

    COLORS
    0: 'Green',
    1: 'White',
    2: 'Blue',
    3: 'Yellow',
    4: 'Red',
    5: 'Orange'
    '''
    expected_state = np.matrix([
        0, 0, 3, 0, 0, 3, 0, 0, 3,
        1, 1, 0, 1, 1, 0, 1, 1, 0,
        2, 2, 1, 2, 2, 1, 2, 2, 1, 
        3, 3, 2, 3, 3, 2, 3, 3, 2,        
        4, 4, 4, 4, 4, 4, 4, 4, 4,
        5, 5, 5, 5, 5, 5, 5, 5, 5
    ])

    starting_cube = SOLVED_CUBE
    env = CubeEnvironment()
    env.init_cube(cube_repr=starting_cube)
    new_state, reward, solved = env.take_action('R')

    assert reward == 0
    assert solved is False
    assert np.array_equal(new_state, expected_state)


def test_solved():
    '''
    starts with a solved cube
    take action R then action R'
    -> cube should be solved
    '''
    starting_cube = SOLVED_CUBE
    env = CubeEnvironment()
    env.init_cube(cube_repr=starting_cube)
    new_state, reward, solved = env.take_action("R")
    new_state, reward, solved = env.take_action("R'")

    assert reward > 0
    assert solved is True
    assert np.array_equal(new_state, starting_cube)


if __name__ == '__main__':
    test_rotations()