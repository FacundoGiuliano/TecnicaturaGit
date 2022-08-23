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
print(nombres)