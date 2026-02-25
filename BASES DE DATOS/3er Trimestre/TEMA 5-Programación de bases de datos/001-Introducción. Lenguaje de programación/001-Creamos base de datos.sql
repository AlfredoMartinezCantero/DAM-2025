CREATE DATABASE sqlavanzado;
USE sqlavanzado;

CREATE TABLE clientes(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    apellidos VARCHAR(255),
    email VARCHAR(255),
    direccion VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO clientes VALUES(
	NULL,
  'Alfredo',	
  'Martinez Cantero',
  'alfredo@gmail.com',
  'La calle de Alfredo'
);

SELECT * FROM clientes;