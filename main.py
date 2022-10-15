#Ejercicio 1

from funciones import insertar_numero

primero=insertar_numero()
segundo=insertar_numero()
tercero=insertar_numero()

if int(primero)==0:
    print("Error, el primer número no puede ser 0")
elif primero<segundo<tercero:
    print("Están en orden ascendente")
else:
    print("No están en orden ascendente")

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

#Ejercicio 3

while True:
    palabra=input("Introduce una oración, frase o palabra para contar cuantas veces tiene la letra a: ")
    if palabra==".":
        break
    else:
        palabra=palabra.lower()
        print(palabra.count("a"))
        print("Para finalizar el programa introduzca '.'") 

#Ejercicio 4
from funciones import palabra_mas_larga

lista_palabras=["Cubo", "Esfera", "Piramide", "Dodecaedro"]

palabra_mas_larga(lista_palabras)