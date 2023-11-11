def multiplicacion (numero):
    
    multiplo = 1
    tabla = ""
    
    for resultado in range(1,11):
        resultado = (numero*multiplo)
        tabla = tabla + f"{numero} x {multiplo} = {resultado}\n"
        multiplo += 1
        
    return tabla

#####___MAIN___#####

def main():
    
    print("Introduce el número del que quieras ver su tabla de multiplicar: ")
    numero = int(input())
    
    resultado = print(multiplicacion(numero))
    
    return resultado

if __name__=="__main__":
    main()