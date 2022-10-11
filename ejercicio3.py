""" Realiza un programa que lea letras y cuente con una variable contador las letras "a" que se introducen. 
 Para salir del programa, introducir el carácter ".". Al finalizar mostrar el número de veces que se ha pulsado la letra "a"."""
 #Ejercicio 3

palabra=input("Introduce una oració, frase o palabra para contar cuantas veces tiene una letra: ")
letra=input("Introduce que caracter quieres que cuente: ")
print(palabra.count(letra))
