# List Comprehension
'''
Estructura de datos propia de python:

Listas avanzadas en 1 linea de código.
lista1 = [<expresion> for elemento in <coleccion o string>]

'''
# Ejemplo1
'''
lista1 = []
for numero in range(0, 11):
    lista1.append(numero**2)
print(lista1)
'''
'''
lista2 = [numero**2 for numero in range(0, 11)]
print(lista2)
'''
# Ejemplo2
'''
lista3 = []
for numero in range(0, 11):
    if numero % 2 == 0:
        lista3.append(numero)
print(lista3)
'''
'''
lista4 = [numero for numero in range(0, 11) if numero % 2 == 0]
print(lista4)
'''
# ----------------------------------------------------------
# Lambda (funciones anónimas)
'''
def doblar(num):
    resultado = num * 2
    return resultado

print(doblar(2))
'''
# Mas reducida
'''
def doblar(num):
    return num*2
'''
# Lambda
'''
doblar = lambda num: num*2
print(doblar(2))
'''

# Funciones Filter y Map hacen uso de las Lambdas (Paradigma funcional)

# Filter: filtrar un iterable segun la condicion y 
# nos devuelve una nueva coleccion.
# Sintaxis: filter(<lambda <parametro>: <expresion condicional>(primer parámeto de fiter, lambda)>, <list, String, un iterable...(segundo parametro de filter)>)

'''
def multiple(numero):
    if numero%5 == 0:
        return True

numeros = [2,5,10,23,40,33]
lista1 = filter(multiple, numeros)
#list(filter(multiple, numeros))

for i in lista1:
    print(i)
'''
'''
numeros = [2,5,10,23,40,33]
print(list(filter(lambda numero: numero%5 == 0, numeros)))
'''

# Map: funcion que nos ayuda a iterar sobre un iterable y transformar sus valores
'''
def doblar(numero):
    return numero * 2

numeros = [2,5,10,23,50,33]

lista1 = list(map(doblar, numeros))
print(lista1)
'''
'''
numeros = [2,5,10,23,50,33]
print(list(map(lambda x: x*2, numeros)))
'''
# Recursividad:
# Funciones que se llaman a si misma n cantidad de veces
'''Factorial de un número'''
# El factorial de 0 es 1 (0! = 1)
# El factorial de un número n! = n *(n-1)! *

def factorial(numero):
    #Fin de la recursividad: if
    if numero == 0:
        return 1
    else:
        '''
        print(f"soy el {numero}")
        recur = factorial(numero - 1)
        da = recur * numero
        return da
        '''
        return factorial(numero -1) * numero

print(factorial(5))

# Calculo de fibonacci
'''
0 = 1
1 = 1
n = n-1 + (n - 2)
'''

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)