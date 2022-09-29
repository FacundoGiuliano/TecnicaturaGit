# Llenar una lista con numeros del 1 al 10, luego modificar los elementos
# de la lista multiplicandolos por un valor ingresado por el usuario

lista = list(range(1, 11))
# numero = int(input("Digite un numero: "))
#
# for i in lista:
#     print(f"{numero} x {i} = {numero * i}")

print("Lista original")
for i in lista:
    print(i, end="-")
valor = int(input("\nDigite un numero a multiplicar: "))
for indice, i in enumerate(lista): #Funcion para modificar los indices de la lista
    lista[indice] *= valor

print(f"Lista final con los elementos multiplicados por {valor}")
for i in lista:
    print(i, end="-")




