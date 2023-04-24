from .HaversineDistance import HaversineDistanceBetweenCitiesString


def best_search(graph, start, goal, showProcess=False):
    frontier = [(0, start)] # cola de prioridad con distancia acumulada y nodo actual
    visited = set() # nodos visitados
    parent = {} # registro de nodos padre
    n_paso=1 # número de pasos (utilizado en caso de que el usuario quiera ver el proceso del objetivo)
    while frontier:
        frontier.sort() # ordenar lista por prioridad
        (cost, current) = frontier.pop(0) # expandir el nodo con menor costo
        if showProcess:
            print('------------------------------ Paso '+str(n_paso)+'----------------------------------------')
            print('Nodo actual: '+current)
            print('Costo acumulado: '+str(cost))
            print('Nodos visitados: ')
            print(visited)
            print('Cola de prioridad:')
            print(frontier)
        if current == goal:
            # reconstruir el camino desde el nodo objetivo hasta el nodo inicial
            print('----------------- SOLUCIÓN ENCONTRADA --------------------------')
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
                heuristic = HaversineDistanceBetweenCitiesString(neighbor, goal) # función heurística (distancia de Haversine)
                priority = new_cost + heuristic # calcular prioridad para la lista
                frontier.append((priority, neighbor)) # agregar a la cola de prioridad
                parent[neighbor] = current # actualizar registro de nodos padre
        
    return None # si no se llega al objetivo, regresar None
