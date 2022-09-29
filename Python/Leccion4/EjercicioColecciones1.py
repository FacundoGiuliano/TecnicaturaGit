# Ejercicio1: Eliminar duplicados de una lista, por ultimo mostrar la lista

lista = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, "Facundo", "Facundo"]
# conjunto = set(lista)
# lista = list(conjunto)
lista = list(set(lista))
print(lista)

