base_imponible = 0
total_iva = 0
total_factura = 0

base_imponible = float(input("Base imponible de tu factura: "))
total_iva = base_imponible*0.21

total_factura = base_imponible + total_iva

print("base imponible:",base_imponible)
print("iva (21%):",total_iva)
print("total factura",total_factura)





