def objective_function(x):
    return -(x - 3)**2 + 10

def hill_climbing(start, step_size=0.1, max_iterations=100):
    current_x = start
    current_score = objective_function(current_x)

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

        print(f"Iteration {i}: x = {current_x:.4f}, score = {current_score:.4f}")

    return current_x, current_score

best_x, best_score = hill_climbing(start=0)
print(f"Best solution: x = {best_x:.4f}, score = {best_score:.4f}")