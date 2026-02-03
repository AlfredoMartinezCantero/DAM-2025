CREATE DATABASE camaron;

USE camaron;

CREATE TABLE viviendas(
	id INT(255),
	localidad VARCHAR(255),
    precio INT(255),
    metroscuadrados DECIMAL(4,2),
    aniodeconstruccion YEAR(4),
    direccion VARCHAR(255),
    altura INT(4),
    tipodevivienda VARCHAR(255),
    descripcion TEXT,
    estado VARCHAR(255),
    banios INT(4),
    habitaciones INT(4),
    teniente VARCHAR()
);

CREATE TABLE imagenes(
	id INT(255),
    id_vivienda INT(255),
    imagen VARCHAR(255),
)