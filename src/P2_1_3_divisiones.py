"""Ejercicio 2.1.3¶
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error."""
def division (num1, num2):
    if (num2 == 0):
        return "ERROR.\n No puede dividirse entre 0."
    else:
        resultado = f"El resultado de dividir {num1}/{num2} es: {num1/num2:.2f}"
        return resultado
    
def main():
    print("Introduce un numero: ")
    num1 = float(input())
    num2 = float(input())
    
    if (num2 == 0):
        print("ERROR.\nNo puede dividirse entre 0.")
    else:
        resultado = f"El resultado de dividir {num1}/{num2} es: {num1/num2:.2f}"
        print (resultado)
        
if __name__=="__main__":
    main()