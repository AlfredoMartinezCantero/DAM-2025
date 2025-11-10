-- Vamos a crear una base de datos llamada portafolioexamen Crea dos tablas, 
-- piezasportafolio (Identificador,titulo,descripcion,fecha,id_categoria), y categoriasportafolio(Identificador, nombre)
-- Crea claves primarias, y clave foranea para enlazar categorias con piezas Inserta registros en ambas tablas 
-- Demuestra que puedes insertar, leer, actualizar y eliminar registros Crea una seleccion cruzada con LEFT JOIN
-- y una vista de esa misma peticion Crea un usuario con permisos para acceder a esa base de datos


CREATE DATABASE portafolioexamen;

CREATE TABLE categoriasportafolio (
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255)
);

CREATE TABLE piezasportafolio (
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255),
    descripcion VARCHAR(255),
    fecha VARCHAR(50),
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES categoriasportafolio(Identificador)
);

+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| Identificador | int          | NO   | PRI | NULL    | auto_increment |
| titulo        | varchar(255) | YES  |     | NULL    |                |
| descripcion   | varchar(255) | YES  |     | NULL    |                |
| fecha         | varchar(50)  | YES  |     | NULL    |                |
| id_categoria  | int          | YES  | MUL | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)

CREATE TABLE categoriasportafolio (
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255)
);

+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| Identificador | int          | NO   | PRI | NULL    | auto_increment |
| nombre        | varchar(255) | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
2 rows in set (0.00 sec)

-- Insertamos registros en piezasportafolio
INSERT INTO piezasportafolio VALUES (
    NULL,
    'La noche estellada',
    'famosa pintura de Vincent van Gogh de 1889, 
     un óleo sobre lienzo postimpresionista que representa
     un paisaje nocturno con un cielo turbulento y un pueblo idílico.',
    '1889',
    NULL
);

-- Insertamos registros en categoriasportafolio
INSERT INTO categoriasportafolio VALUES (
    NULL,
    'Postimpresionismo'
);

-- Eliminamos columna
ALTER TABLE piezasportafolio 
DROP COLUMN apellidos;
ADD COLUMN apellidos;

-- Selección cruzada con LEFT JOIN
SELECT Identificador, titulo, descripcion, fecha, nombre AS categoria
FROM piezasportafolio
LEFT JOIN categoriasportafolio ON id_categoria = Identificador;

-- Crear vista de la selección cruzada
CREATE VIEW vista_piezas_categorias AS
SELECT Identificador, titulo, descripcion, fecha, nombre AS categoria
FROM piezasportafolio
LEFT JOIN categoriasportafolio ON id_categoria = Identificador;

-- Eliminamos registros
ALTER TABLE piezasportafolio 
DROP CONSTRAINT apellidos;

-- Mostrar usuarios en el sistema.
SELECT USER, HOST FROM mysql.user;

-- Crear un nuevo usuario.
CREATE USER 'nombredeusuario'@'servidor' IDENTIFIED BY 'contraseña';

GRANT USAGE ON *.* TO 'nombredeusuario'@'servidor';

GRANT ALL PRIVILEGES ON portafolioexamen.* TO 'nombredeusuario'@'servidor';

FLUSH PRIVILEGES;