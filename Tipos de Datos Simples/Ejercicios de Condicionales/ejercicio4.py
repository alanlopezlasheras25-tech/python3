#Escribir un programa que pida al usuario un número entero y muestre por pantalla si
#es par o impar.
numero = int(input("Dime un numero: "))
division = numero % 2
if division == 0 :
    print("El numero es par")
else:
    print("El numero es impar")