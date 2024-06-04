from classes.maze import Maze
import random
import numpy as np

class Policy():

    def __init__(self, maze: Maze, discount_factor) -> None:
        self.all_states = [[0,0],[0,1], [0,2], [0,3], [1,0],[1,1], [1,2], [1,3], [2,0],[2,1], [2,2], [2,3], [3,0],[3,1], [3,2], [3,3]]
        self.maze = maze
        self.value_grid = np.array([
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0], 
            [0, 0, 0, 0]
        ])
        self.discount_factor = discount_factor
        self.iteration = 0
        self.policy = {tuple(state): random.choice(self.maze.actions) for state in self.all_states}


    def value_iteration(self):
        print("Iteration: ", self.iteration)
        print("value_grid: \n", self.value_grid)
        threshold = 0.01
        delta = 1
        rows, cols = self.value_grid.shape
        old_values = np.zeros([4,4])
        while delta > threshold:
            new_values = np.copy(old_values)
            delta = 0
            for i in range(rows):
                for j in range(cols):
                    if [i, j] in self.maze.terminal_states:
                        self.policy[tuple([i,j])] = None
                        continue  # Skip terminal states
                    
                    best_value = -999
                    best_action = []
                    for action in self.maze.actions:
                        next_state, reward = self.maze.step([i,j], action)
                        value = reward + self.discount_factor * old_values[next_state[0], next_state[1]]
                        if best_value < value:
                            best_value = value
                            best_action = action
                            delta = max(delta, abs(old_values[next_state[0], next_state[1]] - new_values[next_state[0], next_state[1]]))
                    
                    self.policy[tuple([i,j])] = best_action 
                    new_values[i, j] = best_value

            self.value_grid = new_values
            old_values = new_values

            self.iteration += 1
            print("Iteration: ", self.iteration)
            print("value_grid: \n", self.value_grid)
    
    
    def proof(self):
        for key,value in self.policy.items():
            print(f"locatie: {key} reward: {self.maze.reward_list[list(key)[0], list(key)[1]]} value: {self.value_grid[key]} policy: {value}")