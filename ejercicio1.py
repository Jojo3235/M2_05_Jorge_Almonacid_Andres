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