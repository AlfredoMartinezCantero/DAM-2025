from lxml import etree

# Rutas a tus archivos
XML_FILE = "002-CV en xml.xml"
XSD_FILE = "CV xsd.xsd"

# Cargar XML y XSD
xml_doc = etree.parse(XML_FILE)
xsd_doc = etree.parse(XSD_FILE)

# Crear esquema
schema = etree.XMLSchema(xsd_doc)

# Validar
is_valid = schema.validate(xml_doc)
print("¿El XML es válido?:", is_valid)

# Si hay errores, mostrarlos
if not is_valid:
    print("\nErrores encontrados:")
    for error in schema.error_log:
        print(f"- Línea {error.line}: {error.message}")
