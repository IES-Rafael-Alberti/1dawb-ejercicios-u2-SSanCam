"""Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1"""
def trianguloRegresivo(niveles):
    nivel = 1
    
    while (nivel != niveles):
        for numero in range(niveles, 1, -2):
            print(str(numero) + " ")
            nivel += 1

print(trianguloRegresivo(5))