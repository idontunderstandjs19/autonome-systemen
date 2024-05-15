from classes.maze import Maze
from classes.policy import Policy
import numpy as np
import time

class Agent():
    
    def __init__(self, maze: Maze, policy: Policy) -> None:
        self.maze = maze
        self.policy = policy
        self.route: list = []
        self.total_reward: int = 0
        self.policy.value_iteration()
        self.policy.update_policy()
        self.policy.print_interation()

    
    def moving_agent(self):
        test = True

        while test:
            # Print de huidige positie van de agent in een 4x4 grid
            agent_grid = np.full((4, 4), ' ')
            x, y = self.maze.agent_pos
            agent_grid[x, y] = 'X'  # 'X' staat voor de agent
            print(agent_grid)
            
            # Wacht een seconde
            time.sleep(1)
            
            # Beweeg de agent volgens het beleid
            test = self.move_agent()


    def total_reward_agent(self):
        self.total_reward += self.maze.reward_list[self.maze.agent_pos[0], self.maze.agent_pos[1]]

    
    def move_agent(self):
        state_to_tuple = tuple(self.maze.agent_pos)
        get_direction = self.policy.policy[state_to_tuple]
        if get_direction == None:
            return False
        else:
            self.maze.step(get_direction)
            self.total_reward_agent()
            return True

        