#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene
#un descuento del 60%. Escribir un programa que comience leyendo el número de
#barras vendidas que no son del día. Después el programa debe mostrar el precio
#habitual de una barra de pan, el descuento que se le hace por no ser fresca y el
#coste final total.

nofrescas = int(input("Introduce el número de barras vendidas que no son del día: "))

precio = 3.49
descuento = 0.60 * precio
coste = (nofrescas * precio ) * 0.60

print(f"El precio habitual de una barra de pan es: {precio}€")

print(f"El descuento que se le hace por no ser fresca es: {descuento}%")

print(f"El coste final total es: {round(coste, 2)}€")
