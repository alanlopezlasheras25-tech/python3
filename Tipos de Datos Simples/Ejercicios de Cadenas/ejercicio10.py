#Escribir un programa que pregunte por consola por los productos de una cesta de la
#compra, separados por comas, y muestre por pantalla cada uno de los productos en
#una línea distina
compra = input("Dime los productos de tu cesta de la compra, separados por comas: ")
productos = compra.split(',')
for producto in productos:
    print(producto.strip())