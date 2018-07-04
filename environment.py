import random


class CubeEnvironment(object):

    def __init__(self, cube_size=3):
        self.size = 3
        self.cube_state = None

    def init_cube(self, cube_repr=None):
        '''
        re-init the cube state to a random valid configuration or a specific representation if cube_repr is given
        returns the initial state
        '''
        if cube_repr and self.check_valid_state(cube_repr):
            self.cube_state = cube_repr

        else:
            raise Exception("Cube repr is not valid")

        self.cube_state = self.generate_random_cube()
        return self.cube_state

    def generate_random_cube(self):
        '''
        generates a random valid cube representation
        does NOT store it as the current cube representation
        '''
        # TODO
        pass

    def check_valid_state(self, cube_state):
        '''
        checks if the given cube_state is possible given a standard cube
        '''
        # TODO
        pass

    def check_valid_action(self, action):
        # TODO
        pass

    def take_action(self, action):
        '''
        apply the given action to change the current cube state
        returns state, reward, and a boolean specifying if the cube is solved or not
        '''

        if not self.check_valid_action(action):
            raise Exception("Invalid cube action %s" % action)

        # TODO actually take the action

        solved = self.check_solved(self.cube_state)
        reward = SOLVED_REWARD if solved else STEP_REWARD

        return self.cube_state, reward, solved

    def check_solved(self, cube_state):
        '''
        checks if the given cube state is a solved state
        '''

        # TODO
        pass

        
