#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
#Los ingredientes para cada tipo de pizza aparecen a continuación.
#● Ingredientes vegetarianos: Pimiento y tofu.
#● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y
#en función de su respuesta le muestre un menú con los ingredientes disponibles
#para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el
#tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la
#pizza elegida es vegetariana o no y todos los ingredientes que lleva.

pregunta = input("¿Quieres una pizza vegetariana o no ?: ")
if pregunta.lower() == "si":
    ingrediente = input("¿Quieres una pimiento o tofu?: ")
    if ingrediente.lower() == "tofu":
        print("Has elegido una pizza vegetariana con Mozzarella , tomate y tofu") 
    if ingrediente.lower() == "pimiento":
     print("Has elegido una pizza vegetariana con Mozzarella , tomate y pimiento")     
else:
    ingrediente = input("¿Quieres una Peperoni, Jamón y Salmón?: ")
    if ingrediente.lower() == "peperoni":
            print("Has elegido una pizza con Mozzarella , tomate y peperoni") 
    elif ingrediente.lower() == "jamón":
            print("Has elegido una pizza con Mozzarella , tomate y jamón")
    elif ingrediente.lower() == "salmón":
             print("Has elegido una pizza con Mozzarella , tomate y salmón")