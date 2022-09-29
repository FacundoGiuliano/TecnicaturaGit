# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes:
# Nombre: Aragon
# Clase: Guerrero
# Raza: Dunadan del norte
#
# Nombre: Gandalf
# Clase: Mago
# Raza: Istar
#
# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

personajes = []

p = {"Nombre": "Aragon", "Clase": "Guerrero", "Raza": "Dunadan del norte"}
personajes.append(p)
p = {"Nombre": "Gandalf", "Clase": "Mago", "Raza": "Istar"}
personajes.append(p)
p = {"Nombre": "Legolas", "Clase": "Arquero", "Raza": "Elfo Sindar"}
personajes.append(p)
p = {"Nombre": "Damrod", "Clase": "Soldado", "Raza": "Dunedain del sur"}
personajes.append(p)
p = {"Nombre": "Gimli", "Clase": "clan de Durin", "Raza": "Enano"}
personajes.append(p)
p = {"Nombre": "Glorfindel", "Clase": "clan de Noldor", "Raza": "Elfo"}
personajes.append(p)
print(personajes)
