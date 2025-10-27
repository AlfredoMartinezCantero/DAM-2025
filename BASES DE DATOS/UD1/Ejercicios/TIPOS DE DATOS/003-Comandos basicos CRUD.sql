-- Acceder
sudo mysql -u root -p

-- Create

INSERT INTO clientes VALUES(
	'12345678A',
	'Alfredo',
	'Martínez Cantero',
	'alfredomartinezcantero@gmail.com'
);

-- Read

SELECT * FROM clientes;

+-----------+---------+-------------------+----------------------------------+
| dni       | nombre  | apellidos         | email                            |
+-----------+---------+-------------------+----------------------------------+
| 12345678A | Alfredo | Martínez Cantero  | alfredomartinezcantero@gmail.com |
+-----------+---------+-------------------+----------------------------------+
1 row in set (0,00 sec)

-- Update

UPDATE clientes
SET dni = '11111111A'
WHERE nombre = 'Alfredo';

+-----------+---------+-------------------+----------------------------------+
| dni       | nombre  | apellidos         | email                            |
+-----------+---------+-------------------+----------------------------------+
| 11111111A | Alfredo | Martínez Cantero  | alfredomartinezcantero@gmail.com |
+-----------+---------+-------------------+----------------------------------+
1 row in set (0,00 sec)

-- Delete

DELETE FROM clientes
WHERE dni = '11111111A';





