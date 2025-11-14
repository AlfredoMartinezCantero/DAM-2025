'''
(c) Programa realizado por Alfredo Martínez Cantero, 2025, para mostrar una factura con IVA y un descuento fijo bajo unas condiciones.
'''
IVA = 0.21           
DESCUENTO = 10.0     
nombre_cliente = input("Nombre: ")
precio_bruto = float(input("Precio bruto: "))
iva_aplicado = precio_bruto * IVA
subtotal_con_iva = precio_bruto + iva_aplicado
descuento_aplicado = precio_bruto 

if precio_bruto >= 50:
    descuento_aplicado = DESCUENTO
    print("Descuento fijo de 10€ aplicado.")

else:
    descuento_aplicado = 0.0

pago_total = subtotal_con_iva - descuento_aplicado

print("------ FACTURA ------")
print("Nombre:", nombre_cliente)
print("Precio bruto:", precio_bruto)
print("IVA (21%):", iva_aplicado)
print("Descuento aplicado:", descuento_aplicado)
print("Total a pagar:", pago_total)
print("----------------------")
print("----------------------")
print("----------------------")







