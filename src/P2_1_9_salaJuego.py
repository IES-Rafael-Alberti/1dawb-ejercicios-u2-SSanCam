"""Ejercicio 2.1.9¶
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€."""

def precioEntrada(edad: int):
    
    if (edad < 4):
        print("El precio de tu entrada es de: ")
        precio = 0 
    elif (edad <18):
        print("El precio de tu entrada es de: ")
        precio = 5
    else:
        print("El precio de tu entrada es de: ")
        precio = 10
        
    return "{:}€".format(precio)

def main():
    print("Introduce tu edad: ")
    edad = int(input())
    
    resultado = precioEntrada(edad)
    
    print(f"Para la edad de {edad} años, le corresponde una entrada de {resultado}")
    
if __name__=="__main__":
    main()