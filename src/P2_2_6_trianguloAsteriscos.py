def triangulo(niveles):
    
    estrellas = 1
    triangulo = ""
    while (estrellas != niveles+1):
        triangulo = triangulo + (f"{"*" * estrellas}\n")
        estrellas += 1
           
    return triangulo

def main():
    
    print("Introduce cuántos niveles quieres que tenga tu triángulo: ")
    niveles = int(input())

    print(triangulo(niveles))
    
if __name__=="__main__":
    main()