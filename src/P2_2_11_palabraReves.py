"""Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a
una las letras de la palabra introducida empezando por la última."""
def revesPalabra (palabra):
    reves = ""
    for letra in palabra[::-1]:
        reves = reves + letra
        
    return reves 


###__main__###

def main():
    
    print("Introduce la palabra que quieras ver al revés: ")
    palabra = str(input())
    
    resultado = print(revesPalabra(palabra))
    
    return resultado

if __name__=="__main__":
    main()