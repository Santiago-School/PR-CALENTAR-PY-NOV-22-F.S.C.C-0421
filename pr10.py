print(" Fco. Santiago. Car. Cor")
print(" ")
def generarcaracteres(n, caracter):
    cadena = ""
    for _ in range(n):
        cadena += caracter
    print(f"el resultado de generar {n} veces el caracter '{caracter}' es: {cadena}")
    return cadena

# asignando valores
generarcaracteres(6, "S")  
