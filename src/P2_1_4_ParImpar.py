"""Ejercicio 2.1.4¶
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar."""
def pares(numero):
    
    if (numero%2 == 0):
        return "El número es par."
    else: 
        return "El número es impar."
    
def main():
    
    print("Introduce un número entero: ")
    numero = int(input())
    
    if (numero%2 == 0):
        print ("El número es par.")
    else:
        print("El número es impar.")
        
if __name__=="__main__":
    main()