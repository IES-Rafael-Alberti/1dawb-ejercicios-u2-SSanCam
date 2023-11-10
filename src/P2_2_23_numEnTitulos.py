"""Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). 
Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. 
Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). 
Finalmente, informar cuántas líneas completas se ingresaron."""

def cont_num_titulos(titulo: str) -> str:
    
    digitos = "1234567890"
    total_digitos = 0
    linea = 0

    while (titulo != "/"):
        for numero in titulo:
            if numero in digitos:
                total_digitos += 1
        titulo = str(input("Título: "))   
        linea += 1
    if (total_digitos == 1):
        num = "número"
    else: 
        num = "números"
        
    resultado = f"En {linea} títulos de libros, se ha detectado: {total_digitos} {num}."

    return resultado



def main():
    
    print("Ingresa el titulo de un libro o introduce \'/\'")
    titulo = str(input("Título: "))
    
    resultado = cont_num_titulos(titulo)
    
    return print(resultado)
    
if __name__=="__main__":
    main()