# Funcion recursiva: imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
# Puede ser cualquier valor positivo, por ejemplo si pasamos el valor de 5, debe imprimir
# 5
# 4
# 3
# 2
# 1
# En caso de ser el numero 3 debe imprimir:
# 3
# 2
# 1
# Si se ingresan numeros negativos no imprime nada

def imprimeNumerosDesendentes(numero):
    if numero >= 1: # caso base
        print(numero)
        imprimeNumerosDesendentes(numero-1) # caso recursivo
    elif numero == 0:
        return
    elif numero <= 0:
        print("Valor ingresado incorrecto...")

imprimeNumerosDesendentes(int(input("Digite un numero: ")))
