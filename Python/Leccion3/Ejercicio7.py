i = 1
suma = 0
while i <= 5:
    print(f"Salario del empleado {i}: ")
    horas = int(input(f"Digite las horas trabajadas: "))
    tarifa = int(input("Digite la tarifa por hora: "))
    salario = horas * tarifa
    print(f"El salario es: ${salario}")
    suma = suma + salario
    i += 1
else:
    print(f"La suma de todos los salarios es: {suma}")
