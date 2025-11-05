-- Iniciando sesión en MySQL
sudo mysql -u root -p

-- 1. CREAR LA BASE DE DATOS

CREATE DATABASE portafolio;
SHOW DATABASES;
USE portafolio;

Query OK, 1 row affected (0.01 sec)

+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| portafolio         |
+--------------------+
5 rows in set (0.00 sec)

Database changed

-- 2. CREAR LA TABLA CATEGORIAS
CREATE TABLE categorias (
  Identificador INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(100),
  descripcion TEXT
);

Query OK, 0 rows affected (0.02 sec)

-- Ver estructura de la tabla
DESCRIBE categorias;

+----------------+--------------+------+-----+---------+----------------+
| Field          | Type         | Null | Key | Default | Extra          |
+----------------+--------------+------+-----+---------+----------------+
| Identificador  | int          | NO   | PRI | NULL    | auto_increment |
| titulo         | varchar(100) | YES  |     | NULL    |                |
| descripcion    | text         | YES  |     | NULL    |                |
+----------------+--------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

-- Insertar categorías de ejemplo
INSERT INTO categorias VALUES 
(NULL, 'Diseño Gráfico', 'Proyectos de ilustración, branding y diseño visual'),
(NULL, 'Desarrollo Web', 'Sitios web y aplicaciones interactivas creadas con tecnologías modernas'),
(NULL, 'Fotografía', 'Colección de trabajos fotográficos artísticos y comerciales');

Query OK, 3 rows affected (0.01 sec)
Records: 3  Duplicates: 0  Warnings: 0

-- Ver los registros insertados
SELECT * FROM categorias;

+----------------+------------------+--------------------------------------------------------------------------+
| Identificador  | titulo           | descripcion                                                              |
+----------------+------------------+--------------------------------------------------------------------------+
| 1              | Diseño Gráfico   | Proyectos de ilustración, branding y diseño visual                       |
| 2              | Desarrollo Web   | Sitios web y aplicaciones interactivas creadas con tecnologías modernas  |
| 3              | Fotografía       | Colección de trabajos fotográficos artísticos y comerciales              |
+----------------+------------------+--------------------------------------------------------------------------+
3 rows in set (0.00 sec)

-- 3. CREAR LA TABLA PIEZAS
CREATE TABLE piezas (
  Identificador INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(100),
  descripcion TEXT,
  imagen VARCHAR(255),
  url VARCHAR(255),
  id_categoria INT,
  CONSTRAINT fk_categoria FOREIGN KEY (id_categoria) REFERENCES categorias(Identificador)
);

Query OK, 0 rows affected (0.03 sec)

-- Ver estructura de la tabla
DESCRIBE piezas;

+----------------+--------------+------+-----+---------+----------------+
| Field          | Type         | Null | Key | Default | Extra          |
+----------------+--------------+------+-----+---------+----------------+
| Identificador  | int          | NO   | PRI | NULL    | auto_increment |
| titulo         | varchar(100) | YES  |     | NULL    |                |
| descripcion    | text         | YES  |     | NULL    |                |
| imagen         | varchar(255) | YES  |     | NULL    |                |
| url            | varchar(255) | YES  |     | NULL    |                |
| id_categoria   | int          | YES  | MUL | NULL    |                |
+----------------+--------------+------+-----+---------+----------------+
6 rows in set (0.00 sec)

-- Insertar piezas de ejemplo
INSERT INTO piezas VALUES 
(NULL, 'Logo Minimalista', 'Diseño de logotipo para marca personal', 'logo.jpg', 'https://miportafolio.com/logo', 1),
(NULL, 'Landing Page Interactiva', 'Desarrollo de una landing page con animaciones CSS y JS', 'landing.jpg', 'https://miportafolio.com/landing', 2),
(NULL, 'Retrato en Blanco y Negro', 'Fotografía artística realizada en estudio', 'retrato.jpg', 'https://miportafolio.com/retrato', 3);

Query OK, 3 rows affected (0.02 sec)
Records: 3  Duplicates: 0  Warnings: 0

-- Ver los registros insertados
SELECT * FROM piezas;

