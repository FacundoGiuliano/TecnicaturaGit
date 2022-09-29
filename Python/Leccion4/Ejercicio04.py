# Sumar numeros pares dentro de un rango
# Hacer un programa para sumar numeros pares dentro de un rango
# Por ejemplo: suma de numeros pares del 2 al 30
#              suma = 240

inicio = int(input("Digite un numero para iniciar la suma: "))
fin = int(input("Digite un nuemro para finalizar la suma: "))
suma = 0
for i in range(inicio, fin+1):
    if i % 2 == 0:
        suma += i
print(f"\nLa suma de numeros pares dentro del rango es: {suma}")
