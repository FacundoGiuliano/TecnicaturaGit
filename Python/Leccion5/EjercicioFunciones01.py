# Crear una funcion para suma los valores de tipo numericos, utilizando argumentos variables *args
# como parametros de la funcion y agregar como resultado la suma de todos los valores pasados como argumentos

def sumar_valor(*args):  # Recibimos ua cantidad de parametros indefinidos
    resultado = 0
    # Iteramos cada elemento
    for valor in args:
        resultado += valor
    return resultado


# Llamamos a la funcion
print(sumar_valor(3, 5, 9, 2, 1))
