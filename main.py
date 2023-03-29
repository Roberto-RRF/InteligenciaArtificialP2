import sys
sys.path.append('./recursos')

# Importamos la funcion greedy_best_first_search
from recursos.greedy_best_first_search import greedy_best_first_search
from recursos.a_star_search import a_star_algorithm

# Importamos la funcion generate_states
from recursos.generate_states import generate_states


 
bidireccional_tree, tree = generate_states()

# Definimos el estado inicial y el estado final
initial_state = 'CANCUN'
goal_state = 'CABO SAN LUCAS'


# res1 = greedy_best_first_search(Bidireccional_tree, initial_state, goal_state)
# res2 = greedy_best_first_search(tree, initial_state, goal_state)
# print('Bidireccional_tree: ', res1)

res1 = a_star_algorithm(tree, initial_state, goal_state)
print(res1)
