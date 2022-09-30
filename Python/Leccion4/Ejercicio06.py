# Tabla de Multiplicar
# Hacer un programa que pida un numero por teclado y guarde en una lista su tabla de multiplicar
# hasta el 10. Por ejemplo, si digita el numero 5 la lista tendra: 5,10,15,20,25,30,35,40,45,50

lista = []
numero = int(input("Digite un numero: "))
for i in range(1, 11): #Funcion para modificar los indices de la lista
    lista.append(i * numero)
print(f"\nTabla de multiplicar del {numero}: \n {lista}")

