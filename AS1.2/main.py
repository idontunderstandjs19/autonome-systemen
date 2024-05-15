from classes.maze import Maze
from classes.agent import Agent
from classes.policy import Policy
import numpy as np


def main():
    maze = Maze()
    policy = Policy(maze)
    agent = Agent(maze, policy)
    

if __name__ == "__main__":
    main()