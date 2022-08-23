i = 0
nota_baja = 9999
suma = 0
for i in range(10):
    nota = int(input("Digite una calificacion: "))
    suma += nota
    if nota < nota_baja:
        nota_baja = nota
promedio = suma / 10
print(f"El promedio de notas es: {promedio}")
print(f"La nota mas baja es: {nota_baja}")


