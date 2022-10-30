class Vehiculo:
    """
    Definir una clase padre llamada vehiculo y dos clases hijas llamadas
    Auto y Bicileta, als cuales heredan de la clase padre Vehiculo. La clase
    padre debe tener los siguientes atributos y metodos:
    Vehiculo (clase padre)
    -Atributos (color, ruedas)
    -Metodos ( __init__(color, ruedas) y __str__() )

    Auto (clase hija de vehiculo)
    -Atributos(velocidad (km/hr) )
    -Metodos ( __init__(color, ruedas, velocidad) y __str__() )

    Bicicleta (clase hija de vehiculo)
    -Atributos ( tipo(urbana/montaña/etc) )
    -Metodos ( __init__(color, ruedas, tipo) y __str__() )

    Crear un objeto de cada clase

    """
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color: "+self.color+", Ruedas: "+ str(self.ruedas)

class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__()+", Velocidad(km/hr):  "+ str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__()+", Tipo: "+self.tipo

vehiculo = Vehiculo("Negro", 4)
print(vehiculo)

auto = Auto("Blanco", 4, 120)
print(auto)

bici = Bicicleta("Azul", 2, "Montaña")
print(bici)
