#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),calcule el índice de masa corporal y lo almacene en una variable, y muestre por
#pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el
#índice de masa corporal calculado redondeado con dos decimales

peso= input("Dame tu peso en Kg: ")
altura= input("Dame tu estatura en metros: ")
imc= float(peso) / (float(altura) * float(altura)) 
resultado= round(imc, 2)
print(f"tu imc es de {resultado}")

