def restaSeriada(numero):
    
    serie = ""
    
    for numero in range(numero, 0, -1):
        serie = serie + str(numero) + ", "
    
    serie = serie + "0"
    return serie


def main():
    
    print("Introduce un numero entero: ")
    numero = int(input())
    
    resultado = (restaSeriada(numero))
    print (resultado) 

if __name__=="__main__":
    main()