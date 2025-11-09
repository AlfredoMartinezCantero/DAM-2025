-- Conexión a MySQL.
sudo mysql -u root -p

-- Mostrar bases de datos.
SHOW DATABASES;

-- Seleccionar BBDD empresadam.
USE empresadam;

-- Mostrar tablas en la BBDD.
SHOW TABLES;

-- Ejercicio con la tabla pedidos.
INSERT INTO pedidos (numerodepedido, cliente, producto) 
VALUES ('P001', 'Juan Pérez', 'Laptop');

SELECT * FROM pedidos;

-- Prueba con valores NULL.
INSERT INTO pedidos (numerodepedido, cliente)
VALUES ('P002', 'Ana González');

SELECT * FROM pedidos WHERE numerodepedido = 'P002';