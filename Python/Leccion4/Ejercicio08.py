# Ejercicio08: Menu interactico - cajero automatico
# Hacer un programa que simule un cajero automatico con un saldo inicial de $1000 y tendra
# el siguiente menu de opciones:
#     1: Ingresar dinero en la cuenta
#     2: Retirar dinero de la cuenta
#     3: Mostrar dinero disponible
#     4: Salir

saldo = 1000
while True:
    print("\t.:MENU:.")
    print("1: Ingresar dinero en la cuenta")
    print("2: Retirar dinero de la cuenta")
    print("3: Mostrar dinero disponible")
    print("4: Salir")
    opcion = int(input("Digite la opcion del menu: "))
    print()
    if opcion == 1:
        extra = float(input("Digite la cantidad de dinero a ingresar: "))
        saldo += extra
        print(f"Dinero en la cuenta al momento: ${saldo}")
    elif opcion == 2:
        retira = float(input("Digite la cantidad de dinero a retirar: "))
        if retira > saldo:
            print("No tiene esa cantidad de dinero.")
            retira = float(input("Digite nueva cantidad de dinero a retirar: "))
        else:
            saldo -= retira
            print(f"Dinero en la cuenta al momento: ${saldo}")
    elif opcion == 3:
        print(f"Dinero en la cuenta al momento: ${saldo}")
    elif opcion == 4:
        print("Gracias por utilizar el cajero automatico, hasta pronto!")
        break
    else:
        print("La opcion ingresada es incorrecta.")
        print()

