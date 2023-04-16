from get_euclidean_distance import euclidean_distance_between_cities_string

def a_star_with_weights(graph, start, end):
    """
    Algoritmo A* con pesos para encontrar el camino más corto desde un nodo de inicio hasta un nodo final en un grafo ponderado.

    :param graph: Un diccionario que representa el grafo. Cada clave es un nodo y su valor es una lista de tuplas que representa los nodos vecinos y los costos de cada borde.
    :param start: El nodo de inicio.
    :param end: El nodo final.
    :return: El camino más corto desde el nodo de inicio hasta el nodo final y su costo total.
    """
    # Creamos un diccionario para almacenar el costo total hasta cada nodo visitado
    visited = {start: 0}

    # Creamos un diccionario para almacenar el nodo previo a cada nodo visitado
    parent = {}

    # Creamos una lista para almacenar los nodos que se deben visitar, empezando por el nodo de inicio
    to_visit = [(0, start)]

    # Recorremos la lista de nodos que se deben visitar hasta que esté vacía o hayamos llegado al nodo final
    while to_visit:
        # Sacamos el nodo con el costo mínimo de la lista de nodos que se deben visitar
        current_cost, current_node = min(to_visit, key=lambda x: x[0])
        to_visit.remove((current_cost, current_node))

        # Si llegamos al nodo final, construimos el camino y lo devolvemos junto con su costo total
        if current_node == end:
            path = [end]
            total_cost = current_cost
            while path[-1] != start:
                path.append(parent[path[-1]])
            path.reverse()
            return path, total_cost

        # Recorremos los nodos vecinos del nodo actual
        for neighbor, cost in graph[current_node]:
            # Calculamos el costo total hasta el nodo vecino
            new_cost = visited[current_node] + cost

            # Si el nodo vecino no ha sido visitado o el nuevo costo total es menor que el costo anterior, lo agregamos a la lista de nodos que se deben visitar
            if neighbor not in visited or new_cost < visited[neighbor]:
                visited[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, end)
                to_visit.append((priority, neighbor))
                parent[neighbor] = current_node

    # Si no se encontró un camino desde el nodo de inicio hasta el nodo final, devolvemos None
    return None


def heuristic(node, goal):
    return euclidean_distance_between_cities_string(node, goal)