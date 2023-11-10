"""Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. 
Por cada número, informar cuántos dígitos pares y cuántos impares tiene. 
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total."""
def cont_par_impar(numero) -> str:
    
    num_totales = 0
    cadena_numeros = ""
    suma_pares = 0
    suma_impares = 0
    
    while (numero != 0):
        
        if (numero > 0):
            num_totales += 1
            cadena_numeros = cadena_numeros + str(numero) + ", "
            
            if (numero%2 == 0):
                suma_pares += 1
            else:
                suma_impares += 1
                
        print("Ingresar otro número: ")   
        numero = int(input())        
    
    resultado = f"De un total de {num_totales} números totales:\n\n· {suma_pares} números han sido números pares.\n· {suma_impares} números han sido números impares.\n\nLos números ingresados han sido: {cadena_numeros[:-2]}"
            
    return (resultado)



def main():
    
   print("Introduce todos los números enteros que desees.\nIngresa \"0\" para finalizar.") 
   print("Ingresa tu número:")
   numero = int(input())
   return print(cont_par_impar(numero))

if __name__=="__main__":
    main()