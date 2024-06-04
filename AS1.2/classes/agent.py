from classes.maze import Maze
from classes.policy import Policy
import numpy as np

class Agent():
    
    def __init__(self, maze: Maze, policy: Policy) -> None:
        self.maze = maze
        self.policy = policy
        self.route: list = []
        self.total_reward: int = 0

    
    def act(self, amount_of_moves):
        state_to_tuple = tuple(self.maze.agent_pos)
        print("check: ", state_to_tuple)
        get_direction = self.policy.policy[state_to_tuple]
        self.route.append([amount_of_moves, state_to_tuple, get_direction])
        if get_direction == None:
            return False
        else:
            next_state, reward = self.maze.step(self.maze.agent_pos, get_direction)
            self.maze.agent_pos = next_state
            self.total_reward += reward
            return True
        

    def print_optimal_route(self):
        print("\nOptimale route: \n")
        for i in self.route:
            print(i)