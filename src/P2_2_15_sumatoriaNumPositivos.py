"""Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
Finalmente, mostrar la sumatoria de todos los números positivos ingresados."""

def sum_num_pos():
    print("Ingresa todos los nuúmeros que desees.\nCuando quieras finalizar, ingresa el número 0: ")
    numero = int(input())    
    sumatoria = 0 
    
    while (numero != 0):
        if (numero > 0):
            sumatoria = sumatoria + numero 
            
        numero = int(input())
        
        if (numero == 0):
            mensaje = print(f"La suma de todos los numeros ingresados es de: {sumatoria}")
        
    return mensaje 

def main():
    
    resultado = sum_num_pos()
    return resultado
    
if __name__=="__main__":
    main()