# pip3 install odfpy --break-system-packages

from odf.opendocument import load
from odf.table import Table, TableRow, TableCell
from odf.text import P

documento = load("alumnosynotas.ods")
hoja = documento.spreadsheet.getElementsByType(Table)[0]

for fila in hoja.getElementsByType(TableRow):
    valores = []
    for celda in fila.getElementsByType(TableCell):
        texto = ""
        for p in celda.getElementsByType(P):
            texto += p.firstChild.data if p.firstChild else ""
        valores.append(texto)
    print(valores)