+----------------+--------------------------+------------------------------------------------------------+--------------+-------------------------------------------+--------------+
| Identificador  | titulo                   | descripcion                                                | imagen       | url                                       | id_categoria |
+----------------+--------------------------+------------------------------------------------------------+--------------+-------------------------------------------+--------------+
| 1              | Logo Minimalista         | Diseño de logotipo para marca personal                     | logo.jpg     | https://miportafolio.com/logo             | 1            |
| 2              | Landing Page Interactiva | Desarrollo de una landing page con animaciones CSS y JS    | landing.jpg  | https://miportafolio.com/landing          | 2            |
| 3              | Retrato en Blanco y Negro| Fotografía artística realizada en estudio                  | retrato.jpg  | https://miportafolio.com/retrato          | 3            |
+----------------+--------------------------+------------------------------------------------------------+--------------+-------------------------------------------+--------------+
3 rows in set (0.00 sec)

-- 4. CONSULTA CRUZADA (JOIN)
-- Mostrar las piezas junto con el título y descripción de su categoría
SELECT 
  piezas.titulo AS Título_Pieza,
  piezas.descripcion AS Descripción_Pieza,
  piezas.imagen AS Imagen,
  piezas.url AS URL,
  categorias.titulo AS Categoría,
  categorias.descripcion AS Descripción_Categoría
FROM piezas
LEFT JOIN categorias ON piezas.id_categoria = categorias.Identificador;

+--------------------------+------------------------------------------------------------+--------------+-------------------------------------------+------------------+------------------------------------------------------------+
| Título_Pieza             | Descripción_Pieza                                          | Imagen       | URL                                       | Categoría        | Descripción_Categoría                                       |
+--------------------------+------------------------------------------------------------+--------------+-------------------------------------------+------------------+------------------------------------------------------------+
| Logo Minimalista         | Diseño de logotipo para marca personal                     | logo.jpg     | https://miportafolio.com/logo             | Diseño Gráfico   | Proyectos de ilustración, branding y diseño visual         |
| Landing Page Interactiva | Desarrollo de una landing page con animaciones CSS y JS    | landing.jpg  | https://miportafolio.com/landing          | Desarrollo Web   | Sitios web y aplicaciones interactivas creadas con tecnologías modernas |
| Retrato en Blanco y Negro| Fotografía artística realizada en estudio                  | retrato.jpg  | https://miportafolio.com/retrato          | Fotografía       | Colección de trabajos fotográficos artísticos y comerciales|
+--------------------------+------------------------------------------------------------+--------------+-------------------------------------------+------------------+------------------------------------------------------------+
3 rows in set (0.00 sec)

-- 5. CREAR UNA VISTA (VIEW)
CREATE VIEW vista_piezas AS
SELECT 
  piezas.titulo AS Título_Pieza,
  piezas.descripcion AS Descripción_Pieza,
  piezas.imagen AS Imagen,
  piezas.url AS URL,
  categorias.titulo AS Categoría,
  categorias.descripcion AS Descripción_Categoría
FROM piezas
LEFT JOIN categorias ON piezas.id_categoria = categorias.Identificador;

Query OK, 0 rows affected (0.02 sec)

-- Consultar la vista
SELECT * FROM vista_piezas;

+--------------------------+------------------------------------------------------------+--------------+-------------------------------------------+------------------+------------------------------------------------------------+
| Título_Pieza             | Descripción_Pieza                                          | Imagen       | URL                                       | Categoría        | Descripción_Categoría                                       |
+--------------------------+------------------------------------------------------------+--------------+-------------------------------------------+------------------+------------------------------------------------------------+
| Logo Minimalista         | Diseño de logotipo para marca personal                     | logo.jpg     | https://miportafolio.com/logo             | Diseño Gráfico   | Proyectos de ilustración, branding y diseño visual         |
| Landing Page Interactiva | Desarrollo de una landing page con animaciones CSS y JS    | landing.jpg  | https://miportafolio.com/landing          | Desarrollo Web   | Sitios web y aplicaciones interactivas creadas con tecnologías modernas |
| Retrato en Blanco y Negro| Fotografía artística realizada en estudio                  | retrato.jpg  | https://miportafolio.com/retrato          | Fotografía       | Colección de trabajos fotográficos artísticos y comerciales|
+--------------------------+------------------------------------------------------------+--------------+-------------------------------------------+------------------+------------------------------------------------------------+
3 rows in set (0.00 sec)

CREATE USER 'usuario_portafolio'@'localhost' IDENTIFIED BY 'mi_contraseña_segura';
GRANT ALL PRIVILEGES ON portafolio.* TO 'usuario_portafolio'@'localhost';
FLUSH PRIVILEGES;