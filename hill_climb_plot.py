import matplotlib.pyplot as plt
import numpy as np

def objective_function(x):
    return -(x - 3)**2 + 10

def hill_climbing(start, step_size=0.1, max_iterations=100):
    current_x = start
    current_score = objective_function(current_x)

    x_history = [current_x]
    score_history = [current_score]

    for i in range(max_iterations):
        neighbors = [current_x + step_size, current_x - step_size]
        neighbors_scores = [objective_function(x) for x in neighbors]

        best_neighbor_score = max(neighbors_scores)
        best_neighbor = neighbors[neighbors_scores.index(best_neighbor_score)]

        if best_neighbor_score <= current_score:
            print(f"Stopped at iteration {i}")
            break

        current_x = best_neighbor
        current_score = best_neighbor_score

        x_history.append(current_x)
        score_history.append(current_score)

        print(f"Iteration {i}: x = {current_x:.4f}, score = {current_score:.4f}")

    return current_x, current_score, x_history, score_history

# Run hill climbing
best_x, best_score, x_hist, score_hist = hill_climbing(start=0)

print(f"Best solution: x = {best_x:.4f}, score = {best_score:.4f}")

# --- Plot the results ---
x_vals = np.linspace(-2, 8, 200)
y_vals = objective_function(x_vals)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label="Objective Function", color="blue")
plt.scatter(x_hist, score_hist, color="red", label="Hill Climbing Path")
plt.plot(x_hist, score_hist, color="red", linestyle="--", alpha=0.6)

plt.title("Hill Climbing Optimization Path")
plt.xlabel("x")
plt.ylabel("Objective Function Value")
plt.legend()
plt.grid(True)
plt.show()