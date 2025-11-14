-- Vamos a crear una base de datos llamada portafolioexamen Crea dos tablas, 
-- piezasportafolio (Identificador,titulo,descripcion,fecha,id_categoria), y categoriasportafolio(Identificador, nombre)
-- Crea claves primarias, y clave foranea para enlazar categorias con piezas Inserta registros en ambas tablas 
-- Demuestra que puedes insertar, leer, actualizar y eliminar registros Crea una seleccion cruzada con LEFT JOIN
-- y una vista de esa misma peticion Crea un usuario con permisos para acceder a esa base de datos


-- Crear base de datos
CREATE DATABASE portafolioexamen;
USE portafolioexamen;

-- Crear tabla categorías
CREATE TABLE categoriasportafolio (
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

-- Crear tabla piezas
CREATE TABLE piezasportafolio (
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descripcion TEXT,
    fecha DATE,
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES categoriasportafolio(Identificador)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);

-- Mostrar estructura de las tablas
DESCRIBE categoriasportafolio;
DESCRIBE piezasportafolio;

-----------------------

-- Insertar registros en categorías PRIMERO
INSERT INTO categoriasportafolio (nombre) VALUES 
('Postimpresionismo'),
('Impresionismo'),
('Arte Moderno'),
('Arte Abstracto');

-- Insertar registros en piezas con referencias válidas
INSERT INTO piezasportafolio (titulo, descripcion, fecha, id_categoria) VALUES 
('La noche estrellada', 'Famosa pintura de Vincent van Gogh de 1889, un óleo sobre lienzo postimpresionista', '1889-06-01', 1),
('Nenúfares', 'Serie de pinturas de Claude Monet representando su jardín en Giverny', '1915-01-01', 2),
('El grito', 'Obra emblemática de Edvard Munch representando la angustia existencial', '1893-01-01', 3),
('Composición VIII', 'Obra abstracta de Wassily Kandinsky', '1923-01-01', 4);

-----------------------

-- CREATE (Insertar nuevo registro)
INSERT INTO piezasportafolio (titulo, descripcion, fecha, id_categoria) 
VALUES ('Los girasoles', 'Serie de pinturas de girasoles de Vincent van Gogh', '1888-08-01', 1);

-- READ (Leer registros)
SELECT * FROM piezasportafolio;
SELECT * FROM categoriasportafolio;

-- UPDATE (Actualizar registro)
UPDATE piezasportafolio 
SET descripcion = 'Obra maestra de Vincent van Gogh que representa un cielo nocturno turbulento' 
WHERE Identificador = 1;

-- DELETE (Eliminar registro)
DELETE FROM piezasportafolio WHERE Identificador = 3;

-----------------------

-- Selección cruzada con LEFT JOIN (MEJORADA)
SELECT 
    p.Identificador,
    p.titulo,
    p.descripcion,
    p.fecha,
    c.nombre AS categoria,
    c.Identificador AS id_categoria
FROM piezasportafolio p
LEFT JOIN categoriasportafolio c ON p.id_categoria = c.Identificador;

-- Crear vista de la selección cruzada
CREATE VIEW vista_piezas_categorias AS
SELECT 
    p.Identificador,
    p.titulo,
    p.descripcion,
    p.fecha,
    c.nombre AS categoria,
    c.Identificador AS id_categoria
FROM piezasportafolio p
LEFT JOIN categoriasportafolio c ON p.id_categoria = c.Identificador;

-- Consultar la vista
SELECT * FROM vista_piezas_categorias;

-----------------------

-- Mostrar usuarios existentes
SELECT USER, HOST FROM mysql.user;

-- Crear nuevo usuario específico para la base de datos
CREATE USER 'admin_portafolio'@'localhost' IDENTIFIED BY 'SecurePass123!';

-- Otorgar permisos específicos (no usar ALL PRIVILEGES en producción)
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE VIEW ON portafolioexamen.* TO 'admin_portafolio'@'localhost';

-- Actualizar privilegios
FLUSH PRIVILEGES;

-- Verificar permisos del usuario
SHOW GRANTS FOR 'admin_portafolio'@'localhost';