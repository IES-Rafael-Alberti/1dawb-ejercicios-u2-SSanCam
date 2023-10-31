"""La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva."""

def pedidoPizza(tipoPizza, ingrediente):
    pizzaPedida = ""
    condumio = ""

    if tipoPizza.upper() == "V":
        pizzaPedida = "Vegetariana"

        if ingrediente == 1:
            condumio = "1.-Pimientos."
            
        elif ingrediente == 2:
            condumio = "2.-Tofu."
            
            
    elif tipoPizza.upper() == "NV":
        pizzaPedida = "No vegetariana"
        
        if ingrediente == 1:
            condumio = "1.-Peperoni."
            
        elif ingrediente == 2:
            condumio = "2.-Jamón."
            
        elif ingrediente == 3:
            condumio = "3.-Salmón."
            
    cabecera1 = "**************************"
    ancho = len(cabecera1)
    nombre =("--BELLA NAPOLI--".center(ancho))
    opcion = (f"Has elegido pizza:\n--{pizzaPedida}--").center(ancho)
    ingredientePedido =(f"Los ingredientes son: \n\n1.-Salsa de tomate\n2.-Queso\n{condumio}").center(ancho)
    
    ticket = (f"{cabecera1}\n{nombre}\n{cabecera1}\n{opcion}\n\n{ingredientePedido}\n\n{cabecera1}\n")
    print (ticket)
    
    return condumio

######################___MAIN___######################

def main():
    
    print("Indica si quieres pizza [V]egetariana o [NV] No Vegetariana.")
    tipoPizza = str(input())
    
    print("Todas las pizzas tienen base de tomate y queso, elige un tercer ingrediente.")
    
    print("Introduce el número del ingrediente que desees:\n ·Vegetarianos:\n1.-Pimientos.\n2.-Tofu.\nNo Vegetarianos:\n1.-Peperoni\n2.-Jamón\n3.-Salmón.")
    ingrediente = int(input())
    
    resultado = pedidoPizza(tipoPizza, ingrediente)
    
    print(resultado)

if __name__=="__main__":
    main()
    