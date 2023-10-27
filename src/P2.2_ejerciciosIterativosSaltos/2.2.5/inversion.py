def capitalObtenido(cantInvertir, interes, numTiempo):
    interes = interes / 100
    
    for annios in range(1, numTiempo + 1):
        cantInvertir *= 1 + interes

    return "{:.2f}€".format(cantInvertir)

print(capitalObtenido(1500, 20, 5))
