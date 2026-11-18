#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y
#muestre por pantalla el número de veces que aparece la letra en la frase.
letra = input("Dime una letra: ")
frase = input("Dime una frase: ")
if len(letra) != 1:
    print("Debes poner un caracter")
else:
    contador = frase.lower().count(letra.lower())
    print(f"La letra {letra} aparece {contador} veces en {frase}")