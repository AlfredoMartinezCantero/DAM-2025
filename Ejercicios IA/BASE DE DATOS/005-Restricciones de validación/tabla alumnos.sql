DESCRIBE clientes;

ALTER TABLE clientes
ADD COLUMN direccion VARCHAR(255);

DESCRIBE clientes;

ALTER TABLE clientes
RENAME COLUMN dni TO dninie;

DROP CONSTRAINT comprobar_dni_nie_letra;

ALTER TABLE clientes
RENAME COLUMN dni TO dninie;
