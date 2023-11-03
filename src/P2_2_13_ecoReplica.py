"""Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el
usuario escriba “salir” que terminará."""

def eco(repetir):
    import time 
    
    while (repetir.lower() != "salir"):
        eco = str(input(">>"))
        repetir = eco
        print (repetir)
        
        if (eco.lower() == "salir"):
            print("Saliendo del programa...")
            time.sleep(2)
            break   

def main():
    print("Escribe \"salir\" si quieres finalizar el programa.")
    print("Introduce palabras y las iré repitiendo: ")
    repetir = str(input())
    
    resultado = eco(repetir) 
    
    print(resultado)
        
if __name__=="__main__":
    main()
