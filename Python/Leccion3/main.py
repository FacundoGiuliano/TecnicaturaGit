# # Ciclo while (mientras o durante)
# contador = 0
# while contador < 78:
#     print("Ejecutamos el ciclo while", contador)
#     contador += 1
# else:
#     print("Fin del ciclo while")
#
# maximo = 5
# contador = 0
# while contador <= maximo:
#     print(contador)
#     contador += 1

# minimo = 1
# contador = 5
# while contador >= minimo:
#     print(contador)
#     contador -= 1
#
# #Ciclo for
#
# cadena = "Hello"
# for letra in cadena:
#     print(letra)
# else:
#     print("Fin del ciclo for")

# for letra in "Alemania":
#     if letra == "a":
#         print(f"Letra encontrada: {letra}")
#         break
# else:
#     print("Fin del ciclo for")
#
# palabra reservada continue

for i in range(6):
    if i % 2 == 0:
        print(f"Valor: {i}")

for i in range(6):
    if i % 2 != 0:
        continue
    print(f"Valor: {i}")

