from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    #  print(objeto)  # de manera indirecta llamamos al str de la clase empleado o gerente
    print(type(objeto))  # tipo de dato que recibe
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente): #  Si el objeto que estamos recibiendo es de la clase gerente
        print(objeto.departamento)


empleado = Empleado("Facundo", 150000)
imprimir_detalles(empleado)

gerente = Gerente("Ariel", 50000, "Sistemas")
imprimir_detalles(gerente)
