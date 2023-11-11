"""Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no."""

def aptoTributar(edad: int, ingresos: float):
    if (edad > 16 and ingresos >= 1000):
        return "Puedes tributar."
    else:
        return "No cumples los requisitos necesarios para tributar."

def main():
    print("Introduce tu edad: ")
    edad = int(input())
    print("Introduce tus ingresos mensuales: ")
    ingresos = float(input())
    
    if (edad > 16) and (ingresos >= 1000.00):
        print("Puedes tributar.")
    else:
        print ("No cumples los requisitos necesarios para tributar.")

if __name__=="__main__":
    main()