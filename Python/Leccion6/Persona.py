class Persona: # Creamos una clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): # Metodo init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self): # self es igual a this en java
        print(f"La clase Persona tiene lo siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la direccion es: {self.args}, los datos importantes son: {self.kwargs}")



persona1 = Persona("Facundo", "Giuliano", 23132123132, 26)
print(f"El objeto 1 de la clase persona: {persona1.nombre} {persona1.apellido} {persona1.edad}")
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)

persona2 = Persona("Ariel", "Betancud", 123123132, 40)
print(f"El objeto 2 de la clase persona: {persona2.nombre} {persona2.apellido} {persona2.edad}")

persona1.nombre = "Liliana"
persona1.apellido = "Bucella"
persona1.edad = 40

print(f"El objeto 1 de la clase persona: {persona1.nombre} {persona1.apellido} {persona1.edad}")

# Los atributos son las caracteristicas
# Los metodos son el comportamiento que van a tener los objetos (acciones)

persona1.mostrar_detalle() # En este caso la referencia se pasa de manera automatica
persona2.mostrar_detalle()

# Persona.mostrar_detalle() Debemos pasarle uan referencia al self para que no de error

persona1.telefono = 12314564 # Hemos creado un atributo de un objeto (persona1)
print(persona1.telefono)

persona3 = Persona("Rogelio", "Romero", 465465456, 22, "Telefono", "132465456", "Calle Lopez", 823, "Manzana", 77, "Casa", 18, Altura=1.83, Peso=78, Cfavorito="Azul", Auto="Citroen", Modelo=2021)
persona3.mostrar_detalle()

# print(persona3._dni)  Esto no se debe utilizar(esta encapsulado), desconocemos python
# persona3.__nombre # Esta totalmente encapsulado


