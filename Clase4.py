# Una empresa de autopista tiene unas camaras de seguridad
# en el peaje que cuentan el numero de vehiculos que pasan,
# y unas gomas en el piso que cuentan el numero de ruedas de esos
# vehiculos.

# Se pide elaborar un algoritmo que a partir del número de vehiculos
# y el numero de ruedas extraiga la cantidad de coches y motos que
# pasan por allí.

'''
# O(n2) cuadratica
def cochesYmotosN2(vehiculos, ruedas):
    for coche in range(vehiculos + 1): # N
        for moto in range(vehiculos + 1): # N
            print(f"cantidad coches {coche} y motos {moto} y de vehiculos {vehiculos}")

            if ((coche + moto == vehiculos) and (coche * 4 + moto * 2 == ruedas)):
                return coche, moto

print(cochesYmotosN2(20, 80))
'''
'''
# O(n) lineal
def cochesYmotosLineal(vehiculos, ruedas):
    for coche in range(vehiculos + 1): # N
        moto = vehiculos - coche
        print(f"cantidad coches {coche} y motos {moto} y de vehiculos { vehiculos}")

        if ((coche + moto == vehiculos) and (coche * 4 + moto * 2 == ruedas)):
            print(f"{coche * 4} + {moto*2} = {ruedas}")
            return coche, moto

print(cochesYmotosLineal(30, 80));
'''
'''
# O(1) constante
def cochesYmotos(vehiculos, ruedas):
    coche = ruedas/2 - vehiculos #1
    # 4   =    10    -     6
    moto = vehiculos - coche #1
    # 2  =     6     -   4
    
    print(f"cantidad coches {coche} y motos {moto} y de vehiculos { vehiculos}")

    if (int(coche) + int(moto) == vehiculos): #1
        print(f"{int(coche) * 4} + {int(moto)*2} = {ruedas}")
        return int(coche), int(moto)

print(cochesYmotos(6, 20))
'''


  


'''
def cochesYmotosN2(vehiculos, ruedas):
    for coche in range(vehiculos + 1): # N
        for moto in range(vehiculos + 1): # N
            #print(f"Cant. coches {coche} = ruedas: {coche*4} + cant. de motos = ruedas: {moto*2}. Ruedas totales: {coche*4 + moto*2}")

            if ((coche + moto == vehiculos) and (coche * 4 + moto * 2 == ruedas)):
                return coche, moto

print(cochesYmotosN2(6, 20))
'''

'''
# Ordenamiento de listas
# Por selección:
# 1) Busca el mas grande y lo lleva al final de la lista.
# 2) Busca el más grande entre la primera y la anteultima posicion y lo lleva a la anteultima posicion.

def ord_seleccion(lista):

# Ordena una lista de elementos según el método de selección.
# Pre: los elementos de la lista deben ser comparables.
# Post: la lista está ordenada.

# posición final del segmento a tratar
    pos_final = len(lista) - 1
    
# mientras haya al menos 2 elementos para ordenar
    while pos_final > 0:
    # posición del mayor valor del segmento
        pos_max = buscar_max(lista, 0, pos_final)

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento

        lista[pos_max], lista[pos_final] = lista[pos_final], lista[pos_max]
        
        print("DEBUG: ", pos_max, pos_final, lista)

        # reducir el segmento en 1
        pos_final = pos_final - 1

def buscar_max(lista, inicio, fin):
    # Devuelve la posición del máximo elemento en un segmento de lista de elementos comparables.
    # La lista no debe ser vacía. a y b son las posiciones inicial y final del segmento

    pos_max = inicio
    for i in range(inicio + 1, fin + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

lista1 = [3,5,6,7,1,2,9]
print(ord_seleccion(lista1))

# Ordenar N numero insume N2 (N cuadrática) tiempo.

'''
# Ordenamiento por insercion:
# Compara el segundo con el primero. Si posicion 0 es mayor que el de posicion 1. Si es así se intercambian.
# Compara el 2 y lo ordena respecto del 1 y que el 0.
# Ordena el 3 respecto del 2, 1 y 0.

listaEntrada = [3,5,6,7,1,2,9]

def reubicar(lista, posicion):
    valorPosicion = lista[posicion]
    posOriginal = posicion
    
    while posOriginal > 0 and valorPosicion < lista[posOriginal-1]:
        lista[posOriginal] = lista[posOriginal - 1]
        posOriginal -= 1
    lista[posOriginal] = valorPosicion

# listaEntrada-1: recorro las posiciones
for i in range(len(listaEntrada)-1):
    if listaEntrada[i+1]<listaEntrada[i]:
        reubicar(listaEntrada, i+1)
    print("DEBUG: ", listaEntrada)