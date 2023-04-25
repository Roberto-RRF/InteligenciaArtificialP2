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
Este algoritmo genera el árbol de búsqueda

Ejecucion del programa
        Opcion 1) Solo mandalo a ajecutar
    
    Entradas:
        1) No requiere entradas
    
    Salidas:
        1) Genera tanto un árbol de búsqueda normal como uno unidireccional
"""
#Dependencias
#CSV libreria para leer archivos de tipo csv
import csv
#pandas es utilizada para crear dataframes con informacion del archivo csv
import pandas as pds

#Responsable: Sebastian Ruiz
def generate_states():

    # Abrimos el archivo csv y guardamos cada fila en una lista
    with open('../pesos.csv', 'r') as f:
        reader = csv.reader(f)
        lista = list(reader)

    # Convertimos los valores a enteros 
    for i in range(len(lista)):
       for j in range(len(lista[0])):
         lista[i][j] = int(lista[i][j])

    # Para convertir el arbol direccional en bidireccional sumamos la matriz con su transpuesta, al ser una matriz simetrica la suma de ambas es igual a la matriz bidireccional
    matris = pds.DataFrame(lista)
    matris_t = matris.T
    matris_bidireccional = matris + matris_t
    

    # Convertimos la matriz bidireccional y direccionada a un diccionario    
    bidireccional_tree = {}
    direccional_tree = {}
    available_nodes_names = ['ACAPULCO', 'ACAYUCAN', 'AGUA PRIETA', 'AGUASCALIENTES', 'ALVARADO', 'ATLACOMULCO', 'CABO SAN LUCAS', 'CAMPECHE', 'CANCUN', 'CHETUMAL', 'CHIHUAHUA', 'CHILPANCINGO', 'CIUDAD ALTAMIRANO', 'CIUDAD DE MEXICO', 'CIUDAD DEL CARMEN', 'CIUDAD OBREGON', 'CIUDAD VICTORIA', 'COLIMA', 'CORDOBA', 'CUERNAVACA', 'CULIACAN', 'DURANGO', 'ENSENADA', 'FELIPE CARRILLO PUERTO', 'FRANCISCO ESCARCEGA', 'GUADALAJARA', 'GUANAJUATO', 'GUAYMAS', 'HERMOSILLO', 'HIDALGO DEL PARRAL', 'IGUALA', 'IZUCAR DE MATAMOROS', 'JANOS', 'JUAREZ', 'LA PAZ', 'MANZANILLO', 'MATAMOROS', 'MAZATLAN', 'MERIDA', 'MEXICALI', 'MONCLOVA', 'MONTERREY', 'MORELIA', 'NUEVO LAREDO', 'OAXACA', 'OJINAGA', 'PACHUCA DE SOTO', 'PIEDRAS NEGRAS', 'PINOTEPA NACIONAL', 'PLAYA AZUL', 'PUEBLA', 'PUERTO ANGEL', 'QUERETARO', 'REYNOSA', 'SALAMANCA', 'SAN FELIPE', 'SAN LUIS POTOSI', 'SAN QUINTIN', 'SANTA ANA', 'SANTA ROSALIA', 'SANTO DOMINGO', 'SOTO LA MARINA', 'TAMPICO', 'TEHUACAN', 'TEHUANTEPEC', 'TEPIC', 'TIJUANA', 'TLAXCALA', 'TOLUCA DE LERDO', 'TOPOLOBAMPO', 'TORREON', 'TUXPAN DE RODRIGUEZ CANO', 'TUXTLA', 'VALLADOLID', 'VERACRUZ', 'VILLAHERMOSA', 'ZACATECAS', 'ZIHUATANEJO']

    for i in available_nodes_names:
        bidireccional_tree[i] = []
        direccional_tree[i] = []
    
    for i in range(len(matris_bidireccional)):
        for j in range(len(matris_bidireccional[i])):
            if matris_bidireccional[i][j] != 0:
              bidireccional_tree[available_nodes_names[i]].append((available_nodes_names[j],matris_bidireccional[i][j]))
            if lista[i][j] != 0:
              direccional_tree[available_nodes_names[i]].append((available_nodes_names[j],lista[i][j]))


    return bidireccional_tree, direccional_tree