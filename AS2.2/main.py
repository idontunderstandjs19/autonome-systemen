from classes.maze import Maze
from classes.agent import Agent
from classes.policy import Policy
from classes.td import Temporal_difference
from classes.sarsa import Sarsa
from classes.q_learning import Q_learning
import numpy as np
import time


def main():
    discount_factor = 1
    maze = Maze()
    policy = Policy(maze, discount_factor)
    agent = Agent(maze, policy)
    policy.value_iteration()
    policy.proof()
    agent.print_optimal_route()

    # boolean = True
    # amount_of_moves = 0

    # while boolean:
    #     # Print de huidige positie van de agent in een 4x4 grid
    #     agent_grid = np.full((4, 4), ' ')
    #     x, y = maze.agent_pos
    #     agent_grid[x, y] = 'X'  # 'X' staat voor de agent
    #     print(agent_grid)
        
    #     # Wacht een seconde
    #     time.sleep(1)
        
    #     # Beweeg de agent volgens het beleid
    #     boolean = agent.act(amount_of_moves)

    #     amount_of_moves += 1


    # print("Gefeliciteerd, het spel heeft de optimale pad bewandeld")
    # print(F"De agent had een eind reward van: {agent.total_reward}")
    episodes = 1000000
    gamma = 1 # discount factor
    alpha = 0.1 # learning rate
    episolon = 0.1 # greedy rate
    step_size = 0.1 # step size
    td = Temporal_difference(maze, episodes, policy.policy, gamma, alpha)
    td.temporal_difference()
    sarsa = Sarsa(maze, policy, episodes, gamma, episolon, step_size)
    #sarsa.sarsa()
    q_learning = Q_learning(maze, policy, episodes, gamma, episolon, step_size)
    q_learning.q_learning()
    

if __name__ == "__main__":
    main()