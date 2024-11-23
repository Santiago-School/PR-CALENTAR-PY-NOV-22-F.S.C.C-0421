print(" Fco. Santiago. Car. Cor")
print(" ")
def longitud(listacadena):
    contador = 0
    for _ in listacadena:
        contador += 1
    print(f"la longitud de la entrada es: {contador}")
    return contador

# asignando valores
milista = [1, 2, 3, 4, 5]
longitud(milista)  # la longitud de la entrada es: 5
