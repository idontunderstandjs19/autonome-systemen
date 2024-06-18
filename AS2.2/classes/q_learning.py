from classes.maze import Maze
from classes.policy import Policy
import numpy as np
import random
import pygame

class Q_learning:

    def __init__(self, maze: Maze, policy: Policy, episodes, gamma, episolon, step_size):
        self.maze = maze
        self.policy = policy
        self.episodes = episodes
        self.gamma = gamma # discount factor
        self.episolon = episolon # greedy
        self.step_size = step_size

    def q_learning(self):
        for _ in range(self.episodes):
            state = self.maze.start_coordinates.copy()
            self.policy.update_qfunction(state)
            while list(state) not in self.maze.terminal_states:
                action = max(self.policy.q_function[state[0], state[1]], key=self.policy.q_function[state[0], state[1]].get)
                if random.random() < self.episolon:
                    action = np.random.choice(
                        [
                            "up", 
                            "down", 
                            "left", 
                            "right"
                        ]
                    )
                
                next_state, reward = self.maze.step(state.copy(), action)
                self.policy.update_qfunction(next_state)
                next_action = max(
                    self.policy.q_function[next_state[0], next_state[1]], 
                    key=self.policy.q_function[next_state[0], next_state[1]].get
                )
                self.policy.q_function[state[0], state[1]][action] += (
                    self.step_size * (
                        reward + 
                        self.gamma * (
                            self.policy.q_function[next_state[0], next_state[1]][next_action]
                        )
                        - self.policy.q_function[state[0], state[1]][action]
                    )
                )
                state = next_state
        self.display_q_function(self.policy.q_function)

    def display_q_function(self, Qfunction):
        window_size = 700
        border_width = 1

        cell_size = (window_size // len(self.maze.reward_list[0]), window_size// len(self.maze.reward_list))
        pygame.init()

        screen = pygame.display.set_mode((window_size, window_size), pygame.DOUBLEBUF)
        colors = { 
            -1: (255, 255, 255), 
            -2: (0, 0, 255),
            -10: (255, 0, 0), 
            10: (0, 255, 0), 
            40: (0, 255, 255) } 
        running = True
        font = pygame.font.Font(None, 24)  # Font for rendering text
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    CONTINUE = False
            #Display the maze
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # screen.fill([255,255,255])
            for state in Qfunction.keys():

                pygame.draw.rect(
                    screen,  
                    (255, 255, 255),
                    pygame.Rect(
                        state[0] * cell_size[0], 
                        state[1] * cell_size[1], 
                        cell_size[0] - border_width, 
                        cell_size[1] - border_width
                    )
                )
                font = pygame.font.SysFont(None, 25)
                positions = {
                    'up': (state[0] * cell_size[0] + cell_size[0] / 2, state[1] * cell_size[1] + cell_size[1] / 4),
                    'down': (state[0] * cell_size[0] + cell_size[0] / 2, state[1] * cell_size[1] + 3 * cell_size[1] / 4),
                    'left': (state[0] * cell_size[0] + cell_size[0] / 4, state[1] * cell_size[1] + cell_size[1] / 2),
                    'right': (state[0] * cell_size[0] + 3 * cell_size[0] / 4, state[1] * cell_size[1] + cell_size[1] / 2),
                }

                for action, value in Qfunction[(state[1], state[0])].items():
                    value_text = font.render("{:.2f}".format(value), True, (0, 0, 0))
                    text_rect = value_text.get_rect()
                    text_rect.center = positions[action]
                    screen.blit(value_text, text_rect)

                center = (state[0] * cell_size[0] + cell_size[0] / 2, state[1] * cell_size[1] + cell_size[1] / 2)
                corners = {
                    'up': (state[0] * cell_size[0], state[1] * cell_size[1]),
                    'down': (state[0] * cell_size[0] + cell_size[0], state[1] * cell_size[1] + cell_size[1]),
                    'left': (state[0] * cell_size[0], state[1] * cell_size[1] + cell_size[1]),
                    'right': (state[0] * cell_size[0] + cell_size[0], state[1] * cell_size[1]),
                }

                for corner in corners.values():
                    pygame.draw.line(screen, (0, 0, 0), center, corner, 1)

                pygame.display.update()
                # Display the policy values and directions
        

            pygame.display.flip()