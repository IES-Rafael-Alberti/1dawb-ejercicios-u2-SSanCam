"""Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
finalizando cuando se reciba un cero. 
Imprimir la cantidad de números primos ingresados."""
def comp_num_primos(numero):
    
    cont_numeros = 0 
    lista_numeros = ""
        
    while (numero != 0):
        
        for primo in range(2, int(numero**0.5) + 1):
            if numero % primo == 0:
                lista_numeros = lista_numeros + str(numero) + ", "
                cont_numeros += 1
            
        numero = int(input("Ingresa otro número 0 para finalizar: "))
        
    resultado = (f"Has introducido {cont_numeros} números primos.\nHan sido: {lista_numeros[:-2]}")

    return resultado 



def main():
    
    print("Introduce un numero entero positivo:")
    numero = int(input())
    resultado = comp_num_primos(numero)
    
    return print(resultado)
    
    
    
if __name__=="__main__":
    main()    
        
    