"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta."""
def comprobarClave(clave):
    from src.P2_1_2_cadenaContrasenia import iniciarSesion
    return iniciarSesion(clave.replace(" ", "").lower())

def main():
    print("Introduce tu contraseña: ")
    clave = str(input()).replace(" ", "").lower()
    
    while comprobarClave(clave) != "Contraseña correcta!":
        print("ERROR.\nIntroduce de nuevo la contraseña: ")
        clave = str(input()).replace(" ", "").lower()
    
    print("Acceso concedido.")

if __name__ == "__main__":
    main()