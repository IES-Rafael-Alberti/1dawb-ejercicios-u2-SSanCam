def comprobarPrimo(numero):
    import math
    mensaje = ""
    
    if (numero <= 1): 
        mensaje = "No es un número primo"
        
    elif (numero == 2):
        mensaje = "Es un número primo."
        
    elif (numero%2 == 0):
        mensaje = "No es un número primo."
        
    else:
        
        for divisor in range(3, int(math.sqrt(numero)), 2):
            if numero % divisor == 0:
                mensaje = "No es un número primo."
                
            else:
                mensaje = "Es un número primo."
                
    return mensaje 

