opcion = "1"
while opcion == "1":
    num = int(input("Ingrese un año para comprobar si es bisciesto o no: "))
    if ((num % 4 == 0) and (num % 100 != 0) or num % 400 == 0):
        print("El año es bisciesto.")
    else:
        print("El año NO es bisciesto.")
    opcion = input("Para continuar con otro año digite el numero '1': ")








