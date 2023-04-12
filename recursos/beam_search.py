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
El presente archivo incluye la función para realizar la búsqueda informada "beam search"

Ejecucion del programa
        Correr el programa main.py y desde ahí seleccionar la opción correspondiente a la búsqueda beam search
    
    Entradas:
        1) Nombres del nodo origen y el nodo objetivo, valor de la k de expansión, árbol de búsqueda y
        un booleano que indique si se va a mostrar o no el proceso de búsqueda
    
    Salidas:
        1) Imprime en pantalla la ruta de obtenida luego de realizar la búsqueda informada "beam search"
"""
from .generate_states import *


unidirectional_tree, tree = generate_states()

def beam_search(start, goal, k, tree, showProcess=False):
    queue=[(start,0)]
    path=[]
    parents={}
    names_queue=[start]
    current_state=start
    while len(queue)>0:
        temp_queue=[]
        if goal==current_state:
            print(parents)
            while (parents[current_state] in parents):
                print(parents[current_state])
                current_state=parents[current_state]
                path.append(parents[current_state])
            #path.append(current_state)
            path.reverse()
            return path
        else:
            for hijo,costo in tree.get(current_state,[]):
                    temp_queue.append((hijo,(costo+queue[0][1])))
                    parents[hijo]=current_state
            temp_queue.sort(key=lambda x:x[1])
            while len(temp_queue)>k:
                temp_queue.pop()
            for elemento in temp_queue:
                print("Elemento")
                print(elemento)
                if (elemento[0]) not in names_queue:
                    names_queue.append(elemento[0])
                    queue.append((elemento[0],elemento[1]))
            queue.pop(0)
            queue.sort(key=lambda x:x[1])
            if len(queue)>0:
                current_state=queue[0][0]
    print("El algoritmo no ha podido encontrar una solución\nIntente modificar el valor de k si está seguro de que el algorimto puede encontrar una solución al problema")
    print("Nodos visitados:")
    return names_queue