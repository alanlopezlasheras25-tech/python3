#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y
#el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y
#los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un
#programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo
#que le corresponde.

nombre = input("Dime tu nombre: ")
sexo = input("Dime tu sexo: ")
if (sexo.lower() == "f" and nombre.lower() < "m" ):
    print("Eres del grupo A")

elif (sexo.lower() == "m" and nombre.lower() > "n" ):
    print("Eres del grupo B")
