#Escribir un programa que pida al usuario dos números enteros y muestre por
#pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde
#<n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente
#y el resto de la división entera respectivamente.
prime= int(input("Dame un numero entero "))
segun= int(input("Dame otro numero entero "))

cociente= prime / segun
resto= prime % segun


print(f"{prime} entre {segun} da un cociente {cociente} y un resto {resto} ")
