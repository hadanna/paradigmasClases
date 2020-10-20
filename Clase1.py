#Ejercicio 1
# Crear un programa que imprima por pantalla el mensaje “Hello World!”.
'''var = "Hello World"
print(var)'''
# Nota: se puede imprimir el dato puro o el dato almacenado en una variable, siempre es una buena práctica usar variables.

# Ejercicio 2
# Crear un programa que imprima por pantalla todos los números pares del 0 al 100
'''
for number in range(0, 101):
    if number %2 == 0:
        print(number)
'''
# Ejercicio 3
# Crear un programa que imprima por pantalla todos los números del 0 al 100 que sean divisibles por 3.
'''
def exercise3():
    for number in range(0, 101):
        if number % 3 == 0:
            print(number)
exercise3()
'''
# Ejercicio 4
# Crear un programa que pida al usuario que ingrese dos números y luego el programa imprima por pantalla:
# en un renglón la suma de ellos, en otro la resta y en otro el producto.
'''
def calculo(num1, num2):
    print("Suma", num1 + num2)
    print("Resta", num1 - num2)
    print("Producto", num1 * num2)

calculo(int(input("Ingrese num1: ")), int(input("Ingrese num2: ")))
'''
# Ejercicio 5
# Crear un programa que pida al usuario 10 números enteros, los almacene en una lista,
# ordene los números dentro de la lista y luego imprima por pantalla la lista completa y ordenada.
'''
def excercise5():
    userValueList = [] # 1 (constante)
    for number in range(10): # n (variable)
        userValue = int(input("Ingrese un numero entero")) # 1 (constante)
        userValueList.append(userValue) # 1 (constante)

    userValueList.sort() # n log n
    print(userValueList)

excercise5()

# O = O(n log n)
'''
# Ejercicio 6
#
# Crear un programa que le pida al usuario dos números enteros y luego: si el primero es mayor que el segundo,
# retorne 1, si el primero es menor que el segundo retorne -1 y si ambos números son iguales retorne 0.
'''
def excercise6(number1, number2):
    if number1 > number2:
        return 1
    elif number1 == number2:
        return 0
    else:
        return -1

userInput1 = int(input("Ingrese un numero entero "))
userInput2 = int(input("Ingrese un numero entero "))

resultado = excercise6(userInput1, userInput2)
print(resultado)
'''
# Ejercicio 7
# Crear un programa que le pida al usuario ingresar dos números enteros y devuelva el punto medio entre ellos.
'''
def puntoMedio(num1, num2):
    punto = (num1 + num2)/2
    print(punto)

puntoMedio(int(input("Ingrese num1: ")), int(input("ingrese num2: ")))
'''
# Ejercicio 8
# Crear un programa que tome una lista de números enteros y devuelva dos listas ordenadas.
# La primera con los números pares y la segunda con los números impares.
'''
def separar(lista):
    pares = []
    impares = []
    for item in lista:
        if item%2 == 0:
            pares.append(item)
        else:
            impares.append(item)
    return "pares", pares, "impares", impares
lista1 = [1,2,3,4,5,6,7,8,9,10]
print(separar(lista1))
'''

# Ejercicio 9
# Crear un programa que solicite al usuario que ingrese su dirección mail.
# Imprimir un mensaje indicando si la dirección es válida o no.
# Una dirección se considerará válida si contiene el símbolo "@".
'''
def ingress(email):
    if email.find('@') != -1:
        print("El email es válido")
    else:
        print("el email no es válido")
ingress(input("Ingrese e-mail: "))
'''
# Ejercicio 10
# Crear un programa que dado un número de DNI, retorne True si el número es válido y False si no lo es.
# Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
'''
def dniValid(dni):
    if len(dni) >= 7 and len(dni) <= 8:
        return True
    else:
        return False

print(dniValid(input("Ingrese su DNI: ")))
'''
# Ejercicio 11
# Crear un programa que, dado un string, retorne la longitud de la última palabra.
# Se considera que las palabras están separadas por uno o más espacios.
# También podría haber espacios al principio o al final del string pasado por parámetro.
'''
def excercise11(userInput):
    wordList = userInput.split()
    # ultimaPalabra = wordList[-1]
    # longitud = len(ultimaPalabra)
    # return longitud

    return len(wordList[-1])

result = excercise11("Bienvenidos a paradigmas de programación")
print(result)
'''

# Ejercicio 12
# En McDonald’s se pueden comprar patitas de pollo en 6, 9 o 20 unidades.
# Crear un programa que, a partir de un número, decida si es posible comprar esa cantidad de patitas.
'''
def valid(num1):
    if num1 == "6" or num1 == "9" or num1 == "20":
        return True
    else:
        return False
print(valid(input("Ingrese una cantidad: ")))
'''