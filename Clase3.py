# Eficacia vs. Eficiencia: REsolver el problema de la mejor manera
'''
Independiente del hardware
Independiente del lenguaje informático
Independiente a los factores externos del algoritmo
'''
# Fórmula Gauss
'''
import time

def sumaLineal(cant):
    suma = 0
    for numero in range(1, cant+1):
        suma += numero
    return suma

def sumaContinua(cant):
    return (cant/2) * (cant + 1)

cantidad = 100000

for i in range(4):
    t_0 = time.time()
    
    suma1 = sumaLineal(cantidad)
    
    t_1 = time.time()
    
    suma2 = sumaContinua(cantidad)
    
    t_2 = time.time()
    
    print(f"{suma1}, {t_1 - t_0}")
    print(f"{suma2}, {t_2 - t_1}")
    
    cantidad *= 10
'''
# No es confiable usar el tiempo reloj como medida del tiempo de ejecucion

# Medicion de algoritmo: "Orden de complejidad" "Notacion asintótica" "O Grande"
# A mayor cantidad de datos el numero de operaciones puede crecer
# Cuanto tiempo tarda o cuantos recursos consume. (tiempo de ejecución)
# Notacion asintótica: determinar tiempo de ejecucion de los algoritmos o para comparar entre dos o mas algoritmos.

# TIPOS DE COMPLEJIDAD
'''
O Gande (Big O) --> Omicron ---> El peor de los casos
Omega Grande ---> El mejor de los casos
Theta Grande ---> El caso promedio
'''
# Siempre se va a buscar el peor de los casos para saber como se comporta nuestro algoritmo en un escenario caótico.

#*****   BUSQUEDA LINEAL   *****
'''
listado = [23,5,78,9,45,33,98,34,45,67]

el mejor de los casos seria 1 vez
el promedio 6
el peor 10 (para los ciclos será el largo del iterable)
'''
'''
dato_buscar = (9)

def buscador(numeros, encontrar):
    for i in numeros:
        if i == encontrar:
            return True
    return False

if buscador(listado, dato_buscar) == True:
    print("Dato Encontrado")
else:
    print("Dato no encontrado")
'''
'''
import time

def sumaLineal(cant):
    suma = 0
    for numero in range(1, cant+1):
        suma += numero
    return suma
    # Los ciclos se leen como n cantidad de veces.
    # por cada ciclo hace otra operacion (suma)
    # Operaciones: asignacion + n*2 (ciclo + suma) =>
    # 1 + 2n => nos quedamos con el de mayor valor => 2n
    # El orden de complejidad es 0(n) lineal
    # n = cantidad de datos.

def sumaContinua(cant):
    return (cant/2) * (cant + 1)
    # Tenemos tres operaciones.
    # Orden de complejidad de esta funcion: O(1) Continua
    # 1 = cantidad de operaciones "constante"

cantidad = 100000

for i in range(4):
    t_0 = time.time()
    suma1 = sumaLineal(cantidad)
    t_1 = time.time()
    suma2 = sumaContinua(cantidad)
    t_2 = time.time()
    
    print(f"{suma1}, {t_1 - t_0}")
    print(f"{suma2}, {t_2 - t_1}")
    
    cantidad *= 10
'''
'''
def suma_dos(lista, valor):
    pares = [] #constante
    for i in lista: #n ->          n * n = n2
        for j in lista: #n ->
            if i + j == valor:
                pares.append([i, j]) #constante O(1)
    return pares

# Complejidad = O(n2)

cantidad = [12, 23, 41, 36, 28, 54, 35, 46, 52, 19, 27]
numero = 74
print(suma_dos(cantidad, numero))
'''
'''
# Ejercicio 3:
# Crear un programa que imprima por pantalla todos los numeros del 0 al 100 que sean divisibles por 3.
def excersice3():
    for number in range(0, 100): # n
        if number % 3 == 0: # 1
            print(number)

# Complejidad O grande es de O(n)
excersice3()
'''