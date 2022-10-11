#Ejercicio 1

import sys

def insertar_numero():
    return input("Introduzca un número: ")

primero=insertar_numero()
segundo=insertar_numero()
tercero=insertar_numero()

if int(primero)==0:
    print("Error, el primer número no puede ser 0")
elif primero<segundo<tercero:
    print("Están en orden ascendente")
else:
    print("No están en orden ascendente")