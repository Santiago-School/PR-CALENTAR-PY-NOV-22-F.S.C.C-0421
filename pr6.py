print(" Fco. Santiago. Car. Cor")
print(" ")

def multiplicacion(lista):
    total = 1
    for numero in lista:
        total *= numero
    print(f"ll producto de los numeros en la lista {lista} es {total}")
    return total

# asignando valores
milista = [2, 4, 6, 8]
multiplicacion(milista)  
