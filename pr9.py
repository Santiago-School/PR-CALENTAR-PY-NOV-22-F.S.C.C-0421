print(" Fco. Santiago. Car. Cor")
print(" ")
def superposicion(lista1, lista2):
    for item1 in lista1:
        for item2 in lista2:
            if item1 == item2:
                print(f"las listas tienen al menos un miembro en comun: {item1}")
                return True
    print("las listas no tienen elementos en comun")
    return False

# asignando valores
lista1 = [1, 6, 3]
lista2 = [3, 3, 9]
superposicion(lista1, lista2)  
