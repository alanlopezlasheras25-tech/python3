#Escribir un programa que almacene la cadena de caracteres contraseña en una
#variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
#correcta.

contraseña = "hola"
while True:
    intento = input("Introduce la contraseña: ")
    if intento == contraseña:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo")