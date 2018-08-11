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


def test_u():
    expected_state = np.matrix([4,4,4,0,0,0,0,0,0, 1,1,1,1,1,1,1,1,1, 5,5,5,2,2,2,2,2,2, 3,3,3,3,3,3,3,3,3, 2,2,2,4,4,4,4,4,4, 0,0,0,5,5,5,5,5,5])
    starting_cube = SOLVED_CUBE
    env = CubeEnvironment()
    env.init_cube(cube_repr=starting_cube)
    new_state, reward, solved = env.take_action('[r]')
    new_state, reward, solved = env.take_action('[u]')
    print(new_state)
    new_state, reward, solved = env.take_action('R')
    print(new_state)
    new_state, reward, solved = env.take_action('[u]')
    new_state, reward, solved = env.take_action('[u]')
    new_state, reward, solved = env.take_action('[u]')
    print(new_state)
    new_state, reward, solved = env.take_action('[r]')
    new_state, reward, solved = env.take_action('[r]')
    new_state, reward, solved = env.take_action('[r]')
    print(new_state)
    assert np.array_equal(new_state, expected_state)



@pytest.mark.parametrize(["action", "expected_state"], [

    ["[r]", np.matrix([3,3,3,3,3,3,3,3,3, 0,0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1,1, 2,2,2,2,2,2,2,2,2, 4,4,4,4,4,4,4,4,4, 5,5,5,5,5,5,5,5,5])],
    ["[u]", np.matrix([4,4,4,4,4,4,4,4,4, 1,1,1,1,1,1,1,1,1, 5,5,5,5,5,5,5,5,5, 3,3,3,3,3,3,3,3,3, 2,2,2,2,2,2,2,2,2, 0,0,0,0,0,0,0,0,0])],
    ["R",  np.matrix([0,0,3,0,0,3,0,0,3, 1,1,0,1,1,0,1,1,0, 1,2,2,1,2,2,1,2,2, 3,3,2,3,3,2,3,3,2, 4,4,4,4,4,4,4,4,4, 5,5,5,5,5,5,5,5,5])],
    ["R'", np.matrix([0,0,1,0,0,1,0,0,1, 1,1,2,1,1,2,1,1,2, 3,2,2,3,2,2,3,2,2, 3,3,0,3,3,0,3,3,0, 4,4,4,4,4,4,4,4,4, 5,5,5,5,5,5,5,5,5])],
    ["L",  np.matrix([1,0,0,1,0,0,1,0,0, 2,1,1,2,1,1,2,1,1, 2,2,3,2,2,3,2,2,3, 0,3,3,0,3,3,0,3,3, 4,4,4,4,4,4,4,4,4, 5,5,5,5,5,5,5,5,5])],
    ["L'", np.matrix([3,0,0,3,0,0,3,0,0, 0,1,1,0,1,1,0,1,1, 2,2,1,2,2,1,2,2,1, 2,3,3,2,3,3,2,3,3, 4,4,4,4,4,4,4,4,4, 5,5,5,5,5,5,5,5,5])],
    ["F",  np.matrix([0,0,0,0,0,0,0,0,0, 1,1,1,1,1,1,5,5,5, 2,2,2,2,2,2,2,2,2, 4,4,4,3,3,3,3,3,3, 1,4,4,1,4,4,1,4,4, 5,5,3,5,5,3,5,5,3])],
    ["F'", np.matrix([0,0,0,0,0,0,0,0,0, 1,1,1,1,1,1,4,4,4, 2,2,2,2,2,2,2,2,2, 5,5,5,3,3,3,3,3,3, 3,4,4,3,4,4,3,4,4, 5,5,1,5,5,1,5,5,1])],
    ["U",  np.matrix([4,4,4,0,0,0,0,0,0, 1,1,1,1,1,1,1,1,1, 5,5,5,2,2,2,2,2,2, 3,3,3,3,3,3,3,3,3, 2,2,2,4,4,4,4,4,4, 0,0,0,5,5,5,5,5,5])],
    ["U'", np.matrix([5,5,5,0,0,0,0,0,0, 1,1,1,1,1,1,1,1,1, 4,4,4,2,2,2,2,2,2, 3,3,3,3,3,3,3,3,3, 0,0,0,4,4,4,4,4,4, 2,2,2,5,5,5,5,5,5])],
    ["D",  np.matrix([0,0,0,0,0,0,5,5,5, 1,1,1,1,1,1,1,1,1, 2,2,2,2,2,2,4,4,4, 3,3,3,3,3,3,3,3,3, 4,4,4,4,4,4,0,0,0, 5,5,5,5,5,5,2,2,2])],
    ["D'", np.matrix([0,0,0,0,0,0,4,4,4, 1,1,1,1,1,1,1,1,1, 2,2,2,2,2,2,5,5,5, 3,3,3,3,3,3,3,3,3, 4,4,4,4,4,4,2,2,2, 5,5,5,5,5,5,0,0,0])],
    ["B",  np.matrix([0,0,0,0,0,0,0,0,0, 4,4,4,1,1,1,1,1,1, 2,2,2,2,2,2,2,2,2, 3,3,3,3,3,3,5,5,5, 4,4,3,4,4,3,4,4,3, 1,5,5,1,5,5,1,5,5])],
    ["B'", np.matrix([0,0,0,0,0,0,0,0,0, 5,5,5,1,1,1,1,1,1, 2,2,2,2,2,2,2,2,2, 3,3,3,3,3,3,4,4,4, 4,4,1,4,4,1,4,4,1, 3,5,5,3,5,5,3,5,5])]
])
def test_rotations(action, expected_state):
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

    starting_cube = SOLVED_CUBE
    env = CubeEnvironment()
    env.init_cube(cube_repr=starting_cube)
    new_state, reward, solved = env.take_action(action)

    assert reward == 0
    assert solved is False
    print("NEW STATE %s" % str(new_state))
    assert np.array_equal(new_state, expected_state)


def test_scrambled():
    '''
    tests all the possible actions on a scrambled cube just in case unit permutation 
    tests missed something due to a face being mostly the same color
    '''
    pass


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

