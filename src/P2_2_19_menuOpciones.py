"""Mostrar un menú con tres opciones: 
1- comenzar programa, 
2- imprimir listado, 
3-finalizar programa. 
A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). 
Si elige una opción incorrecta, informarle del error. 
El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. 
Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará."""

def menu_op(opcion: int) -> str:
    menu = ("===MENU===\n\n1 - INICIAR PROGRAMA\n2 - IMPRIMIR LISTADO\n3 - FINALIZAR PROGRAMA")
 
    while (opcion not in range(1,4)):
        print("\nERROR.\mDebes introducir el numero de alguna de las opciones:\n ")
        print("===MENU===\n\n1 - INICIAR PROGRAMA\n2 - IMPRIMIR LISTADO\n3 - FINALIZAR PROGRAMA")
        opcion = int(input())
        
        while (opcion in range(1, 4)):
                        
            if (opcion == 1): 
                print("***INICIANDO PROGRAMA***")
                print("===MENU===\n\n1 - INICIAR PROGRAMA\n2 - IMPRIMIR LISTADO\n3 - FINALIZAR PROGRAMA")
                opcion = int(input())
                    
            elif (opcion == 2):
                print("***IMPRIMIENDO LISTADO***")
                print("===MENU===\n\n1 - INICIAR PROGRAMA\n2 - IMPRIMIR LISTADO\n3 - FINALIZAR PROGRAMA")
                
                opcion = int(input())
                            
            if (opcion == 3):
                print("**SALIENDO DEL PROGRAMA**")
                break    
        
                
            
    
def main():
    
    print("===MENU===\n\n1 - INICIAR PROGRAMA\n2 - IMPRIMIR LISTADO\n3 - FINALIZAR PROGRAMA")
    
    try:
        opcion = int(input("Selecciona una de las tres opciones: "))
        menu_op(opcion)

    except ValueError as e:
        print("Debes introducir un valor numerico.")
    
if __name__=="__main__":
    main()