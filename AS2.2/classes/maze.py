import numpy as np

class Maze():

    def __init__(self) -> None:
        self.reward_list = np.array([
            [-1, -1, -1, 40],
            [-1, -1, -10, -10],
            [-1, -1, -1, -1],
            [10, -2, -1, -1]
        ])
        self.start_coordinates = [3,2]
        self.terminal_states = [[0,3], [3,0]]
        self.agent_pos = self.start_coordinates
        self.actions = ["up", "down", "left", "right"]


    def step(self, location, action):
        new_step = location
        reward = -1 # de reden van -1, we hadden afgesproken dat als je buiten de dolhof 4x4 ging dat je dan een reward van -1 kreeg.
        if action == "up":
            if new_step[0] > 0:
                new_step[0] -= 1
                reward = self.reward_list[new_step[0], new_step[1]]
        elif action == "down":
            if new_step[0] < len(self.reward_list) - 1:
                new_step[0] += 1
                reward = self.reward_list[new_step[0], new_step[1]]
        elif action == "left":
            if new_step[1] > 0:
                new_step[1] -= 1
                reward = self.reward_list[new_step[0], new_step[1]]
        elif action == "right":
            if new_step[1] < len(self.reward_list[0]) - 1:
                new_step[1] += 1
                reward = self.reward_list[new_step[0], new_step[1]]

        return new_step, reward

        