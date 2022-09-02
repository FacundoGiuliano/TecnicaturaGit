tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []
for lista in tupla:
    if lista < 5:
        print(lista)

lista2 = []
for elemento in tupla:
    if elemento < 5:
        lista2.append(elemento)
print(lista2)