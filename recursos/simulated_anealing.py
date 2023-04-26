from HaversineDistance import *
from generate_states import *
import random 

import math
import random

tree = generate_full_conected_tree()
print(tree)

# Definir la función de costo
def cost(origen, destino):
  return HaversineDistanceBetweenCitiesString(origen, destino)


         

      
      
     
    
  

# Definir la función para generar un vecino aleatorio
def generar_vecino(ciudad):
  vecinos = tree[ciudad]
  temp = []
  for i in vecinos:
    temp.append(i[0])
  #print(temp)
  vecino = random.sample(temp, len(temp))
  return vecino

# Definir el algoritmo de Simulado Recocido
def simulated_annealing(origen, destino):
  # Definir la temperatura inicial y final, y el factor de enfriamiento
  temperatura_inicial = 100
  temperatura_final = 0.1
  factor_enfriamiento = 0.99
  
  # Generar una solución inicial aleatoria
  solucion_actual = [origen]
  costo_actual = cost(origen, solucion_actual[0]) + cost(solucion_actual[-1], destino)
  for i in range(len(solucion_actual)-1):
    costo_actual += cost(solucion_actual[i], solucion_actual[i+1])
  
  # Bucle principal del algoritmo
  temperatura = temperatura_inicial
  while temperatura > temperatura_final:
    # Generar un vecino aleatorio
    vecino = generar_vecino(solucion_actual[0])
    costo_vecino = cost(origen, vecino[0]) + cost(vecino[-1], destino)
    for i in range(len(vecino)-1):
      costo_vecino += cost(vecino[i], vecino[i+1])
      
      # Calcular la diferencia de costos
      delta = costo_vecino - costo_actual
      
      # Si el vecino es mejor, aceptarlo automáticamente
      if delta < 0:
        #print('vecino mejor')
        #print(vecino)
        solucion_actual.append(vecino)
        costo_actual = costo_vecino
      # Si el vecino es peor, aceptarlo con una probabilidad dependiente de la temperatura
      else:
        probabilidad_aceptacion = math.exp(-delta/temperatura)
        if random.random() < probabilidad_aceptacion:
          #print('vecino mejor')
          #print(vecino)
          solucion_actual.append(vecino)
          costo_actual = costo_vecino
    
      # Enfriar la temperatura
      temperatura *= factor_enfriamiento
    return solucion_actual, costo_actual


