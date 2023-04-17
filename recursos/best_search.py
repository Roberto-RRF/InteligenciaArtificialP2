from get_euclidean_distance import euclidean_distance_between_cities_string


def best_search(graph, start, goal):
    frontier = [(0, start)] # cola de prioridad con distancia acumulada y nodo actual
    visited = set() # nodos visitados
    parent = {} # registro de nodos padre
    while frontier:
        frontier.sort() # ordenar lista por prioridad
        (cost, current) = frontier.pop(0) # expandir el nodo con menor costo
        if current == goal:
            # reconstruir el camino desde el nodo objetivo hasta el nodo inicial
            path = [current]
            while current != start:
                current = parent[current]
                path.append(current)
            path.reverse()
            return path # regresar el camino de nodos visitados
        visited.add(current) # marcar nodo como visitado
        for (neighbor, distance) in graph[current]:
            if neighbor not in visited:
                # calcular costo acumulado y distancia estimada
                new_cost = cost + distance
                heuristic = euclidean_distance_between_cities_string(neighbor, goal) # función heurística (distancia Euclidiana)
                priority = new_cost + heuristic # calcular prioridad para la lista
                frontier.append((priority, neighbor)) # agregar a la cola de prioridad
                parent[neighbor] = current # actualizar registro de nodos padre
    return None # si no se llega al objetivo, regresar None
