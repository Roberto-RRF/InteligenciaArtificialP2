from get_euclidean_distance import euclidean_distance_between_cities_string

def branch_and_bound(graph, start, goal):
    # Inicialización
    explored = set()
    queue = [(0, start)]
    best_cost = {start: 0}
    parent = {start: None}

    # Ciclo principal
    while queue:
        # Extraemos el nodo con menor costo
        cost, current = min(queue, key=lambda x: x[0])
        queue.remove((cost, current))
        explored.add(current)

        # Comprobamos si hemos encontrado la solución
        if current == goal:
            path = [current]
            while parent[current] is not None:
                path.append(parent[current])
                current = parent[current]
            return list(reversed(path)), best_cost[goal]

        # Generamos los sucesores
        for neighbor, distance in graph[current]:
            if neighbor not in explored:
                # Actualizamos el costo estimado
                estimate = cost + distance + euclidean_distance_between_cities_string(neighbor, goal)
                if neighbor not in best_cost or estimate < best_cost[neighbor]:
                    best_cost[neighbor] = estimate
                    parent[neighbor] = current
                    queue.append((estimate, neighbor))

        # Ordenamos la cola de prioridad
        queue.sort()

    # No se encontró solución
    return None, None
