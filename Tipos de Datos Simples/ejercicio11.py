#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de
#interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de
#año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que
#comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
#introducida por el usuario. Después el programa debe calcular y mostrar por pantalla
#la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada
#cantidad a dos decimales.

ahorrro = float(input("Introduce la cantidad de dinero depositada: "))

porcentaje = 0.04

año1 = ahorrro + ahorrro * porcentaje

año2 = año1 + año1 * porcentaje

año3 = año2 + año2 * porcentaje

print(f"Los ahorros del primer año son: {round(año1, 2)}")

print(f"Los ahorros del segundo año son: {round(año2, 2)}")

print(f"Los ahorros del tercer año son: {round(año3, 2)}")