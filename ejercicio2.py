#Ejercicio 2

from funciones import añadir_a_lista

numeros=list()

primero=añadir_a_lista(numeros)
segundo=añadir_a_lista(numeros)
tercero=añadir_a_lista(numeros)

print(numeros)

if int(numeros[0])==0:
    print("Error, el primer número no puede ser 0")
elif numeros[0]<numeros[1]<numeros[2]:
    print("Están en orden ascendente")
else:
    print("No están en orden ascendente")