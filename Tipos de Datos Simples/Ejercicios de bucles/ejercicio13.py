#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta
#que el usuario escriba “salir” que terminará.

while True:

    frase = input("Dime una frase o palabra hasta que digas salir: ")
    if frase.lower() == "salir" :
        break
    print(frase)
