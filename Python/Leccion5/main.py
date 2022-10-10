# Comenzamos con funciones
# mi_funcion() #No se puede llamar a una funcion antes de definirla
def mi_funcion():
    print("Saludos a todos los profes de la Tecnicatura")

mi_funcion() # Llamamos a la funcion
mi_funcion() # Se puede llamar a una funcion N cantidad de veces
mi_funcion()

# Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+ " "+lastName)
person = ["Facundo", "Giuliano"]
show(person[0], person[1]) # Pasamos uno por uno los datos de la lista a la funcion
show(*person) # Lo pasamos todo junto
person2 = ("Ariel", "Betancud") # Desempaquetamos una tupla
show(*person2)
person3 = {"lastName": "Lucero", "name": "Naty"}
show(**person3)

# Repaso for else
numbers = [1, 2, 3, 4, 5] # Aun con la lista vacia se ejecuta el else
for n in numbers:
    print(n)
    if n == 3:
        break # Esta es la unica manera para que no se ejecute el else
else:
    print("Esto se termino")

# List comprehension, lista de comprension
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == "P"] # Regresa una nueva lista
print(alongP)
print(names)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "belgium"},
           ]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

# Paso de argumentos (funciones)
def mi_funcion2(name, lastName): # PARAMETROS
    print("Saludos a todos los que ven a traves del canal de Youtube")
    print(f"Nombe: {name}, Apellido: {lastName}")
mi_funcion2("Jorge", "Lucero") # ARGUMENTOS
mi_funcion2("Analia", "Pedroza")
mi_funcion2("Ariel", "Betancud")

# La palabra return en funciones
# Creamos una funcion para sumar
def sumar(a, b):
    return a + b
# resultado = sumar(78, 22)
# print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar(78, 22)}")

# Valores por default en los parametros de una funcion
def sumar2(a = 0, b = 0): # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f"El resultado es: {resultado}")
print(f"El resultado de la suma es: {sumar2(22, 66)}")

# Argumentos, variables en funciones
# Cuando no sabemos la cantidad de argumentos
def listarNombres(*nombres):   # Normalmente se ultiliza: (*args)
    for nombre in nombres: # Se convierte en una tupla
        print(nombre)
listarNombres("Lucas", "Ramiro", "Violeta", "Celeste")
listarNombres("Ezequiel", "Julieta", "Alan", "Marcos")

# Argumentos variables para un diccionario
def listarTerminos(**terminos): # kwargs Lo mas utilizado es kwargs para recibir los argumentos
    for llave, valor in terminos.items(): # key word argument
        print(f"{llave} : {valor}")

listarTerminos() # Nada se va a mostrar
listarTerminos(IDE="Integrated Development Enviroment", PK="Primary Key")
listarTerminos(Nombre="Lionel Messi")

# Lista de elementos con funciones (convertir)

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ["Tito", "Pedro", "Carlos"]
desplegarNombres(nombres2)
desplegarNombres("Carla")
# desplegarNombres(10, 11) No es un objero iterable
desplegarNombres((10,)) # La convertimos en una tupla, un solo elemento no olvidar la coma
desplegarNombres([22, 55]) # La convertimos en una lista

# Funciones recursivas
def factorial(numero):
    if numero == 1: # caso base
        return 1
    else:
        return numero * factorial(numero-1) # caso recursivo
numeroFactorial = int(input("Digite el numero para calcular el factorial: "))
resultado = factorial(numeroFactorial) # lo hacemos en codigo duro
print(f"El factorial de {numeroFactorial} es: {resultado}")

















