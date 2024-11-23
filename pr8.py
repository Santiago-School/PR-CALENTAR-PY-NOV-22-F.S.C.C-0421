print(" Fco. Santiago. Car. Cor")
print(" ")
def espalindromo(palabra):
    lomismoperoalreves = ""
    for i in range(len(palabra) - 1, -1, -1):
        lomismoperoalreves += palabra[i]
    if palabra == lomismoperoalreves:
        print(f"La palabra '{palabra}' es un palindromo")
        return True
    else:
        print(f"la palabra '{palabra}' no es un palindromo")
        return False

# asignando valores
mipalabra = "OSO"
espalindromo(mipalabra)  
