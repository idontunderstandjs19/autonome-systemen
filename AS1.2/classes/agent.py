from classes.maze import Maze
from classes.policy import Policy
import time

class Agent():
    
    def __init__(self, maze: Maze, policy: Policy) -> None:
        self.maze = maze
        self.policy = policy
        self.route: list = []
        self.total_reward: int = 0
        self.move_agent() # to make the first move after iteration 0 has been settled, this is a random move based on the random start policy
        self.policy.print_interation()
        print(f"Locatie agent: {self.maze.agent_pos}")
        self.new_move()

    
    def new_move(self):
        while True:
            # Controleer of de agent een terminalstaat heeft bereikt
            if self.maze.agent_pos in self.maze.terminal_states:
                break  # Stop de loop als de agent een terminalstaat bereikt

            # Voer een beweging uit
            self.policy.new_iteration()
            self.move_agent()
            print(f"Locatie agent: {self.maze.agent_pos}")

            # Wacht een seconde voordat je de volgende beweging uitvoert
            time.sleep(1)


    def total_reward_agent(self):
        self.total_reward += self.maze.reward_list[self.maze.agent_pos[0], self.maze.agent_pos[1]]

    
    def move_agent(self):
        state_to_tuple = tuple(self.maze.agent_pos)
        get_direction = self.policy.policy[state_to_tuple]
        self.maze.step(get_direction)
        self.total_reward_agent()