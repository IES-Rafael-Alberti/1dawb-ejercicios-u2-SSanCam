"""Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. 
Informar cuál fue el mayor número ingresado."""

def mayor_num_positivo(numero):
    
    lista_numero = []
    
    while (numero != 0):
        numero = int(input())
        if (numero > 0):
            lista_numero.append(numero)
    
    if (numero == 0):
        print(f"De todos los números que has ingresado, el mayor número positivo ha sido: {max(lista_numero)}")
        num_mayor = max(lista_numero)
    return num_mayor


##__MAIN__##
def main():
    
    print("Introduce todos los números que quieres que recoja.\nCuando quieras finalizar, ingresa el número 0.")
    print("Introduce tus números: ")
    numero = int(input())
    
    mayor_num_positivo(numero)
    
if __name__=="__main__":
    main()
        
        