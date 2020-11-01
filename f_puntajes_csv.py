import csv

# guarda en un archivo los puntajes
def guardar_puntaje_csv(nombre_archivo, puntajes):
    with open(nombre_archivo, "w", newline='') as f:
        # newine remueve la linea nueva extra
        # es lo mismo que decir f = open(nombre_archivo, 'w')
        
        # intanciamos un objeto csv y le pasamos por parametro la varible con el nombre de archivo recibido
        archivo_csv = csv.writer(f)
        
        # escribe los puntajes en el archivo csv
        archivo_csv.writerows(puntajes)
        # no hace falta que hagamos ningun loop
        
# Recupera los puntajes del archivo y
# devuelve lista con los puntajes
def recuperar_puntajes_csv(nombre_archivo):
    # creamos una lista vacía
    puntajes=[]
    
    # Abre el archivo en modo lectura
    with open(nombre_archivo, "r") as f:
        archivo_csv = csv.reader(f)
        list_rows = list(archivo_csv)
        return list_rows

def recuperar_puntajes_csv1(nombre_archivo):
    # creamos una lista vacía
    puntajes=[]
    
    # Abre el archivo en modo lectura
    with open(nombre_archivo, "r") as f:
        archivo_csv = csv.reader(f)
        for nombre, puntaje, tiempo in archivo_csv:
            puntajes.append((nombre, puntaje, tiempo))
        return puntajes
