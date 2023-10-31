def grupo(nombre, sexo):
    inicial = (nombre[0]).upper()
    if ((inicial > "M") and (sexo.upper() == "M")) or (inicial < "N") and (sexo.upper() == "H"):
        return "Perteneces al grupo A"
    else:
        return "Perteneces al grupo B"

def main():
    
    print("Introduce tu sexo: [H]ombre, [Mujer]: ")
    sexo = str(input())
    print("Introduce tu nombre: ")
    nombre = str(input())
    
    inicial = (nombre[0]).upper()
    if ((inicial > "M") and (sexo.upper() == "M")) or (inicial < "N") and (sexo.upper() == "H"):
        print ("Perteneces al grupo A")
    else:
        print ("Perteneces al grupo B")
        
if __name__=="__main__":
    main()
    
