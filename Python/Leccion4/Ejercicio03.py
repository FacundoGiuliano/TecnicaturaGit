# Pedir numeros e insertarlos en una lista, cuando el usuario introduzca
# un numero 0, nuestro programa dejaria de insertar. Por ultimo
# mostrar los numeros ordenados de menor a mayor.

lista = []
salir = False
while not salir:
    numero = int(input("Digite un numero: "))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort() #lista ordenada de menor a mayor
print(f"\nLista ordenada: \n{lista}")
