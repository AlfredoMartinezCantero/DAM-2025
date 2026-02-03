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


CREATE USER 
'camaron'@'localhost' 
IDENTIFIED  BY 'Camaron123$';

GRANT USAGE ON *.* TO 'camaron'@'localhost';

ALTER USER 'camaron'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON camaron.* 
TO 'camaron'@'localhost';

FLUSH PRIVILEGES;
