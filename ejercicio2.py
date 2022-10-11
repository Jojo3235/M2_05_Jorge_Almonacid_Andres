#Ejercicio 2

import sys

numeros=[]

def insertar_numero():
    return input("Introduzca un número: ")

def añadir_a_lista():
    return numeros.append(insertar_numero())

primero=añadir_a_lista()
segundo=añadir_a_lista()
tercero=añadir_a_lista()

print(numeros)

if int(numeros[0])==0:
    print("Error, el primer número no puede ser 0")
elif numeros[0]<numeros[1]<numeros[2]:
    print("Están en orden ascendente")
else:
    print("No están en orden ascendente")