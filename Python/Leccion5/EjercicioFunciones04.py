# Calculadora de impuestos
# Crear una funcion para calcular el total de un pago incluyendo el IVA
# pago_total = pago_sin_impuesto + pago_sin_impuesto * impuesto/100
# Proporcione el pago sin impuesto: 1000
# Proporsione el monto del impuesto: 21%
# Pago con impuesto: xxx

def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * impuesto/100
    return pago_total

pago_sin_impuesto= float(input("Digite el pago sin impuestos: "))
impuesto = float(input("Digite el monto del impuesto a aplicar: "))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f"El pago con impuesto es: {pago_con_impuesto}")



