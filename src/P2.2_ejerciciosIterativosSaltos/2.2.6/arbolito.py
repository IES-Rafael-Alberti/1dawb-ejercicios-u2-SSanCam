def piramide(numero):
    cont = 1
    while (cont <= numero):
        nivel = "*" * cont 
        print (nivel)
        cont += 1
        

print(piramide(7))