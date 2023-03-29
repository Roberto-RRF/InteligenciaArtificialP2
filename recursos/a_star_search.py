from get_euclidean_distance import euclidean_distance_between_cities_string

def a_star_algorithm(tree, start, goal):
    """
    Algoritmo de búsqueda A* para árboles.

    tree: diccionario con los nodos del árbol y sus conexiones
          Ejemplo: {'acapulco': [('chilpancingo', 140)], 'acayucan': [('alvarado', 110), ('tehuantepec', 80)], ...}
    start: nodo inicial
    goal: nodo objetivo

    Devuelve una lista de nodos en el camino óptimo desde el nodo inicial al objetivo.
    """

    # Función de heurística (en este caso, la distancia en línea recta)
    def heuristic(nodo):
        return euclidean_distance_between_cities_string(nodo, goal)


    # Inicialización de variables
    open_set = set([start])
    closed_set = set()
    parent = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start)}

    # Búsqueda
    while open_set:
        # Obtener el nodo con el costo f(n) más bajo
        current = min(open_set, key=lambda x: f_score[x])

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return list(reversed(path))

        open_set.remove(current)
        closed_set.add(current)

        for neighbor, cost in tree.get(current, []):
            if neighbor in closed_set:
                continue

            tentative_g_score = g_score[current] + cost

            if neighbor not in open_set or tentative_g_score < g_score[neighbor]:
                parent[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor)
                if neighbor not in open_set:
                    open_set.add(neighbor)

    return None  # No se encontró un camino