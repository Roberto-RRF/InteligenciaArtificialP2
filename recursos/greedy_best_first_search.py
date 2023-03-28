from queue import PriorityQueue
# importamos get_euclidean_distance para calcular la distancia euclideana entre dos ciudades
from get_euclidean_distance import cities_coordinates


def greedy_best_first_search(tree, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    came_from[start] = None
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        
        for neighbor, distance in tree[current]:
            if neighbor not in came_from:
                priority = distance_to_goal(neighbor, goal)
                frontier.put(neighbor, priority)
                came_from[neighbor] = current
    
    return None


def distance_to_goal(neighbor, goal):
    return 1