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


    def step(self, action):
        new_step = self.agent_pos.copy()

        if action == "up":
            if self.agent_pos[0] > 0:
                new_step[0] -= 1
        elif action == "down":
            if self.agent_pos[0] < len(self.reward_list) - 1:
                new_step[0] += 1
        elif action == "left":
            if self.agent_pos[1] > 0:
                new_step[1] -= 1
        elif action == "right":
            if self.agent_pos[1] < len(self.reward_list[0]) - 1:
                new_step[1] += 1
        self.agent_pos = new_step

    