#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
hora= input("¿Numero de horas que trabajas? ")
coste= input("¿Coste por hora? ")
sueldo= float(coste) * float(hora) 
print(f"El sueldo es de {sueldo} euros")

