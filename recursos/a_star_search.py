"""
Universidad Panamericana
Inteligencia Artificial
Integrantes del equipo:
    Felipe de Jesús Hernández Pérez
    Roberto Requejo Fernández
    Sebastián Ruíz Sandoval Suárez
Proyecto: Algoritmos Informados 

Generación del archivo: 4 de abril de 2023
Versión del código: 1.0.0

Descripción
En este archivo se encuentra el algoritmo de búsqueda informada a* con pesos, que a su vez también utilizamos para realizar la búsqueda de 
a*, ya que la única diferencia entre ambos algoritmos es el agregar un coeficiente de valor mayor a 1 a la heurística que se aplica en la 
función de costos

Ejecucion del programa
    Ejecuta el archivo main.py dentro de esta carpeta y selecciona la opción correspondiente al algoritmo de búsqueda de a*
    o weighted a*, según corresponda
    
    Entradas:
       tree: diccionario con los nodos del árbol y sus conexiones
          Ejemplo: {'acapulco': [('chilpancingo', 140)], 'acayucan': [('alvarado', 110), ('tehuantepec', 80)], ...}
        start: nodo inicial
        goal: nodo objetivo
        W: Valor del coeficiente que va a multiplicar a la heurística dentro de f(n)
        Devuelve una lista de nodos en el camino óptimo desde el nodo inicial al objetivo.
        showProcess: Booleano que habilita el modo para Mostrar el proceso del algoritmo, este modo permite ver al usuario qué sucede al final de cada paso de la ejecución  
    
    Salidas:
        1) Regresa una lista con el camino para llegar desde la ciudad origen hasta la ciudad destino, usando el método de búqueda ordenada a*
"""

from .HaversineDistance import *

#Responsable del algoritmo: Roberto
def a_star_algorithm(tree, start, goal, W=1, showProcess=False):
    """
    Algoritmo de búsqueda A* para árboles.
   
    """

    # Función de heurística (en este caso, la distancia de Haversine)
    def heuristic(nodo):
        return HaversineDistanceBetweenCities(cities_coordinates[nodo], cities_coordinates[goal])


    # Inicialización de variables
    open_set = set([start]) #open_set: Set de los nodos del grafo que se tienen que visitar en la ejecución del algoritmo
    closed_set = set()#closed_set: Incluye todos los nodos ya visitados en la ejecución del algoritmo
    parent = {}#parent: Diccionario con el formato { Nodo Hijo : Nodo Padre}; incluye los padres de todos los nodos del grafo
    g_score = {start: 0}#g_score: Diccionario que va a incluir los costos de traslado desde el nodo inicial hasta el nodo seleccionado   // Formato: {Nodo seleccionado : costo desde el nodo inicial}
    f_score = {start: heuristic(start)}#f_score: Diccionario con el costo calculado de f(n) : (W*(heurística) + costo dentro del grafo)
    n_paso=0 #n_paso: Entero que representa el número de paso dentro del algoritmo, utilizado para imprimir el paso actual en el modo Mostrar Proceso
    # Búsqueda
    #Mientras exista el open_set
    while open_set:
        # Obtener el nodo con el costo f(n) más bajo
        current = min(open_set, key=lambda x: f_score[x])
        #Si encuentra una solución
        if current == goal:
            print("RESULTADO")
            print("---------------------------------------------------------------------")
            #Genera una lista con el camino de la solución y regresa el resultado
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
                f_score[neighbor] = tentative_g_score + W*(heuristic(neighbor))
                #En caso de no estar en el open_set, se agrega
                if neighbor not in open_set:
                    open_set.add(neighbor)
        #Pasos que se muestran en caso de que se habilite el modo mostrar proceso
        if showProcess==True:
            print("-------------------Paso "+str(n_paso)+"-------------------------")
            print("Nodo actual\n"+current)
            print("Nodos visitados")
            print(closed_set)
            print("Nodos por visitar")
            print(open_set)
            print("Valores de f(n) de los nodos hijos")
            for nodo in open_set:
                if f_score[nodo]:
                    print(nodo,f_score[nodo])
            n_paso=n_paso+1

    return None  # No se encontró un camino
