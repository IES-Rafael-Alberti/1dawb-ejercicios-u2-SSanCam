"""Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. 
Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más."""

def long_palabra_frase (frase: str) -> str:
    palabras = frase.split()

    palabra_mas_larga = max(palabras, key = len)
    
    resultado = f"La palabra mas larga introducida ha sido: {palabra_mas_larga}"
    return resultado
    
    
def main():
    print("Introduce una frase: ")
    frase = str(input())
    
    resultado = long_palabra_frase(frase)
    return print(resultado)
    

if __name__=="__main__":
    main()