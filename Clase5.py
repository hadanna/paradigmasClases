# Ordenamientos recursivos
# Merge sort: si la lista tiene un tamaño menor a dos, ya está ordenada.
# Sino se divide la lista a la mitad, si es numero impar la divide en dos lo mas parecidos posible
# Se divide nuevamente cada una de las lista resultantes hasta que solo queden partes de un solo elemento caada una.
# Se ordena cada sublista y luego de hace un merge de la listas ordenadas dede adentro hacia afuera

'''
# El mergesort tiene un orden de complejidada de Log2 N, es más pequeño que un N.

listaDesordenada = [6, 7, -1, 0, 5, 2, 3, 8, 9]
def merge_sort(lista):
    if len(lista) <= 1:
        return lista     
    else:
        medio = len(lista)//2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        #print(f"medio: {medio}")
        #print(f"izq: {lista[:medio]}")
        #print(f"der: {lista[medio:]}")
        return merge(izq, der)

def merge(lista1, lista2):
    i = 0
    j = 0
    listaSalida = []
    while (i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            listaSalida.append(lista1[i])
            i += 1
        else:
            listaSalida.append(lista2[j])
            j += 1
    listaSalida += lista1[i:]
    listaSalida += lista2[j:]
    print(f"listaSalida {listaSalida}")
    return listaSalida

print(merge_sort(listaDesordenada))

# Recursion: entra hasta lo mas que puede y luego sale y ejecuta.
'''

# Quick Sort: más eficiente. Tiene dos variantes. Si tiene un solo elemento, ya está ordenado.
# Si tiene mas elementos, toma un elemento (pivote) y arma tres listas.
# lista 1: elementos menore al pivote.
# lista 2: pivote solo.
# lista 3: numero mayores o iguales al pivote.
# Ordena cada sublista y las concatena.

'''
listaEntrada = [7, 5, 3, 12, 9, 2, 10, 4, 15, 8]

def quickSort(lista):
    if len(lista) <= 1:
        return lista
    else:
        l_menores, l_pivote, l_mayores = divide(lista)
        print(f"pivote: {l_pivote}")
        print(f"menores: {l_menores}")
        print(f"mayores: {l_mayores}")
    return quickSort(l_menores) + l_pivote + quickSort(l_mayores)

def divide(lista):
    l_menores = []
    l_mayores = []
    l_pivote = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < l_pivote:
            l_menores.append(lista[i])
        elif lista[i] >= l_pivote:
            l_mayores.append(lista[i])
    return l_menores, [l_pivote], l_mayores

print(quickSort(listaEntrada))

# Es menos eficiente cuando la lista esta ordenada o parcialmente ordenada, menos eficiente que un mergesort.
# Tiene un costo de Log2 N en el mejor de los casos.
# En el peor de los casos tiene un orden de complejidad de N.
# Listas auxiliares: problema de memoria.
'''

listaEntrada = [7, 5, 3, 12, 9, 2, 10, 4, 15, 8]

# Quicksort mejorada o de Hoare.
def quick_sort(lista):
    '''Ordena la lista de forma recursiva.
    Pre: los elementos de la lista deben ser comparables.
    Post: la lista está ordenada.'''
    _quick_sort(lista, 0, len(lista) - 1)
    return lista

def _quick_sort(lista, inicio, fin):
    '''Función quick_sort recursiva.
    Pre: los índices inicio y fin indican sobre qué porción operar.
    Post: la lista está ordenada.'''
    if inicio >= fin:
        return
    menores = _partition(lista, inicio, fin)
    _quick_sort(lista, inicio, menores - 1)
    _quick_sort(lista, menores + 1, fin)

def _partition(lista, inicio, fin):
    '''Función partición que trabaja sobre la misma lista.
    Pre: los índices inicio y fin indican sobre qué porción operar.
    Post: los menores están antes que el pivote, los mayores después.
    Devuelve: la posición en la que quedó ubicado el pivote.'''
    pivote = lista[inicio]
    menores = inicio

    # Ubicar menores a la izquierda, mayores a la derecha
    for i in range(inicio + 1, fin + 1):
        if lista[i] < pivote:
            menores += 1
            if i != menores:
                # Intercambio los elementos
                _swap(lista, i, menores)
    # Ubicar el pivote al final de los menores
    if inicio != menores:
        _swap(lista, inicio, menores)
    return menores

def _swap(lista, i, j):
    '''Intercambia los elementos i y j de lista.'''
    lista[j], lista[i] = lista[i], lista[j]

print(quick_sort(listaEntrada))

# Los ordenamientos por seleccion e insercion son 
# ordenamientos sencillos pero costosos en cantidad 
# de intercambios o de comparaciones. Pero es posible
# conseguir ordenamientos con mejor orden utilizando algoritmos
# recursivos.

# MERGE SORT consiste en dividir la lista a ordenar
# hasta que tenga 1 o 0 elementos y luego combinar la lista
# de forma ordenada. N log N.
# Desventaja: siempre usa el doble de la memoria requerida
# por la lista a ordenar.

# QUICK SORT consiste en elegir un elemento, pivote y ordenar
# los elementos menores a la izquierda y los mayores a la
# derecha. Luego ordenar cada sublista de la misma forma.
# No requiere mas memoria ya que trabaja sobre la misma
# lista.
# Desventaja: promedio N log N. Peor caso: N2.