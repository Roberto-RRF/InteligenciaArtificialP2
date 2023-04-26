import random

def calculate_distance(path, tree):
    distance = 0
    for i in range(len(path)-1):
        for node, edges in tree[path[i]]:
            if node == path[i+1]:
                distance += edges
    return distance



# Definimos la función de búsqueda Stochastic Hill Climbing
def stochastic_hill_climbing(tree, initial_state, goal_state, max_iterations=1000, showProcess=False):

    current_state = [initial_state]
    current_distance = calculate_distance(current_state, tree)
    for i in range(max_iterations):
        neighbors = []
        for node, edges in tree[current_state[-1]]:
            neighbor = current_state.copy()
            neighbor.append(node)
            neighbors.append(neighbor)
        if not neighbors:
            return current_state
        neighbor_distances = [calculate_distance(neighbor, tree) for neighbor in neighbors]
        best_distance = min(neighbor_distances)
        if best_distance >= current_distance:
            return current_state
        best_neighbors = [neighbors[i] for i in range(len(neighbors)) if neighbor_distances[i] == best_distance and neighbors[i][-1] == goal_state]
        if best_neighbors:
            return best_neighbors[0]
        else:
            best_neighbors = [neighbors[i] for i in range(len(neighbors)) if neighbor_distances[i] == best_distance]
            current_state = random.choice(best_neighbors)
            current_distance = best_distance
    return current_state