print(" Fco. Santiago. Car. Cor")
print(" ")
def inversa(cadena):
    lomismoperoalreves = ""
    for i in range(len(cadena) - 1, -1, -1):
        lomismoperoalreves += cadena[i]
    print(f"La inversión de la cadena '{cadena}' es '{lomismoperoalreves}'")
    return lomismoperoalreves

# Asignando valores
micadena = "Vamos al Hong Kong profe pero en fa"
inversa(micadena)  
