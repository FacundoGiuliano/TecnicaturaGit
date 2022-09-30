# Realizar un juego para adivinar un numero. Para ello se debe generar un numero aleatorio
# entre 1 y 100, y luego ir pidiendo numeros indicando "es mayor" o "es menor" segun sea mayor o menor
# con respecto a N. El proceso termina cuando el usario acierta y alli se debe mostrar el numero de intentos.



import random
print("\t.:Juego adivina el numero:.")
aleatorio = random.randint(0, 100)
contador = 0
print(aleatorio)
numero = int(input("Digite un numero: "))
while numero != aleatorio:
    contador += 1
    if numero < aleatorio:
        numero = int(input("Digite un numero MAYOR: "))
    else:
        numero = int(input("Digite un numero MENOR: "))
print("Felicitaciones, HA GANADO!")
print(f"Cantidad de intentos fallidos: {contador}")





