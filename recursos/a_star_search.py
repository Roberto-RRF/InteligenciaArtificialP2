from .HaversineDistance import *

#Responsable del algoritmo: Roberto
def a_star_algorithm(tree, start, goal):
    """
    Algoritmo de búsqueda A* para árboles.
    tree: diccionario con los nodos del árbol y sus conexiones
          Ejemplo: {'acapulco': [('chilpancingo', 140)], 'acayucan': [('alvarado', 110), ('tehuantepec', 80)], ...}
    start: nodo inicial
    goal: nodo objetivo
    Devuelve una lista de nodos en el camino óptimo desde el nodo inicial al objetivo.
    """

    # Función de heurística (en este caso, la distancia de Haversine)
    def heuristic(nodo):
        return HaversineDistanceBetweenCities(cities_coordinates[nodo], cities_coordinates[goal])


    # Inicialización de variables
    open_set = set([start]) #open_set: Set de los nodos del grafo que aún no han sido visitados, pero son hijos de los nodos del grafo que ya se han visitado
    closed_set = set()#closed_set: Incluye todos los nodos ya visitados en la ejecución del algoritmo
    parent = {}#parent: Diccionario con el formato { Nodo Hijo : Nodo Padre}; incluye los padres de todos los nodos del grafo
    g_score = {start: 0}#g_score: Diccionario que va a incluir los costos de traslado desde el nodo inicial hasta el nodo seleccionado   // Formato: {Nodo seleccionado : costo desde el nodo inicial}
    f_score = {start: heuristic(start)}#f_score: Diccionario con el costo calculado de f(n) : (heurística + costo dentro del grafo)

    # Búsqueda
    #Mientras exista el open_set
    while open_set:
        # Obtener el nodo con el costo f(n) más bajo
        current = min(open_set, key=lambda x: f_score[x])
        #Si encuentra una solución
        if current == goal:
            print("RESULTADO")
            print("---------------------------------------------------------------------")
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return list(reversed(path))
        #Una vez visitado el nodo, se elimina del open_set y se añade al closed set
        open_set.remove(current)
        closed_set.add(current)
        #Se obtienen los hijos del nodo actual y sus costo de traslado desde el mismo
        for neighbor, cost in tree.get(current, []):
            #Si el algoritmo ya se ha expandido desde ese nodo hijo, se ignora
            if neighbor in closed_set:
                continue
            #Si no, se le calcula el costo de traslado desde el nodo inicial
            tentative_g_score = g_score[current] + cost
            #Si el nodo no se encuentra en el open set o se le ha calculado un g_score menor en el paso anterior
            if neighbor not in open_set or tentative_g_score < g_score[neighbor]:
                #Se registra el padre del nodo y se calcula el costo de la f(n) del mismo
                parent[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor)
                #En caso de no estar en el open_set, se agrega
                if neighbor not in open_set:
                    open_set.add(neighbor)

    return None  # No se encontró un camino
