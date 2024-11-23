print(" Fco. Santiago. Car. Cor")
print(" ")
def esvocal(caracter):
    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
        print(f"el caracter '{caracter}' es una vocal")
        return True
    else:
        print(f"el caracter '{caracter}' no es una vocal")
        return False

# asignando valores
micaracter = "s"
esvocal(micaracter)  
