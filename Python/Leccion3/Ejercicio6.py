i = 1
suma_pares = 0
conteo_pares = 0
suma_impares = 0
conteo_impares = 0
n_elementos = int(input("Digite la cantidad de numeros enteros a ingresar: "))
while i <= n_elementos:
    num = int(input(f"{i}. Digite un numero: "))
    if num % 2 == 0:
        suma_pares += num
        conteo_pares += 1
    else:
        suma_impares += num
        conteo_impares += 1
    i += 1
else:
    if conteo_pares == 0:
        print("No se han encontrado numeros pares.")
    elif conteo_impares == 0:
        print("No se han encontrado numeros impares.")
    else:
        print(f"La suma de los numeros pares es: {suma_pares}")
        print(f"El conteo de los numeros pares es: {conteo_pares}")
        promedio_impares = suma_impares/conteo_impares
        print(f"El promedio de impares es: {promedio_impares}")
