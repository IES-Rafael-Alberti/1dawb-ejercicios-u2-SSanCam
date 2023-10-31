"""Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde."""

def declaracion(renta):
    
    if (renta < 10000):
        impositivo = 5
        
    elif (renta < 20000):
        impositivo = 15
        
    elif (renta < 35000):
        impositivo = 20
        
    elif (renta < 60000):
        impositivo = 30
        
    else:
        impositivo = 45
        
    return "{:}%".format(impositivo)
    
def main(): 
    print("Introduce tu renta anual: ")
    renta = float(input())
    
    impositivo = declaracion(renta)
       
    print (f"Para tu renta de {renta}€, corresponde un impositivo del {impositivo}")

if __name__=="__main__":
    main()