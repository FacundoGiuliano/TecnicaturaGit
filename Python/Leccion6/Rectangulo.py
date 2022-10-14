class Rectangulo:
    """
    Crear una clase llamada rectangulo, debe tener 2 atrubutos: altura y base.
    El nombre del metodo sera calcular_area utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresadas por el
    usuario y los objetos deben ser tres.
    """
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.base * self.altura


altura = int(input("Digite la altura del primer rectangulo: "))
base = int(input("Digite la base del primer rectangulo: "))
rectangulo1 = Rectangulo(altura, base)
print(f"El area del primer rectangulo es: {rectangulo1.calcular_area()}")

altura = int(input("\nDigite la altura del segundo rectangulo: "))
base = int(input("Digite la base del segundo rectangulo: "))
rectangulo2 = Rectangulo(altura, base)
print(f"El area del segundo rectangulo es: {rectangulo2.calcular_area()}")

altura = int(input("\nDigite la altura del tercer rectangulo: "))
base = int(input("Digite la base del tercer rectangulo: "))
rectangulo3 = Rectangulo(altura, base)
print(f"El area del tercer rectangulo es: {rectangulo3.calcular_area()}")




