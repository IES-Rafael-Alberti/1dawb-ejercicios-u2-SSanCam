"""Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el
número de años, y muestre por pantalla el capital obtenido en la inversión cada año que
dura la inversión.

# Formula para calcular El capital tras un año.
amount *= 1 + interest / 100
# En donde:
# - amount: Cantidad a invertir
# - interest: Interes porcentual anual"""

def capitalObtenido (inversion: float, interes: int, anios: int):
    
    interes = int(interes) / 100
    
    for bonificacion in range(1, int(anios)+1):
        inversion *= 1 +  interes
        
    inversion_formateada = "{:.2f}€".format(inversion)
    
    print("Tras un año, su inversión ha generado un total de: ")
    return inversion_formateada


print(capitalObtenido(1000,10,1))

def main():
    
    print("Introduce el capital que quieres invertir: ")
    inversion = float(input())
    
    print("Introduce el tipo de intereés que quieres aplicar: ")
    interes = int(input())
    	
    print("Indica durante cuántos años quieres mantener la inversión: ")
    anios = int(input()) 
    
    resultado = capitalObtenido(inversion, interes, anios)
    print(resultado)
    
if __name__=="__main__":
    main()