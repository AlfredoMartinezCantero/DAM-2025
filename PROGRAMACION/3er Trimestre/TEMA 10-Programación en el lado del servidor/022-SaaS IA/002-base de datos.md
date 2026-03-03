CREATE DATABASE saasia;

USE saasia;

CREATE TABLE clientes (
    id INT(11) NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255),
    apellidos VARCHAR(255),
    email VARCHAR(255),
    poblacion VARCHAR(255),
    fecha_de_nacimiento DATE,
    PRIMARY KEY (id)
);