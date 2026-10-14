#Los tramos impositivos para la declaración de la renta en un determinado país son
#los siguientes:

#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla
#el tipo impositivo que le corresponde.

renta = int(input("Dime tu renta actual: "))
if renta < 10000 :
    print("Tu impositivo es del 5%")
elif renta > 10000 and renta < 20000:
    print("Tu impositivo es del 15%")
elif renta > 20000 and renta < 35000:
    print("Tu impositivo es del 20%")
elif renta > 35000 and renta < 60000:
    print("Tu impositivo es del 30%")    
elif renta > 60000:
    print("Tu impositivo es del 45%")   