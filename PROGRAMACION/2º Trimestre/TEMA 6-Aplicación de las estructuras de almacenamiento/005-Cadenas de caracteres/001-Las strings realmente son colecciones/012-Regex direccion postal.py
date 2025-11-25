import re

patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

direccion_mal = "Calle Mayor"
direccion_bien = "Calle Mayor 10 46001"

print(re.match(patron, direccion_mal))
print(re.match(patron, direccion_bien))

