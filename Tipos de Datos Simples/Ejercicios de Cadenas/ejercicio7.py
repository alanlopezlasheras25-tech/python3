#Escribir un programa que pregunte el correo electrónico del usuario en la consola y
#muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante
#de la arroba @) pero con dominio ceu.es.
correo = input("Dime una tu correo electronico: ")
nombre = correo.split('@')[0]
final = "ceu.es"
print(f"Tu nuevo correo es: {nombre}@{final}")
