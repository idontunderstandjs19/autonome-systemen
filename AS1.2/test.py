import numpy as np

# Defineer parameters en roep de functie aan
reward_list = np.array([[-1, -1, -1, 40],
               [-1, -1, -10, -10],
               [-1, -1, -1, -1],
               [10, -2, -1, -1]])

value_grid = np.array([[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0], 
              [0, 0, 0, 0]])

discount_factor = 1
iterations = 8

def value_iteration(reward_list, value_grid, discount_factor, iterations):
    rows, cols = reward_list.shape
    end_states = [(0, 3), (3, 0)]  # Definieer de posities van de eindstaten

    for t in range(iterations):
        new_values = np.copy(value_grid)

        for i in range(rows):
            for j in range(cols):
                if (i, j) in end_states:
                    continue  # Sla de eindstaten over

                values = []

                # Check boven
                if i > 0:
                    values.append(reward_list[i-1, j] + discount_factor * value_grid[i-1, j])
                # Check beneden
                if i < rows - 1:
                    values.append(reward_list[i+1, j] + discount_factor * value_grid[i+1, j])
                # Check links
                if j > 0:
                    values.append(reward_list[i, j-1] + discount_factor * value_grid[i, j-1])
                # Check rechts
                if j < cols - 1:
                    values.append(reward_list[i, j+1] + discount_factor * value_grid[i, j+1])

                max_value = max(values) if values else 0
                new_values[i, j] = max_value

        # Update value_grid, maar behoud de waarde van eindstaten op 0
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in end_states:
                    value_grid[i, j] = new_values[i, j]

        # Print elke iteratie de grid om de voortgang te tonen
        print(f"Iteratie: {t + 1}")
        print(value_grid)
        

value_iteration(reward_list, value_grid, discount_factor, iterations)
