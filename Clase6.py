'''
Ejercicio 20.7.1. Escribir una función merge_sort_3 que funcione igual que el merge sort pero
en lugar de dividir los valores en dos partes iguales, los divida en tres (asumir que se cuenta
con la función merge(lista_1, lista_2, lista_3)). ¿Cómo te parece que se va a comportar
este método con respecto al merge sort original?
'''
'''
def merge_sort(lista):
    if len(lista) <= 2:
        return lista
    medio = len(lista) // 3
    izq = merge_sort(lista[:medio])
    print("izq", izq)
    med = merge_sort(lista[medio: (medio * 2)])
    print("med", med)
    der = merge_sort(lista[(medio * 2):])
    print("der", der)
    return merge(izq, med, der)

def merge(lista1, lista2, lista3):
    print("DEBUG", "lista1", lista1, "lista2", lista2, "lista3", lista3)
    i, j, k= 0, 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2) and k < len(lista3)):
        if (lista1[i] < lista2[j]) and (lista1[i] < lista3[k]):
            resultado.append(lista1[i])
            i += 1
        elif (lista2[j] < lista1[i]) and (lista2[j] < lista3[k]):
            resultado.append(lista2[j])
            j += 1
        elif (lista3[k] < lista1[i]) and (lista3[k] < lista2[j]):
            resultado.append(lista3[k])
            k += 1

    print("queda", resultado)
    resultado += lista1[i:]
    print("despues de agregar al resto I ", resultado)

    resultado += lista2[j:]
    print("despues de agregar al resto J", resultado)
    
    resultado += lista3[k:]
    print("despues de agregar al resto K", resultado)

    return resultado

print(merge_sort([6,7,-1,0,5,2,3,8,1]))
'''
'''
Ejercicio 20.7.2. Mostrar los pasos del ordenamiento de la lista: 6 0 3 2 5 7 4 1 con los métodos
de inserción y con merge sort. ¿Cuáles son las principales diferencias entre los métodos?
¿Cuál usarías en qué casos?
'''
'''
Ejercicio 20.7.3. Ordenar la lista 6 0 3 2 5 7 4 1 usando el método quicksort. Mostrar el árbol
de recursividad explicando las llamadas que se hacen en cada paso, y el orden en el que se
realizan.
'''

# Realizar un algoritmo para cortar una pizza en 8 porciones
# teniendo en cuenta que es  1 pizza. No puede ser pizza/8,
# y puede que necesite pasar alguna otra referencia. Luego
# realizar el algoritmo pero con recursividad.
'''
def cortar(pizza, original, porciones):
    for corte in range(porciones):
        pizza = pizza / 2
        if pizza == original/porciones:
            return pizza

print(cortar(1, 1, 8))
'''

# Ciclica
'''
def cortar(pizza, cortes, porciones):
    for corte in range(1, cortes):
        print("Cortes: ", corte)
        pizza = pizza / 2
    return pizza

print(cortar(1, 4, 8))
'''

# Recursiva
'''
from fractions import Fraction
def cortar(pizza, original, porciones):
    if pizza == original/porciones:
        return pizza
    return cortar(pizza / 2, original, porciones)
print(Fraction(cortar(1, 1, 8)))
'''

# Escribir un programa que pida una serie de numeros y luego
# imprima el cuadrado del mismo, utilizando comprehencion list.

#lista = [1,2,3,4,5,6,7,8,9]
'''
def cuadrado():
    lista = []
    n = int(input("Ingrese cant de numeros: "))
    for pos in range(n):
        lista.append(int(input("Ingrese numero: ")))
    return [i * i for i in lista]
print(cuadrado())
'''
'''
def cuadrados():
    lista = []
    n = int(input("Ingrese cant de numeros: "))
    for pos in range(n):
        lista.append(int(input("Ingrese numero: ")))
    return cuadrado(lista)

def cuadrado(lista):
    return [i * i for i in lista]

print(cuadrados())
'''

