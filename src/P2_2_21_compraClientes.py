"""Crear un programa que permita al usuario ingresar los montos de las compras de un cliente 
(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
cortando el ingreso de datos cuando el usuario ingrese el monto 0. 
Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. 
Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, 
se le debe aplicar un 10% de descuento."""
def ticket_montos(precio_unitario: float) -> str:
    
    continuar = True  
    totalMonto = 0
    
    while continuar:
        
        while (precio_unitario < 0.0):
            print("Error. Debes introducir cifras numericas positivas.")
            print("Siguiente monto: ")
            precio_unitario = float(input())
        
        if (precio_unitario > 0): 
            totalMonto += precio_unitario
            print("Siguiente monto: ")
            precio_unitario = float(input())
            
        if (precio_unitario == 0):
            continuar = False
            
    ticket = print(f"El total es de: {totalMonto:.2f}€")
    
    return ticket 

def main():
    
    print("Ingresa la cantida de los montos para sumarlas: ")
    precio_unitario = float(input())
    
    ticket_montos(precio_unitario)
    
if __name__=="__main__":
    main()