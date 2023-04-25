import sys
sys.path.append('./recursos')

# Importamos la funcion greedy_best_first_search
from recursos.greedy_best_first_search import greedy_best_first_search
from recursos.a_star_search import a_star_algorithm
from recursos.steepest_ascent_hill_climbing import steepest_ascent_hill_climbing
from recursos.branch_and_bound import branch_and_bound
from recursos.best_search import best_search
from recursos.stochastic_hill_climbing_search import stochastic_hill_climbing
from recursos.beam_search import beam_search

# Importamos la funcion generate_states
from recursos.generate_states import generate_states
origen_valido =False
destino_valido=False


 
bidireccional_tree, tree = generate_states()

# Definimos el estado inicial y el estado final



# res1 = greedy_best_first_search(Bidireccional_tree, initial_state, goal_state)
# res2 = greedy_best_first_search(tree, initial_state, goal_state)
# print('Bidireccional_tree: ', res1)


print("Inteligencia Artificial")
print("Proyecto Segundo Parcial")
print("-Felipe de Jesús Hernández Pérez\n-Roberto Requejo Fernández\n-Sebastián Ruíz Sandoval Suárez")
print("Introduzca los datos esenciales para la búsqueda:")
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
    if algoritmo==' ':
        print('gracias por usar el programa!!!')
        break
    print("--------------------------------------------------------------------------------")
