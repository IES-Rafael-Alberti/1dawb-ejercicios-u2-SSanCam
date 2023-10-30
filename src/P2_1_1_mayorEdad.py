def edad(anios):
    
    if (anios > 0 ):
        
        if (anios >= 18):
            mensaje = "Eres mayor de edad."
        else:
            mensaje = "Eres menor de edad."
            
        if (anios > 100):
            mensaje = "Relája, Nosferatus."
            
        return mensaje
    
def main() :
    anios = int(input("Introduce tu edad: "))
    resultado = edad(anios)
    print(resultado)

if __name__=="__main__":
    main()