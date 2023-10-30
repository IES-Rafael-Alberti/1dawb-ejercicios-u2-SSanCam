def contrasenia(cadena: str):
    password = "aytortilla"
    
    while cadena.lower() != password:
        print("Introduce tu contraseña: ")
        cadena = str(input())
    
    if (cadena.lower() == password):
        return "Contraseña correcta!"