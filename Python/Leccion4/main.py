#Colecciones (arreglos o vectores): listas(mutables), tuplas(inmutables), set, diccionario

nombres = ["Naty", "Osvaldo", "Ariel", "Lily"]
print(nombres)
print(nombres[1])
print(nombres[2])
print(nombres[-1])
print(nombres[-2])

print(nombres[0:2])

print(nombres[ :3])

print(nombres[1: ])

#Modificamos en valor

nombres[3] = "Liliana"
nombres[0] = "Natalia"
print(nombres)

#Iterar una lista

for nombre in nombres:
    print(nombre)
else:
    print("Se acabaron los elementos")

#Cuantos elementos tiene la lista

print(len(nombres))

#Agregamos un elemento
nombres.append("Facundo")
nombres.append([1, 2, 3])
nombres.append(10.45)
nombres.append(True)
print(nombres)

#En un indice especifico

nombres.insert(1, "Gabriel")
print(nombres)

nombres.insert(3, "Giuliano")
print(nombres)

#Eliminamos
nombres.remove("Gabriel")
print(nombres)

#Eliminamos el ultimo
nombres.pop()
print(nombres)

#Eliminamos elemento especifico
del nombres[2]
print(nombres)

#Eliminar todos los elementos
nombres.clear()
print(nombres)

#Eliminar la lista
del nombres
#print(nombres)

#Definimos una tupla
cocina = ("cuchara", "cuchillo", "tenedor")
print(len(cocina))

#Acceder a un elemento

print(cocina[0])

print(cocina[-1])

#Acceder a un rango

print(cocina[0:2])

#Ejemplo

verduras = ("papa",)

for cocinar in cocina:
    print(cocinar, end=" ") #end para eliminar los saltos de linea

cocinaLista = list(cocina)
cocinaLista[0] = "Plato"
cocina = tuple(cocinaLista)
print('\n', cocina)

#del cocina
#print(cocina)

#Tipo SET
planetas = {"Marte", "Jupiter", "Venus"}
print(len(planetas)) #significa largo

#Revisar si un elemento existe o no
print("Marte" in planetas) #not

#Agregar un elemento
planetas.add("Tierra")
print(planetas)

#Eliminar elementos, puede arrojar error si no existe el elemento
planetas.remove("Jupiter") # da error
print(planetas)
planetas.discard("tierra") # no da error
print(planetas)

#Limpiar set
planetas.clear()
print(planetas)

#Eliminar set
#del planetas
#print(planetas)

#Diccionarios, una llave y un valor
# "Maradona": 10

diccionario = {
    "IDE": "Integrated Developed Environment",
    "POO": "Programacion orientada a objetos",
    "SABD": "Sistema de administracion de Base de Datos"
}
print(len(diccionario))
print(diccionario)

#Acceder a un elemento con la key
print(diccionario["IDE"])
#Otra forma
print(diccionario.get("POO"))

#Modificar un elemento
diccionario["IDE"] = "Entorno de Desarrollo Integrado"
print(diccionario)

#Recorrer los elementos
for termino in diccionario: #solo las llaves
    print(termino)
# Otra manera
for termino in diccionario.keys():
    print(termino)

#Solo los valores
for valor in diccionario.values():
    print(valor)

#funcion para recorrer el diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

#Verificar si hay un elemento o no (not in)
print("IDE" in diccionario)

#Agregar un elemento

diccionario["PK"] = "Primary key"
print(diccionario)

#Eliminar un elemento
diccionario.pop("SABD")
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Elimianr diccionario
#del diccionario
#print(diccionario)

#Concatenar una lista
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista3)
lista3.extend([7, 8, 9])
print(lista3)

print(lista3.index(5)) #ubicar en que indice esta el valor indicado

#cuantos valores repetidos hay en una lista
print(lista3.count(1))

lista3.reverse()
print(lista3)

#Para que una lista se multiplique repitiendo sus elementos
lista = [1, 2, 3] * 2
print(lista)

#Metodos de ordenamiento
lista3.sort() #ascendentemente
print(lista3)

lista3.sort(reverse=True) #descendentemente
print(lista3)

#repaso de tuplas
tupla = (4, "Hola", 6.78, [1, 2, 3, 4, 5], "Hola", 5)
print(tupla)

#buscar un elemento o no (not in)
print(4 in tupla)

