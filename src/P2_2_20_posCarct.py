"""Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). 
Recorrer la frase, carácter a carácter, comparando con la letra buscada. 
Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. 
Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución."""

def posicion_caracter_cadena(frase = str, letra = str) -> str:
    
    lista_posiciones = ""
    
    for index,caracter in enumerate(frase.lower(), start=1):
        if (letra.lower() == caracter):
            lista_posiciones = lista_posiciones + "Posicion: "+ str(index) + "\n"
    
    if (letra.lower() not in frase.lower()):
        print("El caracter no se ha encontrado en la frase.")   
        
    posicion_letra = f"La letra \'{letra.lower()}\' se encuentra en:\n"    
    resultado = posicion_letra + lista_posiciones      
    return print(resultado)

                               
def main():
    
    print("Introduce una frase: ")
    frase = str(input()).lower()
    
    print("Introduce que caracter quieres encontrar: ")
    letra = str(input()).lower()
    
    posicion_caracter_cadena(frase, letra)
    
if __name__=="__main__":
    main()