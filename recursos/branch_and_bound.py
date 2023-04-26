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
Este algoritmo realiza la búsqueda informada branch and bound

Ejecucion del programa
        Opcion 1) Selecciona la opción ejecuta el archivo main.py y selecciona la opción correspondiente
    
    Entradas:
        1) El grafo de búsqueda, el nodo inicial y final, y un booleano para método de entrada
    
    Salidas:
        1) Regresa una lista con los nodos visitados que forman parte del camino
"""


#Dependencias
#Utilizamos el archivo HarversinDistance para sacar la euristica de cada nodo.
from .HaversineDistance import HaversineDistanceBetweenCitiesString

import math

#Responsable: Roberto Requejo
def branch_and_bound(graph, start, goal, showProcess=False):
    # Inicialización
    explored = set()
    queue = [(0, start)]
    best_cost = {start: 0}
    parent = {start: None}
    n_pasos=1

   

    # Ciclo principal
    while queue:
        # Extraemos el nodo con menor costo
        cost, current = min(queue, key=lambda x: x[0])
        queue.remove((cost, current))
        explored.add(current)
        #Impresión del paso a paso del algoritmo de búsqueda
        if showProcess:
            porVisitar=[]
            print('----------------------------------Paso '+str(n_pasos)+'------------------------------------')
            print('Nodo actual: '+current)
            print('Costo del nodo: '+str(best_cost[current]))
            print('Nodos visitados: ')
            print(explored)
            n_pasos+=1
        # Comprobamos si hemos encontrado la solución
        if current == goal:
            print('------------------------------SOLUCIÓN ENCONTRADA---------------------------------------')
            path = [current]
            while parent[current] is not None:
                path.append(parent[current])
                current = parent[current]
            return list(reversed(path)), best_cost[goal]

        # Generamos los sucesores
        for neighbor, distance in graph[current]:
            if neighbor not in explored:
                # Actualizamos el costo estimado
                estimate = cost + distance + HaversineDistanceBetweenCitiesString(neighbor, goal)
                if neighbor not in best_cost or estimate < best_cost[neighbor]:
                    best_cost[neighbor] = estimate
                    parent[neighbor] = current
                    queue.append((estimate, neighbor))

        # Ordenamos la cola de prioridad
        queue.sort()

    # No se encontró solución
    return None, None
