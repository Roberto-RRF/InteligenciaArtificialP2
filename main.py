import sys
sys.path.append('./recursos')

# Importamos la funcion greedy_best_first_search
from recursos.greedy_best_first_search import greedy_best_first_search
from recursos.a_star_search import a_star_algorithm
from recursos.steepest_ascent_hill_climbing import steepest_ascent_hill_climbing
from recursos.branch_and_bound import branch_and_bound
from recursos.best_search import best_search


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
while 1==1:
    print("Seleccione el algoritmo de búsqueda a ejecutar")
    print("[1] greedy best first search")
    print("[2] A star")
    print("[3] A star con pesos")
    print("[4] Beam Search")
    print("[5] Steeping Hill Climbing")
    print("[6] Stochastic Hill Climbing")
    print("[7] Simmulated annealing")
    print("[8] Best Search")
    print("[9] Branch and bound")
    print("Para salir, oprima cualquier otra tecla...")
    algoritmo=input("Seleccione el algoritmo a ejecutar: ")
    if algoritmo=='1':
        print("Usted ha seleccionado el algoritmo greedy best first search")
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
        muestraPasos=input("¿Desea ver la ejecución paso a paso de este algoritmo? [Y/N]")
        if muestraPasos=='Y' or muestraPasos=='y':
            resultado = greedy_best_first_search(tree,initial_state,goal_state,True)
            print(resultado)
        else:
            resultado = greedy_best_first_search(tree,initial_state,goal_state,False)
            print(resultado)
        input()
    else:
        print("Si estás viendo esto, todavía no acabo de programar el menú")
        break
