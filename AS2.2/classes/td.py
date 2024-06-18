from classes.maze import Maze
import numpy as np

class Temporal_difference():

    def __init__(self, maze: Maze, episodes, policy, gamma, alpha)-> None:
        self.maze = maze
        self.episodes = episodes
        self.policy = policy # optimal path
        self.gamma = gamma # discount factor
        self.alpha = alpha # learning rate

    def temporal_difference(self):
        values = np.zeros((4, 4))
        for _ in range(self.episodes):
            state = self.maze.start_coordinates.copy()
            while list(state) not in self.maze.terminal_states:
                x, y = state
                action = self.policy[x,y]
                next_state, _ = self.maze.step(state.copy(), action)
                values[state[0], state[1]] += self.alpha * (
                    self.maze.reward_list[next_state[0], next_state[1]] + \
                    self.gamma * values[next_state[0], next_state[1]] - \
                    values[state[0], state[1]]
                )
                state = next_state

        print(values)