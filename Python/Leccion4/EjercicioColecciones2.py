# Ejercicio 2:
# Escriba un programa que tenga 2 listas y que a continuacion cree
# las siguientes listas(no debe haber repeticion)
# 1 Lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 Lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 Lista de palabras que aparecen en ambas listas

Lista1 = [1, 2, 3, 4, 5, 4, 3, 2, 2, 1, 5]
Lista2 = [4, 5, 6, 7, 8, 4, 5, 6, 7, 7, 8]
Lista_1 = list(set(Lista1 + Lista2))
print(f"Lista 1: {Lista_1}")

Lista_2 = set(Lista1) - set(Lista2)
Lista_2 = list(Lista_2)
print(f"Lista 2: {Lista_2}")

Lista_3 = set(Lista2) - set(Lista1)
Lista_3 = list(Lista_3)
print(f"Lista 3: {Lista_3}")

Lista_4 = set(Lista1) & set(Lista2)
Lista_4 = list(Lista_4)
print(f"Lista 4: {Lista_4}")
