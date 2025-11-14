'''
(c) Programa desarrollado por Alfredo Martínez Cantero, 2025, calculadora de IVA y posibles descuentos además de mostrar un ticket.
'''
IVA = 0.21  # Constante que representa el 21% de IVA
cliente_nombre = input("Nombre: ")
edad = int(input("Edad: ")) # Convertimos la edad a número entero

# Si la edad es menor que 18, no se puede emitir una factura
if edad < 18: 
    print("No se puede emitir una factura a un menor de 18 años")
else:
    base_imponible = float(input("Introduce la base imponible de la factura: "))
    if base_imponible < 0:
        print("No se puede emitir una factura con importe negativo")
    else:
        importe_descuento = 0
        porcentaje_descuento = 0
        
######## Si la base imponible está entre 100 y 199.99, se aplica un 5% de descuento ######
        if base_imponible >=100 and base_imponible <= 199.99:
          importe_descuento = base_imponible * 0.05 # Calculamos y aplicamos el 5% de descuento
          porcentaje_descuento = 5
        elif base_imponible >= 200:
            importe_descuento = base_imponible * 0.1 # Calculamos y aplicamos el 10% de descuento
            porcentaje_descuento = 10

######## Calculamos el total ################################################
        base_tras_descuento = base_imponible - importe_descuento
        importe_iva = base_tras_descuento * IVA
        total_factura = base_tras_descuento + IVA
        
############Información del programa ######### 
        print("Impresora de tickets")
        print("Alfredo Martínez Cantero")
        print("2025 - v1.0 (c)")
        print("")
        print("----------------------------------------------------------")
        print("")

############Información Cliente ############
        print("Nombre: ", cliente_nombre)
        print("Edad: ", edad)
        print("")
        print("----------------------------------------------------------")
        print("")
        
############Desglose del ticket #############
        print("Base Imponible: ", base_imponible)
        print("% Descuento : ", porcentaje_descuento, "%")
        print("Importe descuento: ", importe_descuento)
        print("Base tras descuento: ", base_tras_descuento)
        print("IVA: ", importe_iva)
        print("") 
        print("----------------------------------------------------------")
        print("")
