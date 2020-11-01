
# guarda en un archivo los puntajes
def guardar_puntaje(nombre_archivo, puntajes):
    with open(nombre_archivo, 'w') as f:
        # es lo mismo que decir f = open(nombre_archivo, 'w')
        
        # por cada nombre, puntaje y tiempo en la tupla
        for nombre, puntaje, tiempo in puntajes:
            # escribime en el archivo con el siguiente formato
            f.write("{}, {}, {}\n".format(nombre, puntaje, tiempo))

# Recupera los puntajes del archivo y
# devuelve lista con los puntajes
def recuperar_puntajes(nombre_archivo):
    # creamos una lista vacía
    puntajes=[]
    
    # Abre el archivo en modo lectura
    with open(nombre_archivo, 'r') as f:
        
        # por cada una de las lineas
        for linea in f:
            nombre, puntaje, tiempo = linea.rstrip("\n").split(',')
            # rstrip("\n") --> borro "\n" de la ultima posicion a la hora de guardar en la tupla
            puntajes.append((nombre, int(puntaje), tiempo))
    return puntajes

def agregar_puntajes(nombre_archivo, puntajes):
    with open(nombre_archivo, 'a') as f:
        # es lo mismo que decir f = open(nombre_archivo, 'a')
        
        # por cada nombre, puntaje y tiempo en la tupla
        for nombre, puntaje, tiempo in puntajes:
            # escribime en el archivo con el siguiente formato
            f.write("{}, {}, {}\n".format(nombre, puntaje, tiempo))
            
