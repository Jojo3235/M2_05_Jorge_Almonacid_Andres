 #Ejercicio 3

while True:
    palabra=input("Introduce una oración, frase o palabra para contar cuantas veces tiene la letra a: ")
    if palabra==".":
        break
    else:
        palabra=palabra.lower()
        print(palabra.count("a"))
        print("Para finalizar el programa introduzca '.'") 