"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
todos los números impares desde 1 hasta ese número separados por comas."""
def comparaNumero (numero):
    
    if (numero%2 == 0):
        return "Éste número es par."
    
    else:
        return "Éste número es impar."
    
    

def main():
    
    print("Introduce un número positivo: ")
    numero = int(input())
    
    resultado = comparaNumero(numero)
    
    print (resultado)

if __name__=="__main__":
    main()