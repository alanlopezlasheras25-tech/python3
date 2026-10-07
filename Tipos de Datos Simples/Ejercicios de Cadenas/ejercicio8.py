#Escribir un programa que pregunte por consola el precio de un producto en euros
#con dos decimales y muestre por pantalla el número de euros y el número de
#céntimos del precio introducido.

precio = input("Dime el precio de un producto en euros con dos decimales: ")
euro = precio.split('.')[0]
centimo = precio.split('.')[1]
print(f"El precio es: {euro} euros y {centimo} centimos")