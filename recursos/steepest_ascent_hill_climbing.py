"""
Universidad Panamericana
Inteligencia Artificial
Integrantes del equipo:
    Felipe de Jesús Hernández Pérez
    Roberto Requejo Fernández
    Sebastián Ruíz Sandoval Suárez
Proyecto: Algoritmos Informados 

Generación del archivo: 25 de abril de 2023
Versión del código: 1.0.0

Descripción
Este algoritmo realiza la búsqueda informada steepest ascent hill climbing search

Ejecucion del programa
        Opcion 1) Dentro del main selecciona la opción correspondiente
    
    Entradas:
        1) El arbol de busqueda, el nodo inicial y final, y la booleana para mostrar el proceso. 
    
    Salidas:
        1) Regresa el camino seguido para encontrar la solución.
"""


# Definir la función principal que llama a la función de búsqueda Steepest Ascent Hill Climbing
#Responsable del algoritmo: Roberto Requejo
def steepest_ascent_hill_climbing(tree, start, end, showProcess=False):
    # Definir la función objetivo como encontrar la ruta más corta entre dos ciudades
    def shortest_path(start, end):
        visited = set()
        queue = [(start, [start])]
        while queue:
            (node, path) = queue.pop(0)
            if node not in visited:
                visited.add(node)
                if node == end:
                    return path
                for (neighbour, distance) in tree[node]:
                    queue.append((neighbour, path + [neighbour]))
        return None

    # Definir la función que genera todos los vecinos posibles de la solución actual
    def get_neighbors(state):
        neighbors = []
        for (neighbour, distance) in tree[state[-1]]:
            neighbors.append(state + [neighbour])
        return neighbors

    # Definir la función de evaluación que evalúa la calidad de cada vecino
    def evaluate(state):
        path_length = 0
        for i in range(len(state) - 1):
            for (neighbour, distance) in tree[state[i]]:
                if neighbour == state[i+1]:
                    path_length += distance
        return path_length

    # Definir la función de búsqueda Steepest Ascent Hill Climbing
    def hill_climbing(start, end):
        current_state = [start]
        while True:
            neighbors = get_neighbors(current_state)
            best_neighbor = None
            best_evaluation = evaluate(current_state)
            for neighbor in neighbors:
                evaluation = evaluate(neighbor)
                if evaluation < best_evaluation:
                    best_neighbor = neighbor
                    best_evaluation = evaluation
            if best_neighbor is not None:
                current_state = best_neighbor
            else:
                return current_state

    # Ejecutar la búsqueda Steepest Ascent Hill Climbing y devolver la ruta más corta encontrada
    shortest = hill_climbing(start, end)
    return shortest_path(start, end)