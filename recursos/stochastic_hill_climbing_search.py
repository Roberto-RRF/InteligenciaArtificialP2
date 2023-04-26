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
Este algoritmo realiza la búsqueda informada steepest stochastic hill climbing search

Ejecucion del programa
        Opcion 1) Dentro del main selecciona la opción correspondiente
    
    Entradas:
        1) El arbol de busqueda, el nodo inicial y final, y la booleana para mostrar el proceso. 
    
    Salidas:
        1) Regresa el camino seguido para encontrar la solución.
"""

import random

# Función que implementa el algoritmo de Stochastic Hill Climbing para encontrar una ruta entre dos ciudades en un gráfico
# origin: ciudad de origen
# destination: ciudad de destino
# graph: grafo que representa las conexiones entre ciudades y sus distancias
# maxIterations: número máximo de iteraciones para evitar bucles infinitos
# Responsable: Roberto Requejo Fernández
def stochastic_hill_climbing(origin, destination, graph, maxIterations = 1000, showProcess = False):
    path = [] # Lista para almacenar la ruta desde el origen hasta el destino
    current_city = origin # Inicialización de la ciudad actual con el origen

    # Bucle que se ejecuta mientras no se alcance la ciudad de destino y no se alcance el número máximo de iteraciones
    while current_city != destination and maxIterations > 0:
        neighbors = graph[current_city] # Lista de vecinos de la ciudad actual
        if not neighbors:
            return None # Si no hay vecinos, no hay ruta posible

        neighbor_cities = [n[0] for n in neighbors] # Lista de las ciudades vecinas a la actual
        shortest_distance = min([n[1] for n in neighbors]) # Distancia más corta entre la ciudad actual y sus vecinos
        best_neighbors = [n for n in neighbors if n[1] == shortest_distance] # Lista de los vecinos con la distancia más corta
        next_city = random.choice(best_neighbors)[0] # Siguiente ciudad, elegida aleatoriamente si hay más de una con la misma distancia mínima

        if showProcess:
            print(f"Current city: {current_city}")
            print(f"Next city: {next_city}")

        path.append(current_city) # Añadir la ciudad actual a la ruta
        if graph[next_city]: # Si hay vecinos en la siguiente ciudad, avanzar a ella
            current_city = next_city

        maxIterations -= 1 # Decrementar el número de iteraciones restantes

    path.append(destination) # Añadir la ciudad de destino a la ruta
    return path # Devolver la ruta encontrada