print(" Fco. Santiago. Car. Cor")
print(" ")
def maxtres(x, y, z):
    if x > y:
        if x > z:
            print(f"el mayor entre {x}, {y} y {z} es {x}")
            return x
        else:
            print(f"el mayor entre {x}, {y} y {z} es {z}")
            return z
    else:
        if y > z:
            print(f"el mayor entre {x}, {y} y {z} es {y}")
            return y
        else:
            print(f"el mayor entre {x}, {y} y {z} es {z}")
            return z

# asignando valores
valor1 = 2
valor2 = 6
valor3 = 4
maxtres(valor1, valor2, valor3)  
