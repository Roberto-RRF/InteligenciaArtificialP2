import csv
import time
import sys
sys.path.append('./recursos')

# Importamos la funcion greedy_best_first_search
from greedy_best_first_search import greedy_best_first_search

def generate_states():
    # Abrimos el archivo csv y guardamos cada fila en una lista
    with open('pesos.csv', 'r') as f:
        reader = csv.reader(f)
        lista = list(reader)

    for i in range(len(lista)):
      for j in range(len(lista[0])):
        lista[i][j] = int(lista[i][j])
    
    nodes_tuples = {}
    available_nodes_names = ['acapulco','acayucan', 'agua prieta', 'aguascalientes', 'alvarado', 'atlacomulco', 'cabo san lucas', 'campeche', 'cancun', 'chetumal', 'chihuahua', 'chilpancingo', 'ciudad altamirano', 'ciudad de mexico', 'ciudad del carmen', 'ciudad obregon', 'ciudad victoria', 'colima', 'cordoba', 'cuernavaca', 'culiacan', 'durango', 'ensenada', 'felipe carrillo puerto', 'francisco escarcega', 'guadalajara', 'guanajuato', 'guaymas', 'hermosillo', 'hidalgo del parral', 'iguala', 'izucar de matamoros', 'janos', 'juarez', 'la paz', 'manzanillo', 'matamoros', 'mazatlan', 'merida', 'mexicalli', 'monclova', 'monterrey', 'morelia', 'nuevo laredo', 'oaxaca', 'ojinaga', 'pachuca de soto', 'piedras negras', 'pinotepa nacional', 'playa azul', 'puebla', 'puerto angel', 'queretaro', 'reynosa', 'salamanca', 'san felipe', 'san luis potosi', 'san quintin', 'santa ana', 'santa rosalia', 'santo domingo', 'soto la marina', 'tampico', 'tehuacan', 'tehuantepec', 'tepic', 'tijuana', 'tlaxcala', 'toluca de lerdo', 'topolobampo', 'torreon', 'tuxpan de rodriguez cano', 'tuxtla', 'valladolid', 'veracruz', 'villa hermosa', 'zacatecas', 'zihuatanejo']

    for i in available_nodes_names:
        nodes_tuples[i] = []
    
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j] != 0:
              nodes_tuples[available_nodes_names[i]].append((available_nodes_names[j],lista[i][j]))
    
    return nodes_tuples

 
tree = generate_states()
# print(tree)

result = greedy_best_first_search(tree, "cancun", "la paz")
print (result)