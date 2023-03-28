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
    available_nodes_names = ['ACAPULCO', 'ACAYUCAN', 'AGUA PRIETA', 'AGUASCALIENTES', 'ALVARADO', 'ATLACOMULCO', 'CABO SAN LUCAS', 'CAMPECHE', 'CANCUN', 'CHETUMAL', 'CHIHUAHUA', 'CHILPANCINGO', 'CIUDAD ALTAMIRANO', 'CIUDAD DE MEXICO', 'CIUDAD DEL CARMEN', 'CIUDAD OBREGON', 'CIUDAD VICTORIA', 'COLIMA', 'CORDOBA', 'CUERNAVACA', 'CULIACAN', 'DURANGO', 'ENSENADA', 'FELIPE CARRILLO PUERTO', 'FRANCISCO ESCARCEGA', 'GUADALAJARA', 'GUANAJUATO', 'GUAYMAS', 'HERMOSILLO', 'HIDALGO DEL PARRAL', 'IGUALA', 'IZUCAR DE MATAMOROS', 'JANOS', 'JUAREZ', 'LA PAZ', 'MANZANILLO', 'MATAMOROS', 'MAZATLAN', 'MERIDA', 'MEXICALI', 'MONCLOVA', 'MONTERREY', 'MORELIA', 'NUEVO LAREDO', 'OAXACA', 'OJINAGA', 'PACHUCA DE SOTO', 'PIEDRAS NEGRAS', 'PINOTEPA NACIONAL', 'PLAYA AZUL', 'PUEBLA', 'PUERTO ANGEL', 'QUERETARO', 'REYNOSA', 'SALAMANCA', 'SAN FELIPE', 'SAN LUIS POTOSI', 'SAN QUINTIN', 'SANTA ANA', 'SANTA ROSALIA', 'SANTO DOMINGO', 'SOTO LA MARINA', 'TAMPICO', 'TEHUACAN', 'TEHUANTEPEC', 'TEPIC', 'TIJUANA', 'TLAXCALA', 'TOLUCA DE LERDO', 'TOPOLOBAMPO', 'TORREON', 'TUXPAN DE RODRIGUEZ CANO', 'TUXTLA', 'VALLADOLID', 'VERACRUZ', 'VILLAHERMOSA', 'ZACATECAS', 'ZIHUATANEJO']

    for i in available_nodes_names:
        nodes_tuples[i] = []
    
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j] != 0:
              nodes_tuples[available_nodes_names[i]].append((available_nodes_names[j],lista[i][j]))
    
    return nodes_tuples

 
tree = generate_states()
# print(tree)

