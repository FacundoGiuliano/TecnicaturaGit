i = 1
factorial = 1
num = int(input("Digite un numero: "))
while num >= 0:
    while i <= num:
        factorial *= i
        i += 1
    else:
        print(f"El factorial es: {factorial}")
        break
else:
    num = int(input("Digite un numero: "))
