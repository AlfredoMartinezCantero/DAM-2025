# 003-validador.py 
from lxml import etree

try:
    # Leemos los archivos físicos
    xml_doc = etree.parse("001-documento de referencia.xml")
    xsd_doc = etree.parse("002-esquema.xsd")

    # Creamos el objeto validador a partir del XSD
    schema = etree.XMLSchema(xsd_doc)

    # Ejecutamos la validación
    es_valido = schema.validate(xml_doc)

    # Mostramos el resultado de forma amigable
    if es_valido:
        print("RESULTADO: El documento XML es VÁLIDO según el esquema XSD.")
    else:
        print("RESULTADO: El documento NO es válido.")
        # Si falla, imprimimos el log de errores para saber por qué
        print(schema.error_log)

except OSError:
    print("Error: No se encuentran los archivos .xml o .xsd en la carpeta.")
except etree.XMLSchemaParseError as e:
    print(f"Error en la estructura del XSD: {e}")