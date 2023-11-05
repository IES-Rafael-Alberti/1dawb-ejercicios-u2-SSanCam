"""Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. 
Por cada número, informar cuántos dígitos pares y cuántos impares tiene. 
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total."""

def num_pares_impares ():
        
    lista_numeros = []
    suma_pares = 0
    suma_impares = 0
    
    seguir = True
    
    while seguir:
        print("Ingresa un numero entero: ")
        numero = str(input())
        
        lista_numeros.append(numero)
        
        if (numero == 0):
            seguir = False 
            
    
    for cifra in lista_numeros:
        for digito in cifra:
            
            if (digito%2 == 0):
               print(f"De {cifra}: {digito} es par.")
               suma_pares += 1
            else:
               print(f"De {cifra}: {digito} es impar.")
               suma_impares += 1
                
   
def main(): 
    
    num_pares_impares()

if __name__=="__main__":
    main()