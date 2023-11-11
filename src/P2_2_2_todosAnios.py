"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años
que ha cumplido (desde 1 hasta su edad).
"""
def cantidadAnios(edad):
    serieEdad = ""
    
    for anio in range(1, edad):
        
        serieEdad = serieEdad + str(anio) + ", "
        
    serieEdad = serieEdad + str(edad)
    
    return serieEdad

print (cantidadAnios(5))
def main():
    
    print("Introduce tu edad: ")
    edad = int(input())
    
    print("Desde que naciste, has cumplido:")
    
    resultado = cantidadAnios(edad)
    
    return resultado
    
if __name__=="__name__":
    main()