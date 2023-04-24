from .HaversineDistance import *


def greedy_best_first_search(tree, start, goal, showProcess=False):
    n_pasos=1
    frontier = [start]
    came_from = {start: None}

    while frontier:
        frontier.sort(key=lambda x: HaversineDistanceBetweenCities(cities_coordinates[x], cities_coordinates[goal]))
        current = frontier.pop(0)
        
        if current == goal:
            print("---------------------------SOLUCÓN ENCONTRADA-------------------------------")
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for neighbor, distance in sorted(tree[current], key=lambda x: HaversineDistanceBetweenCities(cities_coordinates[x[0]], cities_coordinates[goal])):
            if neighbor not in came_from:
                frontier.append(neighbor)
                came_from[neighbor] = current
        if showProcess:
            print("--------------------------------------- Paso "+str(n_pasos)+"------------------------------------------------------------")
            print("Nodo actual: "+current)
            print("Nodos por recorrer: ")
            print(frontier)
            n_pasos+=1


    return None

