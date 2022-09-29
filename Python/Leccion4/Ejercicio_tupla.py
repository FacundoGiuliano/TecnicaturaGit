import math # Para utilizar la funcion sqrt (raiz cuadrada)
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

# Ejercicio: Sacar la razi cuadrada de un numero positivo
numero = int(input("Ingrese un numero positivo: "))
while numero < 0:
    print("El numero ingresado no es positivo")
    numero = int(input("Ingrese un numero positivo: "))
print(f"\nSu raiz cuadrada es: {math.sqrt(numero):.2f}")


