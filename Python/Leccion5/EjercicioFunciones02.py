# Crear una funcion para multiplicar los valores recibidos de tipo numerico,
# utilizando argumentos variables *args como parametro de la funcion y regresar como
# resultado la multiplicacion  de todos los valores pasados como argumento.

def multiplica(*args):
    resultado = 1
    for i in args:
        resultado *= i
    return resultado

print(multiplica(3, 5, 15))
