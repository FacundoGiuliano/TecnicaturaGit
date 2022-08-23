i = 0
neutro = 0
positivos = 0
negativos = 0
for i in range(10):
    num = int(input("Digite un numero: "))
    if num == 0:
        neutro += 1
    elif num > 0:
        positivos += 1
    else:
        negativos += 1
print(f"Cantidad de numeros neutros: {neutro}")
print(f"Cantidad de numeros positivos: {positivos}")
print(f"Cantidad de numeros negativos: {negativos}")

