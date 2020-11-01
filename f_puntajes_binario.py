import pickle

# guarda en un archivo los puntajes
def guardar_puntaje_binary(nombre_archivo, puntajes):
    with open(nombre_archivo, "wb") as f:
    # es lo mismo que decir f = open(nombre_archivo, 'wb')
        
        # los archivos binarios trabajan con bytes
        # llamamos metodo dump del modulo pickle
        # le pasamos los datos y el archivo donde los guardaremos
        pickle.dump(puntajes, f)
        
# Recupera los puntajes del archivo y
# devuelve lista con los puntajes
def recuperar_puntajes_binary(nombre_archivo):
    # NO creamos una lista vacía
    # NO hay que hacer ningun ciclo
    with open(nombre_archivo, "rb") as f:
        return pickle.load(f)

# IMPORTANTE: el archivo binario guarda un tipo de codificacion que no entendemos
# Usando pickle podemos recuperar datos de un binario en idioma humano
