CREATE DATABASE camaron;
USE camaron;

CREATE TABLE viviendas (
    id INT UNSIGNED AUTO_INCREMENT,
    localidad VARCHAR(255),
    precio INT UNSIGNED,
    metroscuadrados DECIMAL(6,2),
    aniodeconstruccion YEAR,
    direccion VARCHAR(255),
    altura INT,
    tipodevivienda VARCHAR(255),
    descripcion TEXT,
    estado VARCHAR(255),
    banios INT,
    habitaciones INT,
    teniente VARCHAR(255),
    PRIMARY KEY (id)
);

CREATE TABLE imagenes (
    id INT UNSIGNED AUTO_INCREMENT,
    id_vivienda INT UNSIGNED,
    imagen VARCHAR(255),
    PRIMARY KEY (id),
    CONSTRAINT fk_imagenes_viviendas
        FOREIGN KEY (id_vivienda)
        REFERENCES viviendas(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);