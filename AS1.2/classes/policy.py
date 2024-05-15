from classes.maze import Maze
import random
import numpy as np

class Policy():

    def __init__(self, maze: Maze) -> None:
        self.all_states = [[0,0],[0,1], [0,2], [0,3], [1,0],[1,1], [1,2], [1,3], [2,0],[2,1], [2,2], [2,3], [3,0],[3,1], [3,2], [3,3]]
        self.maze = maze
        self.reward_list = maze.reward_list
        self.value_grid = np.array([
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0], 
            [0, 0, 0, 0]
        ])
        self.discount_factor = 1
        self.iteration = 0
        self.policy = self.create_start_policy()

    
    def new_iteration(self):
        self.value_iteration()
        self.update_policy()
        self.print_interation()


    def value_iteration(self):
        print("Iteration: ", self.iteration)
        print("value_grid: ", self.value_grid)
        threshold = 0.01
        delta = 1
        rows, cols = self.reward_list.shape
        old_values = np.zeros([4,4])
        while delta > threshold:
            new_values = np.copy(old_values)
            delta = 0
            for i in range(rows):
                for j in range(cols):
                    if [i, j] in self.maze.terminal_states:
                        continue  # Skip terminal states
                    
                    # Calculate value for each possible action
                    values = []
                    if i > 0:
                        values.append(self.reward_list[i-1, j] + self.discount_factor * old_values[i-1, j])
                        delta = max(delta, abs(old_values[i-1, j] - new_values[i-1, j]))
                    if i < rows - 1:
                        values.append(self.reward_list[i+1, j] + self.discount_factor * old_values[i+1, j])
                        delta = max(delta, abs(old_values[i+1, j] - new_values[i+1, j]))
                    if j > 0:
                        values.append(self.reward_list[i, j-1] + self.discount_factor * old_values[i, j-1])
                        delta = max(delta, abs(old_values[i, j-1] - new_values[i, j-1]))
                    if j < cols - 1:
                        values.append(self.reward_list[i, j+1] + self.discount_factor * old_values[i, j+1])
                        delta = max(delta, abs(old_values[i, j+1] - new_values[i, j+1]))

                    # Find the maximum value
                    max_value = max(values) if values else 0
                    new_values[i, j] = max_value

            # Copy new values back into the main value grid
            self.value_grid = new_values
            old_values = new_values

            self.iteration += 1
            print("Iteration: ", self.iteration)
            print("value_grid: ", self.value_grid)


    def get_next_state(self, state, action):
        row, col = state
        if action == "up":
            row -= 1
        elif action == "down":
            row += 1
        elif action == "left":
            col -= 1
        elif action == "right":
            col += 1

        if 0 <= row < len(self.value_grid) and 0 <= col < len(self.value_grid):
            return (row, col)
        else:
            return state
    

    def update_policy(self):
        actions = ["up", "down", "left", "right"]
    
        for state in self.all_states:
            if state in self.maze.terminal_states:
                self.policy[tuple(state)] = None

                continue

            max_value = float("-inf")
            best_action = None
            
            for action in actions:
                next_state = self.get_next_state(state, action)
                reward = self.reward_list[next_state[0], next_state[1]]
                expected_reward = reward + self.discount_factor * self.value_grid[next_state[0], next_state[1]]
                
                if expected_reward > max_value:
                    max_value = expected_reward
                    best_action = action
            
            self.policy[tuple(state)] = best_action

    
    def create_start_policy(self):
        actions = ["up", "down", "left", "right"]
        start_policy = {tuple(state): random.choice(actions) for state in self.all_states}
        return start_policy
    
    
    def proof(self):
        for key,value in self.policy.items():
            print(f"locatie: {key} reward: {self.reward_list[key]} value: {self.value_grid[key]} policy: {value}")
            
    
        
    def print_interation(self):
        print(f"Iteratie: {self.iteration}")
        print(f"Value grid: \n {self.value_grid}")
        print(f"policy: {self.policy}")