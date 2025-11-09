-- Crea una tabla de clientes.
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(255) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    email VARCHAR(255) NOT NULL,
    localidad VARCHAR(50) NOT NULL
);

-- Inserta un nuevo cliente.
INSERT INTO clientes VALUES(
    NULL,
    'Rafa',
    'Cantero Trullenque',
    '682601446',
    'rafa.cantero@gmail.com',
    'Valencia'
);

-- Actualizar un registro con WHERE.
UPDATE clientes SET nombre = 'Jose Vicente' WHERE telefono = '620891718';

-- Eliminar todos los registros de la tabla clientes.
DELETE FROM clientes;



