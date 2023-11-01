"""Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre
por pantalla el número de veces que aparece la letra en la frase."""

def contadorLetras(frase: str, letra: str):
    contadorLetra = 0 
    
    for caracter in frase.lower():
        if (letra.lower() == caracter):
            contadorLetra += 1
            
    print(f"Número de ocurrencias de la letra \"{letra}\" : ")
    
    return contadorLetra 


def main():
    
    print("Introduce una frase: ")
    frase = str(input())
    
    print("Introduce la letra que quieres encontrar: ")
    letra = (input())
    
    resultado = print(contadorLetras(frase, letra))

    return resultado 


if __name__=="__main__":
    main()