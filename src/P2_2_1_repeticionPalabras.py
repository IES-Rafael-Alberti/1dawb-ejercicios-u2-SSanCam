"""
Ejercicio 2.2.1
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""
def repeticion(palabra):
    
    resultado = ""
    
    for cad in range(1,10):
        resultado = resultado + palabra.replace(" ","") + ", "
    
    resultado = resultado + palabra.replace(" ","")
    
    return resultado 


def main():
    
    print("Introduce la palabra que quieras repetir 10 veces: ")
    palabra = str(input())
    
    palabraRepetida = repeticion(palabra)
    
    print (palabraRepetida)

if __name__=="__main__":
    main()