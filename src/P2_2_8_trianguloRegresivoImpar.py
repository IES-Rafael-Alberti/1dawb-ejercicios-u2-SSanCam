"""Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1"""
def trianguloRegresivo(numero):
    nivel = 1
    serie = ""
    
    while (nivel <= numero):
        
        for num in range(nivel, 0, -2):
            serie += (str(num)) + " "
            
        serie += "\n"
        nivel += 2  
        
    return serie

def main():
    
    print("Ingresa un número entero cualquiera: ")
    numero = int(input())
    
    resultado = (trianguloRegresivo(numero))
    
    return resultado
    
if __name__=="__main__":
    main()