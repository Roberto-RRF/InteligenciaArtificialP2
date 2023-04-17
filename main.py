import sys
sys.path.append('./recursos')

# Importamos la funcion greedy_best_first_search
# from recursos.greedy_best_first_search import greedy_best_first_search
# from recursos.a_star_search import a_star_algorithm
# from recursos.weighted_a_star_search import a_star_with_weights
# from recursos.steepest_ascent_hill_climbing import steepest_ascent_hill_climbing
from recursos.branch_and_bound import branch_and_bound
from recursos.best_search import best_search


# Importamos la funcion generate_states
from recursos.generate_states import generate_states




 
bidireccional_tree, tree = generate_states()

# Definimos el estado inicial y el estado final
initial_state = 'CANCUN'
goal_state = 'CABO SAN LUCAS'


# res1 = greedy_best_first_search(Bidireccional_tree, initial_state, goal_state)
# res2 = greedy_best_first_search(tree, initial_state, goal_state)
# print('Bidireccional_tree: ', res1)

res1 = best_search(bidireccional_tree, initial_state, goal_state)
print(res1)
