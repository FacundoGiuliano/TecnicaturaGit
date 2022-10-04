# No repetir caracteres
# Hacer un programa que pida una cadena por teclado, luego meter los caracteres en una lista sin repetirlos.

cadena = input("Digite una cadena: ")
lista = []
for i in cadena:
    if i not in lista: # Si el caracter aun no esta en la lista...
        lista.append(i) # Lo agregamos a la lista
print(f"\nCadena sin repetir caracteres:\n {lista}")

lista = list(set(input("Ingrese una cadena: ")))
print(f"\nCadena sin repetir caracteres:\n {lista}")
