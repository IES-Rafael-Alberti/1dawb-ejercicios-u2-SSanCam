"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta."""

def pedirClave(clave):
    
    from P2_1_2_cadenaContrasenia import iniciarSesion
    clave = str(input()).replace(" ", "")
    
    while (iniciarSesion(clave) != "Contraseña correcta!"):
        print("Intenta introducir de nuevo la contraseña: ")
        clave = str(input()).replace(" ", "")
    
    return "Contraseña correcta!"
    

print(pedirClave("ay TOR tilla"))
####__MAIN__####

"""def main():
    
    print("Introduce tu clave: ")
    clave = str(input()).replace(" ", "")
    
    if (pedirClave(clave)) == "Contraseña correcta!" :
        return "Contraseña correcta!" 
    
if __name__=="__main__":
    main()"""