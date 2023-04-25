import sys
import math
import random
sys.path.append('./recursos')



# Importamos la funcion generate_states
from recursos.generate_states import generate_states




 
bidireccional_tree, tree = generate_states()


# Definimos el estado inicial y el estado final
start_city = 'CANCUN'
end_city = 'CABO SAN LUCAS'


#Función Genetic Algorithm
def genetic_algorithm(graph, population_size, num_generations, mutation_rate):
    population = generate_initial_population(population_size, graph)
    for generation in range(num_generations):
        fitness_scores = [fitness_function(chromosome, graph) for chromosome in population]
        parent1 , parent2 = select_parents(population)
        offspring = generate_offspring(parent1 , parent2)
        population = mutate_population(offspring, mutation_rate,graph)
    best_chromosome = max(population, key=lambda chromosome: fitness_function(chromosome, graph))
    return best_chromosome

#Función generate_initial_population para realizar el algoritmo de Genetic Algorithm
#Lo que hace esta función es generar una población de manera aleatoria, esta población es 
# cada uno de los nodos del grafo, los cuales representan una posible solución del problema,
# esta función toma cada nodo del grafo y los coloca de modo de un directorio para poder ver la 
# mejor solución al problema
def generate_initial_population(population_size, graph):
    population = []
    nodes = list(graph.keys())
    for i in range(population_size):
        chromosome = random.sample(nodes, len(nodes))
        population.append(chromosome)
    return population

#Función de fitness_function para realizar el algoritmo de Genetic Algorithm
"""Esta función hace la implemnetación de ver que tanta aplitud tiene cada nodo
 esto quiere decir que ve cuantos vecinos tiene cada uno de los nodos que se ecnuentran
 en el cromosoma, se busca maximizar los vecinos que son soluciones en el cromosoma"""
def fitness_function(chromosome, graph):
    fitness = 0
    for node in graph:
        for neighbor in graph[node]:
            if neighbor in chromosome:
                fitness += 1
    return fitness

#Función select_parents para realizar el algoritmo de Genetic Algorithm
"""La función genera un cruce entre dos padres la cual lo hace de la siguiente manera,
 toma un candidato y lo que hace es que selecciona un nodo de manera aleatoria para poder 
 encontrar a un candidato con el mayor fitness, ya cuando tenga el candidato con mayor fitness
 ese lo toma como padre y este procedimiento lo hace 2 veces para tener los 2 padres y lo 
 agrega a la lista de mejores andidatos la cual se guarda en padres"""
def select_parents(population):
    parent1 = random.choice(population)
    parent2 = random.choice(population)
    while parent2 == parent1 and len(population) > 1:
        parent2 = random.choice(population)
    return parent1, parent2

#Función generate_offspring para realizar el algoritmo de Genetic Algorithm
"""Esta función lo que hace es que a partir de los 2 padres crea una desendencia 
    lo hace a partir de una de las partes de cada uno de los padres para poder 
    realizar esta desecendia y esto lo hace de la siguiente manera si un número 
    aleatorio generado al azar es mayor que la tasa de cruce, se clona uno de los 
    padres como el descendiente sin realizar cruce. Si el número aleatorio es menor 
    o igual a la tasa de cruce, se selecciona un punto de cruce aleatorio entre 1 y 
    la longitud del cromosoma menos 1. Luego, se combina la primera parte del primer 
    padre con la segunda parte del segundo padre a partir del punto de cruce para 
    formar el descendiente. """
def generate_offspring(parent1, parent2):
    if len(parent1) <= 1:  # verificación de longitud de parent1
        return parent1
    crossover_point = random.randrange(1, len(parent1))
    child = parent1[:crossover_point] + parent2[crossover_point:]
    if random.random() < mutation_rate:
        mutate_population(child)
    return child

#Función mutate_population para realizar el algoritmo de Genetic Algorithm
"""Esta función lo que hace es generar una mutación en los cromosomas, esto lo hace tomando
    de forma aleatoria un nodo del cromosoma para poder realizar la mutación, esto se hace 
    con las siguientes reglas, ya que la función itera a través de cada cromosoma en la población
    y verifica si se debe aplicar una mutación. Si un número aleatorio generado al azar es menor 
    o igual a la tasa de mutación (mutation_rate), se realiza la mutación. Se crea una copia del 
    cromosoma original y se cambia un nodo aleatorio en el cromosoma por otro nodo elegido al azar 
    del grafo, el cromosoma mutado se agrega a una lista de cromosomas mutados, que se devuelve al 
    final de la función."""
    
def mutate_population(population, mutation_rate, graph):
    mutated_population = []
    for chromosome in population:
        mutated_chromosome = list(chromosome)
        for i in range(len(chromosome)):
            if random.random() < mutation_rate:
                mutated_chromosome[i] = random.choice(list(graph.keys()))
        mutated_population.append(mutated_chromosome)
    return mutated_population

#Función de main para realizar el algoritmo de Genetic Algorithm
"""Esta función lo que hace es que llama a la función de genetic_algorithm para poder realizar
    el algoritmo de Genetic Algorithm, esta función lo que hace es que recibe los parámetros
    de la función de genetic_algorithm y los imprime en pantalla para poder ver el resultado
    de la solución al problema"""

population_size = len(tree.keys())
num_generations = 1000
mutation_rate = 0.01
best_chromosome = genetic_algorithm(bidireccional_tree, population_size, num_generations, mutation_rate)
print('Best chromosome:', best_chromosome)
print('Fitness:', fitness_function(best_chromosome, bidireccional_tree))

