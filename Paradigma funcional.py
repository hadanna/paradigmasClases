# List normal
Lista3 = []
for numero in range(1,11):
    Lista3.append(numero**2)
print(Lista3)

# Python LIST COMPREHENSION
Lista4 = [numero**2 for numero in range(1,11)]
print(Lista4)

# List normal
Lista1 = []
for numero in range(1, 11):
    if numero % 2 == 0:
        Lista1.append(numero)
print(Lista1)

# Python List Comprehension
Lista2 = [numero for numero in range(1,11) if numero %2 ==0]
print(Lista2)

# Funciones Lambda
def doblas(num):
    return num*2

# LAMBDA (Funciones anónimas)
# lambda var1:return
# lambda num:num*2

#invocar
doblar = lambda num: num*2
doblar(2)

#------------------------------------------------------------
' filter() filtra '
' map() transforma '
# Funciones que se usan con lambda filter() y map()
def multiple(numero): #primero declaramos la funcion
    if numero % 5 == 0: #comprobamos que sea multiplo de cinco
        return True
numeros = [10, 33, 60, 100]

resultado = list(filter(multiple, numeros)) #filter(funcion, parametro) lo casteo a lista
print(resultado)

# con lambda
# filter: nos permite filtrar un iterable bajo una condición (Lista, diccionario, objetos)
resultado1 = list(filter(lambda numero: numero % 5 == 0, numeros))
print(resultado1)

def doble(numero1): #primero declaramos la funcion
    return numero1**2

numeros1 = [10, 33, 60, 100]

print(list(map(doble, numeros1))) #map(funcion, parametro) lo casteo a lista

# con lambda
# map: nos permite filtrar un iterable bajo una condición (Lista, diccionario, objetos)
resultado2 = list(map(lambda numero1: numero1**2, numeros1))
print(resultado2)