# Escribir una funcion que reciba un numero positivo n
# y devuelva la cantidad de digitos que tiene,
# utilizando recursividad.
'''
def digitos(n, contador):
    while n > 9:
        n = n // 10
        print("numero: ", n)
        return digitos(n, contador + 1)
    return contador
print(digitos(92, 1))
'''
# Dada una lista anidada, por ejemplo:
# [1, ['a', 'b', 'c'], 2, 3, ['c', 'd', 'e']]
# hacer un algoritmo que devuelva los elementos base
# en una lista y los de sublistas en otra. Deberá usar la
# función isinstance().
'''
lista =  [1, ['a', 'b', 'c'], 2, 3, ['c', 'd', 'e']]
base = []
sub = []
for i in lista:
    if isinstance(i, list) == False:
        base.append(i)
        print(f"{i} pertenece a la lista base.")
    elif isinstance(i, list) == True:
        print(f"{i} pertenece a la sublista.")
        sub.append(i)
print(f"Base: {base}")
print(f"Sublista: {sub}")
'''
'''
lista =  [1, ['a', 'b', 'c'], 2, 3, ['c', 'd', 'e']]
base = []
sub = []
for i in lista:
    if isinstance(i, list) == False:
        base.append(i)
        print(f"{i} pertenece a la lista base.")
    elif isinstance(i, list) == True:
        for elemento in i:
            print(f"{elemento} pertenece a la sublista.")
            sub.append(elemento)
print(f"Base: {base}")
print(f"Sublista: {sub}")
'''

# ------- Manejo de archivos ------- #

# Abrir archivos: open()
# Leer archivos: readline()
# Cerrar archivos: close()
'''archivo = open('I:archivo.txt')'''

# Lee la primera linea
# linea = archivo.readline()

# Imprime la primera linea y una linea vacía luego
# print(linea)

#while linea != '':
#    linea = archivo.readline()
#    print(linea)
'''
for linea in archivo:
    print(linea)
archivo.close()
'''

'''
# Lee todo el archivo y guarda en una lista cada una de las lineas
# (linea + \n o salto de linea)

lineas = archivo.readlines()
print(lineas)
'''

# Si cerramos el archivo y queremos leerlo nuevamente
# nos da un error de I/O operation on closed file.

# Una vez que ya lo leemos, si volvemos a leerlo
# el puntero va a estar al final del archivo y no tiene nada
# que leer.

# Cuando sale de la siguiente bloque, se cierra el archivo automaticamente.
# with open ("C:archivo.txt") as archivo:

'''
archivo =  open("C:archivo.txt")
i = 1

for linea in archivo:
    linea = linea.rstrip("\n")
    print("{}:{}".format(i, linea))
    i += 1
archivo.close()
'''

# con with open no hace falta que se cierre el archivo una vez ejecutado
'''with open("C:archivo.txt") as archivo:
    i = 1
    for linea in archivo:
        # Le sacamos el salto de linea
        linea = linea.rstrip("\n")
        
        # Le agregamos el numero de linea
        print("{}:{}".format(i, linea)) # Formato
        i += 1
'''

# para no tener que hacer un contador a mano, usamos la funcion: enumerate

'''with open("C:archivo.txt") as archivo:
    for i, linea in enumerate(archivo):
        linea = linea.rstrip("\n")
        print("{}: {}".format(i, linea))
'''
# ------ modo de apertura de archivos -------

# modo de lectura r (read): No se puede modificar, solo leer
# Este modo es por defecto

'''with open("C:archivo.txt") as archivo:
    i = 1
    for linea in archivo:
        linea = linea.rstrip("\n")
        print("{}:{}".format(i, linea))
        i += 1
'''
    # archivo.write("hola") # out: "not writable"

# modo solo escritura write (w):

# EN MODO ESCRITURA (w):
# cuando el archivo no existe automaticamente me crea uno en la ruta que le indico.
'''with open("H:archivos.txt", mode="w") as archivo:
    archivo.write("hola")
    archivo.write("chau")
'''
# modo escritura posicionandose al final del archivo
'''with open("H:archivos.txt", mode="a") as archivo:
    archivo.write("23\n")
    archivo.write("98\n")
'''
# con el símbolo '+' se pasa a un modo lectura escritura
# r+ != w+
# r+ --> sobreescribe y deja lo escrito anterior (lee y escribe)
# w+ --> sobreescribe los datos y borra lo anterior escrito (Escribe y lee)

# 'w', 'a', 'w+', 'a+' --> python crea el archivo si no esxiste

# Escritura en diferentes lineas: \n

lista_cadenas = ['2396', '5852', 'Camila']

'''
with open("H:archivos.txt", mode="a") as archivo:
    archivo.writelines(["Ana", "Laura"])
''' 
'''
with open("H:archivos.txt", mode="a") as archivo:
    archivo.writelines(lista_cadenas)
'''
