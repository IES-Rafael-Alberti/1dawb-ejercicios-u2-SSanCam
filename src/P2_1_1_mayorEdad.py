def mayorEdad(anios: int):
    
    if anios < 18:
        mensaje = "Eres menor de edad."
        
    elif anios > 100:
        mensaje = "Relája, Nosferatu."
        
    else:
        mensaje = "Eres mayor de edad."
    
    return mensaje

def main():
    print("Que edad tienes: ")
    anios = int(input())
    
    if anios < 18:
        print("Eres menor de edad.")
    elif anios > 100:
        print("Relája, Nosferatu.")
    else: 
        print("Eres mayor de edad.")
        
if __name__=="__main__":
    main()