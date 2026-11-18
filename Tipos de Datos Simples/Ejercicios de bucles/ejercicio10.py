#Escribir un programa que pida al usuario un número entero y muestre por pantalla si
#es un número primo o no.
num = int(input("Dime un numero entero: "))
i = 2
while num % i != 0:
    i += 1 
if i == num :
    print(f"{num} es primo")
else:
    print(f"{num} no es primo")
    