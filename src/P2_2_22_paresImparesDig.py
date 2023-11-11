"""Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. 
Por cada número, informar cuántos dígitos pares y cuántos impares tiene. 
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total."""


def tipo_entrada(numero: int) -> str:
    
    cadena_numeros = ""
    suma_pares = 0
    suma_impares = 0
    
    while (type(numero) != int):
        numero = int(input())
    
    while (numero != 0) and (numero < 10):
        
        for digito in str(numero):
            
            if (int(digito)%2 == 0):
                suma_pares += 1
            else: 
                suma_impares += 1
                
        print("Ingresa otro numero o 0 para finalizar: ")
        numero = int(input())
        
    while (numero != 0) and (numero > 9):
        for digito in str(numero):
            
            if (int(digito)%2 == 0):
                suma_pares += 1
            else:
                suma_impares += 1
        print("Ingresa otro numero o 0 para finalizar: ")
        numero = int(input())
    
    resultado = f"De todos los numeros ingresados:\n{suma_impares} han sido digitos impares.\n{suma_pares} han sido digitos pares."

    return resultado


def main():
    
    print("Introduce un numero entero: ")
    numero = int(input())
    
    resultado = tipo_entrada(numero)
    
    return print(resultado)
    
if __name__=="__main__":
    main()