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
Este algoritmo realiza la búsqueda informada greedy best first search

Ejecucion del programa
        Opcion 1) Dentro del main selecciona la opción correspondiente
    
    Entradas:
        1) El arbol de busqueda, el nodo inicial y final, y la booleana para mostrar el proceso. 
    
    Salidas:
        1) Regresa el camino seguido para encontrar la solución.
"""
#Dependencias
#Utilizamos el archivo HarversinDistance para sacar la euristica de cada nodo.
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

