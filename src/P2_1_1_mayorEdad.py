"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no."""
def mayoriaEdad(edad: int):
    
    if (edad >= 18):
        return "Eres mayor de edad."
    elif (edad < 18):
        return "Eres menor de edad."
    elif (edad > 100):
        return "Relája Nosferatu."

