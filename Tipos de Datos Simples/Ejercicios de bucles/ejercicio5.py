#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
#año que dura la inversión.

cantidad = float(input("Dime una cantidad a invertir: "))
interes = float(input("Dime el interés anual: "))
ano = float(input("Dime el número de años: "))
for i in range(1, int(ano) + 1):
    cantidad = cantidad + (cantidad * interes / 100)
    print(f"Capital obtenido en el año {i}: {cantidad:.2f}")