#Repaso de set o conjunto
#para definir un conjunto
conjunto2 = set()
conjunto1 = {"bye", }
conjunto2.add(7)
conjunto2.add("Hola")
print(conjunto2)
conjunto1.add("Hola")
print(conjunto1)
print(3 not in conjunto1) #Preguntamos si el numero 3 no esta en el conjunto1

#igualdad de dos conjuntos

print(conjunto1 == conjunto2)

#Operaciones en conjuntos
#Union de conjuntos
conjunto3 = conjunto1 | conjunto2
print(conjunto3)

#elemento que tienen en comun
conjunto3 = conjunto1 & conjunto2
print(conjunto3)

#Asigna el valor que esta en el conjunto1 y no en el conjunto2
conjunto3 = conjunto1 - conjunto2
print(conjunto3)

conjunto3 = conjunto2 - conjunto1
print(conjunto3)

#elementos que no comparten
conjunto3 = conjunto1 ^ conjunto2
print(conjunto3)

#preguntamos si un conjunto es un subconjunto dentro de otro
conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3))
print(conjunto1.issubset(conjunto3))

#preguntamos si los elementos del conjunto1 estan dentro del conjunto3
#si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto3.issuperset(conjunto1))
print(conjunto3.issuperset(conjunto2))
print(conjunto2.issuperset(conjunto3))

#como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2))

#convertir un conjunto a totalmente inmutable
conjunto1 = frozenset

#repaso diccionarios
diccionarioNuevo = {"Azul": "Blue", "Rojo": "Red", "Verde": "Green", "Amarillo": "Yellow"}
print(diccionarioNuevo)
#como eliminar

del (diccionarioNuevo["Azul"])
print(diccionarioNuevo)

#los diccionarios pueden almacenar difierentes tipos de datos
diccionario2 = {"Facundo": {"Edad": 26, "Altura": 1.75}, "Osvaldo": [45, 1.85], "Natalia": [35, 1.67]}
print(diccionario2)

seleccionArgentina = {
    10: {"Nombre": "Lionel Messi", "Edad": 35, "Altura": 1.70, "Precio": "50 millones", "Posicion": "Enganche"},
    11: {"Nombre": "Angel Di Maria", "Edad": 34, "Altura": 1.80, "Precio": "12 millones", "Posicion": "Extremo derecho"},
    24: {"Nombre": "Paulo Dybala", "Edad": 28, "Altura": 1.77, "Precio": "35 millones", "Posicion": "Media punta"},
    19: {"Nombre": "Nicolás Otamendi", "Edad": 34, "Altura": 1.83, "Precio": "3.5 millones", "Posicion": "Defensor"},
    1: {"Nombre": "Franco armani", "Edad": 35, "Altura": 1.89, "Precio": "3.5 millones", "Posicion": "Arquero"},
    22: {"Nombre": "Lautaro Martinez", "Edad": 25, "Altura": 1.74, "Precio": "80 millones", "Posicion": "Delantero"},
    13: {"Nombre": "Cristian Romero", "Edad": 24, "Altura": 1.88, "Precio": "100 millones", "Posicion": "Defensor"},
    7: {"Nombre": "Rodrigo De Paul", "Edad": 28, "Altura": 1.80, "Precio": "25 millones", "Posicion": "Mediocampista"},
    8: {"Nombre": "Emiliano Buendia", "Edad": 25, "Altura": 1.74, "Precio": "35 millones", "Posicion": "Mediocampista"}
}
for llave, valor in seleccionArgentina.items():
    print(llave, valor)

print("Tenemos cargados en el diccionario la cantidad de jugadores: ", end=" ")
print(len(seleccionArgentina))

# pilas usando listas
pila = [1,2,3]

#agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

#sacamos elementos por el final
pila.pop()
print(pila)
#quita el ultimo elemento y lo guarda en una variable
elementoBorrado = pila.pop()
print(pila)
print(f"El elemento borrado es: {elementoBorrado}")

#colas con listas
#estructura de datos tipo fifo (first input, first output)

cola = ["Juan", "Pedro", "Fulano"]
cola.append("Mengano")
cola.append("Mengana")
print(cola)

#sacamos elementos de la cola

seRetira = cola.pop(0)
print(f"Atendido: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido: {seRetira}")
print(cola)














