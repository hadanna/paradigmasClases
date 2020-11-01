# modulos creados por nosotros e importados
'''
from sumayresta import suma

print(suma(2,3))
'''

# ------------- archivos binarios ---------------#
'''
archivo_binario = open('c:/Users/GabrielPalavecino/Desktop/Belen/1.jpg', 'rb')
print(archivo_binario.tell()) 
# tell() nos da la posicion actual del cursor
# a penas abris un archivo, la posicion es 0

datos = archivo_binario.read(3) #cantidad de bytes que queremos que lea
print(datos)
print(type(datos)) # imprime el tipo de datos

# imprimo nuevamente la posicion del cursor
print(archivo_binario.tell())

# seek() modifica la posicion del cursor.
# le pasamos la posicion que queremos por parametro
archivo_binario.seek(0)

print(archivo_binario.tell())

# leemos toda la imagen
datos = archivo_binario.read()
# imprimir la longitud del archivo jpg
print(len(datos))
'''

# -------- Persistencia de datos --------- #
# juego que guarda puntajes en una lista de tuplas
# nombre_archivo --> archivo de texto
# puntajes --> los puntajes que se van a guardar

# f_puntajes tiene guardadas las funciones que usa este archivo
'''
import f_puntajes
datos = [("Ana", 344, 3), ("Elías", 766, 1)]

f_puntajes.guardar_puntaje("puntajes.txt", datos) # me crea el archivo en el escritorio, piso datos existentes
print(f_puntajes.recuperar_puntajes("puntajes.txt"))

datos_nuevos = [("Ariel", 455, 3), ("Gabriel", 877, 1)]

f_puntajes.agregar_puntajes("puntajes.txt", datos_nuevos) # arego datos nuevos al archivo
print(f_puntajes.recuperar_puntajes("puntajes.txt"))
'''
'''
tupla1 = (("Ana", 34, "8GS"), ("Gabriel", 92, "8FO"), ("Pedro", 82, "PK48"))
for nombre, numero, sigla in tupla1:
    print("{}, {}, {}".format(nombre, numero, sigla))
''' 
# FileNotFoundError: no existe el archivo o el directorio, etc

# Archivos SCV (separated comma values)
'''
No siempre son necesarios los encabezados
Son pequeñas bases de datos
'''
# Nombre, Apellido, Edad
# "Ana", "Orellana", 35
# "Gabriel", "Palavecino", 36
# "Maria", "Pacheco", 89
# "Ariel", "Cruzado", 17
# "Elias", "Cruzado", 15

import f_puntajes
import f_puntajes_csv
import f_puntajes_binario

datos = [("Ana", "344", "3"), ("Elias", "766", "1"), ("Alejandro", "7738", "9983"), ("Ariel", "887", "99182")]

'''
f_puntajes.guardar_puntaje("puntajes.csv", datos) # me crea el archivo en el escritorio, piso datos existentes
print(f_puntajes.recuperar_puntajes("puntajes.csv"))
'''

'''
f_puntajes_csv.guardar_puntaje_csv("puntajes.csv", datos) # me crea el archivo en el escritorio, piso datos existentes
print(f_puntajes_csv.recuperar_puntajes_csv1("puntajes.csv"))

f_puntajes_binario.guardar_puntaje_binary("puntajes.csv", datos)
print(f_puntajes_binario.recuperar_puntajes_binary("puntajes.csv"))
'''
# ------------------------ URL -----------------------------#

# Para evitar problemas ala hora de usar archivos en distintos sistemas operativos
# y poder buscarlos de forma generica sin cambiar la ruta del archivo a mano
# se utiliza el módulo OS

'''
import os

# le pasamos la carpeta y el nombre del archivo por parametro
ruta = os.path.join("data", "archivo.csv")

# luego abrimos el archivo
with open(ruta) as f:
'''

# ---------------------------- Manejo de Errores: -------------------------#
# Errores: sintácticos, semánticos (podemos evitarlos y prevenirlos)
# # Erroeres de ejecución (tratamos de lanzar excepciones para tratarlos).

# Exception: genérica, todas las excepciones son d eeste tipo
# AssertError: una instruccion assert falló.
# IndexError: ecceso a un indice fuera de rango.
# Keyerror: acceso a diccionario, clave inexistente.
# TypeError: operacion a un valor de tipo inapropiado.
# ValueError: tipo apropiado, valor inapropiado.
# ZeroDivisionError: se intentó dividir por 0
# IOError: Error de entrada o salida, acceso a un archivo.

# try - except - finally
'''
dividendo = 5
divisor = 0
try:
    resultado = dividendo / divisor
except:
    print("No se puede dividir por cero")
'''

# varios errores en el mismo bloque de codigo
'''
try:
    <codigo>
except IOError:
    <codigo>
except ZeroDivisionError:
    <codigo>
except:
    <cuando se produzca un error no contemplado antes>
'''

# ---------- NO ---------- #
# Nunca se pone el except generico antes de los genericos.

# Con finally:

archivo = None
# la variable archivo se crea afuera
# porque si falla el try, el finally daría error
'''
try:
    archivo = open("miarchivo.txt")
except IOError:
    print("Error de entrada y salida")
    # No hay ningun archivo con ese nombre
except:
    print("Except genérico")
finally:
    # POST proceso, ejecuta siempre
    print("Llegó al finally")
    if archivo and not archivo.closed:
        archivo.close()
'''
'''
try:
    # me ahorro la asignacion anterior y el finally con el close()
    with open("miarchivo.txt") as archivo:
        pass # acá va a ir código en algun momento
except:
    print("generico")
'''

# Dejar constancia de la excepcion o propagarla o ambas.
# Dejar constancia: Archivo LOG.
# Propagarla: raise (invocar)
'''
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print("Excepción atrapada: ", e)
'''
# Validaciones: contenido, ingresos del usuario

# Ejemplo:
# Pide un valor una y otra vez hasta que ingreses el correcto
'''
def pedir_entero():
    # Hasta que no ingrese el numero correctamente
    while True:
        valor = input("Ingrese un numero entero: ")
        try:
            return int(valor)
        except ValueError:
            print("'{}' no es un número entero.".format(valor))

pedir_entero()
'''
'''
def pedir_entero():
    intentos = 0
    # Cinco intentos para ingresar el número correcto
    while intentos < 5:
        valor = input("Ingrese un numero entero: ")
        try:
            return int(valor)
        except ValueError:
            print("'{}' no es un número entero.".format(valor))
            intentos += 1
    raise ValueError("Valor incorrecto ingresado en 5 intentos")

pedir_entero()
'''
'''
i = "A"
if type(i) is not int:
    raise TypeError("i debe ser del tipo int")
'''

# ERRORES:
'''
Sintaxis: detectados por el interprete.
Semantica: el programa no funciona correctamente.
Ejecucion: Excepciones.
'''

# -------------- TAREA: ---------------#

# Ejercicios:
# 11.10.1. Escribir un programa llamado head que reciba
# un archivo y un número N e imprima las primeas N lineas
# del archivo.

# Ejercicio 11.10.2. Escribir un programa, llamado cp.py, 
# que copie todo el contenido de un archivo
# (sea de texto o binario) a otro, de modo que quede exactamente igual.
# Nota: utilizar archivo.read(bytes) para leer como máximo una cantidad de bytes.