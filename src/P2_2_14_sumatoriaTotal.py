def sumaTotal():
    
    print("Ingresa los números que quieras sumar, introduce 0 si quieres acabar.")
    print("Ingresa tus número: ")
    numero = int(input())    
    sumatoria = 0
    
    while (numero != 0):
        sumatoria = sumatoria + numero
        numero = int(input())
    
    if (numero == 0):
        mensaje = print(f"La suma de todos los numeros ingresados es de: {sumatoria}")
        
    return mensaje 

def main():
    
    resultado = sumaTotal()
    return resultado
    
if __name__=="__main__":
    main()