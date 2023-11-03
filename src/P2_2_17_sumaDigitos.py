def sumaNum(numero):
    lista_num = str(numero)
    suma_digitos = 0
    
    for num in (lista_num[:]):
        suma_digitos += (int(num))
        
    return suma_digitos 



##__MAIN__##

def main():
    
    print("Introduce una cifra, de la cual aremos la suma de sus dígitos: ")
    numero = int(input())
    
    return print(f"La suma de los dígitos es de: {sumaNum(numero)}")
    
if __name__=="__main__":
    main()