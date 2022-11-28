class Persona:
    def __init__(self, nombre, edad, comidasFavoritas):
        self.nombre = nombre
        self.edad = edad
        self.comidasFavoritas = comidasFavoritas

    def __add__(self, other):  # suma, otro
        return f"{self.nombre} {other.nombre} {self.comidasFavoritas} {other.comidasFavoritas}"

    def __sub__(self, otro): #  resta
        return self.edad - otro.edad


persona1 = Persona("Facundo", 27, ["manzana", "pera"])
persona2 = Persona("Giuliano", 1, ["frutilla", "ciruela"])

#  persona1.__add__(persona2) Sintaxis interna y automatica

print(persona1 + persona2)
print(persona1 - persona2)
print(persona1.comidasFavoritas + persona2.comidasFavoritas)
