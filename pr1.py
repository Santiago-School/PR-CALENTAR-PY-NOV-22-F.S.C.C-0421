print(" Fco. Santiago. Car. Cor")
print(" ")
#con esto se aplica para saber cual es mayor o menor
def maximo(a, b):
    if a > b:
        print(f"l mayor entre {a} y {b} es {a}")
        return a
    else:
        print(f"l mayor entre {a} y {b} es {b}")
        return b

# signando valores
valor1 = 5
valor2 = 10
maximo(valor1, valor2)  # dira el mayor entre 5 y 10 es 10
