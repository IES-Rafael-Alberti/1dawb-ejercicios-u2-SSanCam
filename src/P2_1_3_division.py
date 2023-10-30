def op_division (numero1, numero2):
    
    if (numero2 == 0):
        return "Error. No puede dividirse entre 0."
    else:
        division = numero1 / numero2
        division_formateada = "{:.2f}".format(division)
        return division_formateada
        

def main():
    numero1 = 10
    numero2 = 5
    
    if "2.00" == op_division(numero1, numero2):
        print("Operación correcta.")
    
if __name__=="__main__":
    main()