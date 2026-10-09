#Escribir un programa que pida al usuario dos números y muestre por pantalla su
#división. Si el divisor es cero el programa debe mostrar un error.

primer = int(input("Dime el primer numero: "))
segun =  int(input("Dime el segundo numero: "))



if segun == 0 :
    print("Error")
else:
    division = primer/segun
    print(f'{division}')