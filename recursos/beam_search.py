"""
Universidad Panamericana
Inteligencia Artificial
Integrantes del equipo:
    Felipe de Jesús Hernández Pérez
    Roberto Requejo Fernández
    Sebastián Ruíz Sandoval Suárez
Proyecto: Algoritmos Informados 

Generación del archivo: 9 de abril de 2023
Versión del código: 1.0.0

Descripción
El presente archivo incluye la función para realizar la búsqueda informada "beam search"

Ejecucion del programa
        Correr el programa main.py y desde ahí seleccionar la opción correspondiente a la búsqueda beam search
    
    Entradas:
        1) Nombres del nodo origen y el nodo objetivo, valor de la k de expansión, árbol de búsqueda y
        un booleano que indique si se va a mostrar o no el proceso de búsqueda
    
    Salidas:
        a) En caso de existir una solución, imprime en pantalla la ruta de obtenida luego de realizar la búsqueda informada "beam search"
        b) En caso contrario, imprime en pantalla los nodos recorridos por el algoritmo antes de determinar que no hay resultado
"""
#Dependencias
#El archivo generate_states, para tener acceso al árbol
from .generate_states import *

#Variables globales
#unidirectional_tree: Almacena el arbol unidireccional generado por generate_states()
#tree: Almacena el árbol direccionado generado por generate_states()
unidirectional_tree, tree = generate_states()

#Responsable del algoritmo: Felipe
def beam_search(tree,start, goal,k,showProcess=False):
    #Variables
    queue=[(start,0)]#queue: Lista de tuplas con los nombres de los nodos que se van a visitar y sus pesos dentro del grafo
    path=[]#path: Variable que almacenará el camino recorrido por el algoritmo, en caso de llegar al nodo objetivo
    parents={}#parents: Diccionario con los padres de cada uno de los nodos dentro del grafo
    names_queue=[start]#names_queue: Lista con los nombres de los nodos que se van a visitar durante la ejecución del algoritmo; se regresa al usuario en caso de no obtener el resultado
    current_state=start#current_state: estado actual que está visitando el algoritmo
    n_paso=1 #Número de pasos, variable que se va a utilizar en caso de que el usuario quiera que se muestre el proceso del algoritmo
    #Mientras queden algoritmospor visitar...
    while len(queue)>0:
        #Se crea una lista temporal, en la que se almacenarán todos los hijos del nodo del estado actual
        temp_queue=[]
        #En caso de que el estado actual sea el nodo objetivo, se le notifica al usuario se llena el path con el camino recorrido durante la ejecución del algoritmo
        if goal==current_state:
            print("---------------------------------------------------------------------------------")
            print("SOLUCIÓN ENCONTRADA")
            path.append(current_state)
            while (parents[current_state] in parents):
                current_state=parents[current_state]
                path.append(parents[current_state])
            path.reverse()
            return path
        #En caso contrario, obtiene los hijos del nodo actual y los añade al queue temporal
        else:
            for hijo,costo in tree.get(current_state,[]):
                    temp_queue.append((hijo,(costo+queue[0][1])))
                    parents[hijo]=current_state
            #Ordena los elementos del queue temporal por su costo y elimina elementos hasta quedarse únicamente con una cantidad dentro del límite
            # k establecido por el usuario
            temp_queue.sort(key=lambda x:x[1])
            while len(temp_queue)>k:
                temp_queue.pop()
            #Una vez eliminados los nodos por los que no se va a expandir el algoritmo, añade los mejores nodos (por los que va a expandirse)
            # al queue, en caso de ya estar registrados dentro del queue, se omite su adición
            for elemento in temp_queue:
                if (elemento[0]) not in names_queue:
                    names_queue.append(elemento[0])
                    queue.append((elemento[0],elemento[1]))
            #Elimina el nodo actual del queue, pues es el de menor costo; reordena la lista por orden descendente de costos y
            # si la lista todavía contiene elementos, selecciona el primero de la lista como nuevo nodo actual
            queue.pop(0)
            queue.sort(key=lambda x:x[1])
            if showProcess:
                print("--------------------------Paso "+str(n_paso)+"-------------------------")
                print("Nodo actual: "+current_state)
                print("Valor de k: "+str(k))
                print("Hijos válidos de "+current_state+":")
                print(temp_queue)
                print("Nodos por expandir (ordenados por peso)")
                print(queue)
                n_paso=n_paso+1
            if len(queue)>0:
                current_state=queue[0][0]
#Si el algoritmo no llega al obetivo, le informa al usuario y regresa una lista con todos los nodos visitados
    print("El algoritmo no ha podido encontrar una solución\nIntente modificar el valor de k si está seguro de que el algorimto puede encontrar una solución al problema")
    print("Nodos visitados:")
    return names_queue