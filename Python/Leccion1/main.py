# """
# miVariable = 3
# print(miVariable)
# miVariable = "Hola a todos los estudiantes"
# print(miVariable)
# miVariable = 3.5
# print(miVariable)
# x = 10
# y = 2
# z = x + y
# print(id(x))
# # Las literales se escriben x624
# print(id(y))
# print(id(z))
#
# a: str = "Hola alumnos"
# print(type(a))
#
# a = True
# print(type(a))
#
# # Tipos: int, float, String, Bool
# x = 10
# print(x)
# print(type(x))
# x = 14.5
# print(x)
# print(type(x))
# x = "Hola alumnos"
# print(x)
# print(type(x))
# x = True
# print(x)
# print(type(x))
# x = False
# print(x)
# print(type(x))
#
# #Manejo de cadenas ( String)
# miGrupoFavorito = "AC/DC:"
# caracteristicas = "The best rock band"
# print("Mi grupo favorito es: "+miGrupoFavorito+" "+caracteristicas)
# print("Mi grupo favorito es:", miGrupoFavorito, caracteristicas)
#
# #numero1 = "7"
# #numero2 = "8"
# #print(int(numero1) + int(numero2))
#
# # Tipos de datos booleanos (bool)
# miBooleano = 3 > 2
# print(miBooleano)
#
# if miBooleano:
#     print("El resultado es verdadero")
# else:
#     print("El resultado es falso")
#
# # Procesar la entrada del usuario (funcion input)
# # resultado = input("Digite un numero: ")  # Regresa un dato tipo string
# # print(resultado)
#
# # Conversion de la entrada de datos
# numero1 = int(input("Escribe el primer numero: "))
# numero2 = int(input("Escribe el segundo numero: "))
# resultado = numero1 + numero2
# print("El resultado de la suma es: ", resultado)
#
# operandoA = 8
# operandoB = 5
#
# suma = operandoA + operandoB
# # print("El resultado de la suma: ", suma)
# print(f"El resultado de la suma es: {suma}")
#
# resta = operandoA - operandoB
# print(f"El resultado de la resta es: {resta}")
#
# multiplicacion = operandoA * operandoB
# print(f"El resultado de la multiplicacion es: {multiplicacion}")
#
# division = operandoA / operandoB
# print(f"El resultado es: {division}")
#
# division = operandoA // operandoB  # int
# print(f"El resultado es: {division}")
#
# modulo = operandoA % operandoB
# print(f"El resultado o residuo es: {modulo}")
#
# exponente = operandoA ** operandoB
# print(f"El resultado es: {exponente}")
#
# alto = int(input("Digite el alto del rectangulo: "))
# ancho = int(input("Ahora digite el ancho del rectangulo: "))
# print(f"El area del rectangulo es {alto * ancho} y el perimetro {(alto + ancho) * 2}" )
#
# alto = int(input("Digite el alto del rectangulo: "))
# ancho = int(input("Ahora digite el ancho del rectangulo: "))
# area = alto * ancho
# perimetro = (alto + ancho) * 2
# print("Area: ", area)
# print("Perimetro: ", perimetro)
#
# miVariable3 = 10
# print(miVariable3)
#
# # Operadores de reasignacion
# miVariable3 = miVariable3 + 1
# print(miVariable3)
#
# miVariable3 += 1
# print(miVariable3)
#
# # miVariable3 = miVariable3 - 2
# miVariable3 -= 2
# print(miVariable3)
#
# # miVariable3 = miVariable3 * 3
# miVariable3 *= 3
# print(miVariable3)
#
# # miVariable3 = miVariable3 / 2
# miVariable3 /= 2
# print(miVariable3)
#
# # Operadores de comparacion
#
# d = 4
# b = 2
# resultado = d == b  # Comprobamos si son iguales
# print(resultado)
#
# resultado = d != b  # diferentes
# print(resultado)
#
# resultado = d > b  # mayor que
# print(resultado)
#
# resultado = d < b  # menor que
# print(resultado)
#
# resultado = d <= b  # menor o igual que
# print(resultado)
#
# resultado = d >= b  # mayor o igual que
# print(resultado)
#
# Ejercicio 1:
#
# num = int(input("Digite un numero: "))
# print(f"El residuo de la division es: {num % 2}")
# if num % 2 == 0:
#     print(f"El numero ingresado: {num} es par")
# else:
#     print("El numero ingresado es impar")
#
# Ejercicio 2:
#
# edad = int(input("Ingrese su edad: "))
# if edad >= 18:
#     print("Eres mayor de edad")
# else:
#     print("Eres menor de edad")
#
# #Operadores Logicos
#
# a = True
# b = True
# resultado = a and b
# print(resultado)
#
# resultado = a or b
# print(resultado)
#
# resultado = not a
# print(resultado)
#
# #Ejercicio:valor dentro de un rango
#
# num = int((input("Digite un numero:")))
# if num >= 0 and num <= 5:
#     print(f"El valor {num} se encuentra dentro del rango")
# else:
#     print(f"El valor {num} esta fuera del rango")
#
# # Ejercicio con el operador or, operador not
#
# vacaciones = False
# diaDescanso = True
# if not (vacaciones or diaDescanso):
#     print("Puede asistir al juego")
# else:
#     print("Tiene trabajo que hacer")
#
# #Ejercicio: Rango entre las edades 20 y 30 años
#
# edad = int(input("Digite su edad: "))
# if edad >= 20 and edad < 30 or edad >= 30 and edad <40:
#     print(f"La edad ingresada: {edad} se encuentra dentro del rango")
# else:
#     print(f"La edad ingresada: {edad} no esta dentro del rango")
#
# edad = int(input("Digite su edad: "))
# #veinte = edad >= 20 and edad < 30
# #print(veinte)
# #treinta = edad >= 30 and edad < 40
# #print(treinta)
#
# #if veinte or treinta:
# #    if veinte:
# #        print("Estas dentro del rango de los 20's años")
# #    elif treinta:
# #        print("Estas dentro del rango de los 30's años")
# #    else:
# #        print("No estas dentro del rango de 20's ni 30's años")
# #else:
# #    print("No estas dentro del rango")
# #Sintaxis simplificada
# if (20 <= edad < 30) or (30 <= edad < 40):
#     print(f"La edad ingresada: {edad} se encuentra dentro del rango")
# else:
#     print(f"La edad ingresada: {edad} no esta dentro del rango")
#
# #Ejercicio: El mayor de dos numeros
#
# num1 = int(input("Digite el valor para el numero1: "))
# num2 = int(input("Digite el valor para el numero2: "))
# if num1 > num2:
#     print("El numero1 es el mayor")
# else:
#     print("El numero2 es el mayor")
#
# #Ejercicio: tienda de libros
# print("Ingrese los siguientes datos del libro: ")
# nombre = input("Nombre del libro: ")
# idLibro = input("ID: ")
# precio = input("Precio: ")
# envio = input("Indique si el envio es gratuito (True/False): ")
# if envio == "True":
#     envio = True
# elif envio == "False":
#     envio = False
# else:
#     envio = "El valor ingresado es incorrecto"
# print(f'''
#         Nombre: {nombre}
#         ID: {idLibro}
#         Precio: {precio}
#         Envio Gratuito?: {envio}







