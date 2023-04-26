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
Este programa funciona solicita al usuario dos ciudades cualesquiera de México y le permite realizar cualquier tipo de búsqueda informada para conectarlas.
En adición a esto, el programa permite ver al usuario el procedimiento que el programa siguió para llegar a la solución

Ejecucion del programa
     Dentro de la terminal, simplemente ejecutar el programa   
    Entradas:
        Ninguna, pero dependiendo del algoritmo seleccionado, se le pueden solicitar diferentes tipos de datos para realizar la búsqueda
    
    Salidas:
        1) Imprime en pantalla el resultado de la búsqueda informada realizada así como cada uno de los pasos  de la ejecución, en caso de haber querido verlos
"""

import sys
import math
import random
sys.path.append('./recursos')

# Dependencias
#Importamos de los diferentes códigos generados en clase, sus funciones de búsqueda, para que el programa pudiera realizarlas correctamente
#estos códigos van desde el greedy best first search, hasta el simulated annealing
from recursos.greedy_best_first_search import greedy_best_first_search
from recursos.a_star_search import a_star_algorithm
from recursos.steepest_ascent_hill_climbing import steepest_ascent_hill_climbing
from recursos.branch_and_bound import branch_and_bound
from recursos.best_search import best_search
from recursos.stochastic_hill_climbing_search import stochastic_hill_climbing
from recursos.beam_search import beam_search

# En adición a esto, importamos el archivo generate states, que nos crea el árbol de búsqueda (tanto unidireccional como direccionado) que utilizaremos en la ejecución del programa
from recursos.generate_states import generate_states

#Variables globales
#origen_valido y destino_valido sirven como banderas para verificar dentro del menú, que los nombres de los nodos introducidos para realizar la búsqueda están correctamente escritos
origen_valido =False
destino_valido=False
#bidirectional_tree y tree almacenan el arbol unidireccional y el arbol dirigido de búsqueda respectivamente
bidireccional_tree, tree = generate_states()
print("Inteligencia Artificial")
print("Proyecto Segundo Parcial")
print("-Felipe de Jesús Hernández Pérez\n-Roberto Requejo Fernández\n-Sebastián Ruíz Sandoval Suárez")
print("Introduzca los datos esenciales para la búsqueda:")
#Se le solicitan los nodos de origen y destino al usuario, y hasta que no sean correctamente introducidos, no se le permite realizar ninguna búsqueda en el programa
while origen_valido==False:
            initial_state=input("Introduzca la ciudad de origen de su búsqueda: ")
            initial_state=initial_state.upper()
            print("Ciudad origen: "+initial_state)
            if initial_state in tree:
                origen_valido=True
            else:
                print("Por favor, introduzca una ciudad válida, escrita completamente en mayúsculas y sin acentos")
while destino_valido==False:
    goal_state=input("Introduzca la ciudad destino de su búsqueda: ")
    goal_state=goal_state.upper()
    print("Ciudad destino: "+goal_state)
    if goal_state in tree:
        destino_valido=True
    else:
        print("Por favor, introduzca una ciudad válida, escrita completamente en mayúsculas y sin acentos")
#Una vez introducidos los nodos de la búsqueda, el usuario entra al menú de selección de búsqueda, este se va a repetir infinitamente hasta que el usuario decida salir del programa
while 1==1:
    print("Seleccione el algoritmo de búsqueda a ejecutar, si selecciona una opción inválida, regresará a este menú")
    print("[1] greedy best first search")
    print("[2] A star")
    print("[3] A star con pesos")
    print("[4] Beam Search")
    print("[5] Steeping Hill Climbing")
    print("[6] Stochastic Hill Climbing")
    print("[7] Simmulated annealing")
    print("[8] Best Search") 
    print("[9] Branch and bound")
    print("Para salir, oprima ESPACIO...")
    algoritmo=input("Seleccione el algoritmo a ejecutar: ")
#Dependiendo del algoritmo seleccionado se le podrán pedir o no datos adicionales, pero siempre se le solicitará al usuario si quiere ver o no el procedimiento paso a paso del algoritmo
# de búsqueda elegido
    if algoritmo=='1':
        print("Usted ha seleccionado el algoritmo greedy best first search")
        muestraPasos=input("¿Desea ver la ejecución paso a paso de este algoritmo? [Y/N]")
        if muestraPasos=='Y' or muestraPasos=='y':
            resultado = greedy_best_first_search(tree,initial_state,goal_state,True)
            print(resultado)
        else:
            resultado = greedy_best_first_search(tree,initial_state,goal_state,False)
            print(resultado)
    if algoritmo=='2':
        print("Usted ha seleccionado el algoritmo A star")
        muestraPasos=input("¿Desea ver la ejecución paso a paso de este algoritmo? [Y/N]")
        if muestraPasos=='Y' or muestraPasos=='y':
            resultado = a_star_algorithm(tree,initial_state,goal_state,1,True)
            print(resultado)
        else:
            resultado = a_star_algorithm(tree,initial_state,goal_state,1,False)
            print(resultado)
    if algoritmo=='3':
    #Si elige el algoritmo A* con pesos se le pedirá que asigne un valor para el coeficiente por el que se va a multiplicar la heurística
    #El usuario no podrá seguir avanzando con el programa si no introduce un valor numérico mayor a 1
         print("Usted ha seleccionado el algoritmo A star con pesos")
         while True:
            try:
                k=float(input("Introduzca el valor de k: "))
                if k>1:
                    break
                else:
                    print("Introduzca un número mayor a 1")
            except:
                print("Introduzca un valor válido (un número mayor a 1)")
         muestraPasos=input("¿Desea ver la ejecución paso a paso de este algoritmo? [Y/N]")
         if muestraPasos=='Y' or muestraPasos=='y':
            resultado = a_star_algorithm(tree,initial_state,goal_state,k,True)
            print(resultado)
         else:
            resultado =(tree,initial_state,goal_state,k,False)
            print(resultado)
    if algoritmo=='4':
        print("Usted ha seleccionado el algoritmo beam search")
        while True:
    #Si el usuario selecciona el algoritmo beam search, no podrá avanzar hasta especificar un valor límite de anchura
    #Si no introduce un número entero, no podrá avanzar en el programa
            try:
                k=int(input("Introduzca el valor de W (límite de anchura): "))
                break
            except:
                print("Introduzca un valor válido (un número entero)")
        muestraPasos=input("¿Desea ver la ejecución paso a paso de este algoritmo? [Y/N]")
        if muestraPasos=='Y' or muestraPasos=='y':
            resultado = beam_search(tree,initial_state,goal_state,k,True)
            print(resultado)
        else:
            resultado = beam_search(tree,initial_state,goal_state,k,False)
            print(resultado)
    if algoritmo=='5':
        print("Usted ha seleccionado el algoritmo Steepest ascent Hill Climbing")
        muestraPasos=input("¿Desea ver la ejecución paso a paso de este algoritmo? [Y/N]")
        if muestraPasos=='Y' or muestraPasos=='y':
            resultado = steepest_ascent_hill_climbing(tree,initial_state,goal_state,True)
            print(resultado)
        else:
            resultado = steepest_ascent_hill_climbing(tree,initial_state,goal_state,False)
            print(resultado)
    if algoritmo=='6':
        print ("Usted ha seleccionado el algoritmo Stochastic Hill Climbing")
        while True:
        #Si el usuario selecciona el algoritmo beam search, no podrá avanzar hasta especificar un valor máximo de iteraciones
        #Si no introduce un número entero, no podrá avanzar en el programa
            try:
                k=int(input("Introduzca el valor máximo de iteraciones: "))
                break
            except:
                print("Introduzca un valor válido (un número entero)")
        muestraPasos=input("¿Desea ver la ejecución paso a paso de este algoritmo? [Y/N]")
        if muestraPasos=='Y' or muestraPasos=='y':
            resultado = stochastic_hill_climbing(bidireccional_tree,initial_state,goal_state,k,True)
            print(resultado)
        else:
            resultado = stochastic_hill_climbing(bidireccional_tree,initial_state,goal_state,k,False)
            print(resultado)
    if algoritmo=='7':
        print ("Usted ha seleccionado el algoritmo Simmulated annealing")
    if algoritmo=='8':
        print ("Usted ha seleccionado el algoritmo best search")
        canmuestraPasos=input("¿Desea ver la ejecución paso a paso de este algoritmo? [Y/N]")
        if muestraPasos=='Y' or muestraPasos=='y':
            resultado = best_search(tree,initial_state,goal_state,True)
            print(resultado)
        else:
            resultado = best_search(tree,initial_state,goal_state,False)
            print(resultado)
    if algoritmo=='9':
        print ("Usted ha seleccionado el algoritmo branch and bound")
        muestraPasos=input("¿Desea ver la ejecución paso a paso de este algoritmo? [Y/N]")
        if muestraPasos=='Y' or muestraPasos=='y':
            resultado = branch_and_bound(tree,initial_state,goal_state,True)
            print(resultado)
        else:
            resultado = branch_and_bound(tree,initial_state,goal_state,False)
            print(resultado)
    #Una vez el usuario introduce un espacio dentro del menú de opciones, el programa termina su ejecución
    if algoritmo==' ':
        print('gracias por usar el programa!!!')
        break
    print("--------------------------------------------------------------------------------")
