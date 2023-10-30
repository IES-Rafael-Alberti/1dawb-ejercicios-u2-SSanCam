def contrasenia(cadena: str):
    password = "aytortilla"

    while cadena.lower() != password:
        print("Ingresa tu contraseña: ")
    
    if (cadena.lower() == password):
        return "Contraseña correcta."
    else: 
        return "Contraseña incorrecta."
    

def comprobarCadena():
    return "aytortilla"

def main():
    
    resultado = comprobarCadena()
    password = "aytortilla"
    
    if password == resultado:
        print("Contraseña correcta!")
    else:
        print("Contraseña incorrecta!")

if __name__=="__main__":
    main()
