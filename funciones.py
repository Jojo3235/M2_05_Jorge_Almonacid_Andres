def insertar_numero():
    return input("Introduzca un número: ")

def añadir_a_lista(lista):
    return lista.append(insertar_numero())

def letras_palabra(palabra):
    for elements in palabra:
        print(elements,len(elements))

def palabra_letras(palabra,letras):
    print("La palabra más larga es", palabra[letras],"con",len(palabra[letras]),"letras")

def palabra_mas_larga(palabra):
    letras_palabra(palabra)
    if len(palabra[0])>len(palabra[1])>len(palabra[2])>len(palabra[3]):
        palabra_letras(palabra,0)
    elif len(palabra[1])>len(palabra[0])>len(palabra[2])>len(palabra[3]):
        palabra_letras(palabra,1)
    elif len(palabra[2])>len(palabra[0])>len(palabra[1])>len(palabra[3]):
        palabra_letras(palabra,2)
    else:        
        palabra_letras(palabra,3) 
