def suma_digis_multiple(cifra):
    from P2_2_17_sumaDigitos import sumaNum
    
    lista_numeros = []
        
    while (cifra != -1):
        cifra = int(input())
        digitos_sumados = sumaNum(cifra)
        
        if ( digitos_sumados%2 == 0):
            digitos_sumados.append(lista_numeros)
        
    if (cifra == -1):
        print("Esta es la lista de los números sumando sus digitos:\n")
        lista_final = print(lista_numeros)
        
    return lista_final



def main():
    
    print("Introduce el número del que quiere que sumemos sus dígitos: ")
    cifra = int(input())
    
    while (cifra != -1):
        cifra = int(input())
        suma_digis_multiple(str(cifra))
    
    if cifra == -1:
        return 
        
    
if __name__=="__main__":
    main()