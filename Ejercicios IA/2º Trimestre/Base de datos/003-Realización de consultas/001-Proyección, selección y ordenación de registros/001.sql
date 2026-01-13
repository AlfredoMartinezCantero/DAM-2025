-- sudo mysql -u root -p

-- Creamos una base de datos

CREATE DATABASE clientes_ejercicio;

USE clientes_ejercicio;

CREATE TABLE clientes(
  nombre VARCHAR(255),
  apellidos VARCHAR(255),
  edad INT
);

INSERT INTO clientes VALUES('Juan', 'Pérez', 30), ('María', 'López', 25), ('Carlos', 'González', 40);

-- Ordenamos descendentemente por edad

SELECT 
  nombre AS 'Nombre del cliente',
  apellidos AS 'Apellidos del cliente',
  edad AS 'Edad del cliente'
FROM 
  clientes
ORDER BY
  edad DESC;

-- Hago una selección nombrando las columnas

SELECT 
  nombre,
  apellidos,
  edad 
FROM 
  clientes;

-- Ordenación ascendente explícito por apellidos

SELECT 
  nombre AS 'Nombre del cliente',
  apellidos AS 'Apellidos del cliente',
  edad AS 'Edad del cliente'
FROM 
  clientes
ORDER BY
  apellidos ASC;

-- Selecciono solo algunas columnas:

SELECT 
  nombre,
  apellidos
FROM 
  clientes;

-- La proyección se refiere a seleccionar un subconjunto de columnas de una tabla. 

SELECT 
  nombre AS 'Nombre del cliente',
  apellidos AS 'Apellidos del cliente'
FROM 
  clientes;

-- Hay un orden por defecto, si no se especifica el orden, SQL ordenará los resultados en orden ascendente por la columna seleccionada.

SELECT 
  nombre AS 'Nombre del cliente',
  apellidos AS 'Apellidos del cliente',
  edad AS 'Edad del cliente'
FROM 
  clientes
ORDER BY
  apellidos;

-- También se puede seguir un orden por dos columnas, se pueden ordenar los resultados por más de una columna, especificando el orden para cada una.

SELECT 
  nombre AS 'Nombre del cliente',
  apellidos AS 'Apellidos del cliente',
  edad AS 'Edad del cliente'
FROM 
  clientes
ORDER BY
  edad DESC,apellidos ASC;

