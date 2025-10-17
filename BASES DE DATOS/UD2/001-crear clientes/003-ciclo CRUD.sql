INSERT INTO clientes VALUES(
	NULL,
	'Alfredo',
	'Martínez Cantero',
	'alfredomartinezcantero@gmail.com'
);

-- read
SELECT * FROM clientes;
-- update
UPDATE clientes
SET email = 'info@alfredomartinezcantero@gmail.com'
WHERE Identificador = 1;
-- delete
DELETE FROM clientes
WHERE Identificador = 1;
