class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}")

    @property  # decorador
    def nombre(self):  # Metodo Getter
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Metodo Setter
        self._nombre = nombre

    @property  # decorador
    def apellido(self):  # Metodo Getter
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):  # Metodo Setter
        self._apellido = apellido

    @property  # decorador
    def edad(self):  # Metodo Getter
        return self._edad

    @edad.setter
    def edad(self, edad):  # Metodo Setter
        self._edad = edad

    def __del__(self):
        print(f"Persona2: {self._nombre} {self._apellido} {self._edad}")

if __name__ == "__main__":
    persona1 = Persona2("Facundo", "Giuliano", 26)
    print(persona1.nombre)  # Llamamos al metodo getter
    persona1.nombre = "Juan Pedro" #  Llamamos el metodo setter
    print(persona1.nombre) #  getter
    print(persona1.mostrar_detalles()) #  Metodo mostrar detalles
    #  Atributo read only (solo lectura) seria la edad porque no tiene el metodo set
    print(persona1.edad)

    #  Tarea: crear tres objetos mas, utilizando los metodos seter y geter y mostrar detalles

    persona2 = Persona2("Ariel", "Betancud", 41)
    persona3 = Persona2("Homero", "Simpson", 40)
    persona4 = Persona2("Marge", "Bouvier", 36)

    print(persona2.mostrar_detalles())
    print(persona3.mostrar_detalles())
    print(persona4.mostrar_detalles())

    persona2.nombre = "Bart"
    persona2.apellido = "Simpson"
    persona2.edad = 10
    persona3.nombre = "Lisa"
    persona3.apellido = "Simpson"
    persona3.edad = 8
    persona4.nombre = "Maggy"
    persona4.apellido = "Simpson"
    persona4.edad = 2
    print(persona2.mostrar_detalles())
    print(persona3.mostrar_detalles())
    print(persona4.mostrar_detalles())

    print(__name__)
