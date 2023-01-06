from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

teclado1 = Teclado("HP", "USB")
monitor1 = Monitor("HP", "15")
raton1 = Raton("HP", "USB")
computadora1 = Computadora("HP", monitor1, teclado1, raton1)

teclado2 = Teclado("Acer", "Bluetooth")
monitor2 = Monitor("Acer", "27")
raton2 = Raton("Acer", "Bluetooth")
computadora2 = Computadora("Acer", monitor2, teclado2, raton2)

teclado3 = Teclado("HP", "USB")
monitor3 = Monitor("HP", "15")
raton3 = Raton("HP", "USB")
computadora3 = Computadora("HP", monitor3, teclado3, raton3)

teclado4 = Teclado("Acer", "Bluetooth")
monitor4 = Monitor("Acer", "27")
raton4 = Raton("Acer", "Bluetooth")
computadora4 = Computadora("Acer", monitor4, teclado4, raton4)

computadora5 = Computadora("Samsung", monitor1, teclado2, raton3)
computadora6 = Computadora("Gamer", monitor2, teclado3, raton4)

computadoras1 = [computadora1, computadora2, computadora5]
orden1 = Orden(computadoras1)
orden1.agregar_computadora(computadora3)
print(orden1)

computadoras2 = [computadora3, computadora4, computadora6]
orden2 = Orden(computadoras2)
orden2.agregar_computadora(computadora2)
print(orden2)

