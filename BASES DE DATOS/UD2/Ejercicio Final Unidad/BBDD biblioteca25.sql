---
# Introducción:
Este ejercicio de BBDD tiene como objetivo la creación y gestión de una base de datos para una biblioteca, denominada **biblioteca25**. A través de este ejercicio se busca practicar la creación de tablas relacionales, la definición de claves primarias y foráneas, así como la implementación de restricciones de integridad y índices para optimizar consultas.

Se diseñan cuatro tablas principales: autores, libros, socios y prestamos, que permiten almacenar información sobre autores de libros, títulos disponibles, socios de la biblioteca y los préstamos realizados. Además, se incluyen validaciones de datos mediante restricciones como NOT NULL, UNIQUE y CHECK, así como la creación de índices para mejorar el rendimiento de las consultas.
Finalmente, se realizan inserciones de datos de ejemplo y se verifican las estructuras y contenidos de las tablas mediante las sentencias DESCRIBE y SELECT, asegurando así que la base de datos se encuentra correctamente estructurada y funcional.

---
#Creamos la base de datos.

---
```
CREATE DATABASE biblioteca25;
```
---
#Seleccionamos la base de datos para usarla.

---
```
USE biblioteca25;
```
---
#Verificamos qué base de daos está actualmente en uso.

---
```
SELECT DATABASE();
+--------------+
| DATABASE()   |
+--------------+
| biblioteca25 |
+--------------+
```
---
#Creamos la tabla **autores** con claves primarias.

---
```
CREATE TABLE autores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    pais VARCHAR(80)
);

Query OK, 0 rows affected (0.03 sec)
```
---
#Creamos la tabla **libros** con claves primarias y foráneas.

---
```
CREATE TABLE libros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    isbn VARCHAR(20) NOT NULL UNIQUE,
    precio DECIMAL(8,2) NOT NULL CHECK (precio >= 0),
    autor_id INT NOT NULL,
    FOREIGN KEY (autor_id)
        REFERENCES autores(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);
```
---
#Listamos las tablas existentes en la base de datos.

---
```
SHOW TABLES;
#Resultado esperado:

+----------------+
| Tables_in_biblioteca25 |
+----------------+
| autores        |
| libros         |
+----------------+
```
---
#Creamos un índice sobre la columna `autor_id` en la tabla `libros`.

---
```
CREATE INDEX idx_autor_id ON libros(autor_id);
```
---
#Describimos la estructura de la tabla `libros`.

---
```
DESCRIBE libros;
```
---
#Mostramos los índices existentes en `libros`.

---
```
SHOW INDEX FROM libros;
```
```
DESCRIBE libros;
+-----------+--------------+------+-----+---------+----------------+
| Field     | Type         | Null | Key | Default | Extra          |
+-----------+--------------+------+-----+---------+----------------+
| id        | int          | NO   | PRI | NULL    | auto_increment |
| titulo    | varchar(200) | NO   |     | NULL    |                |
| isbn      | varchar(20)  | NO   | UNI | NULL    |                |
| precio    | decimal(8,2) | NO   |     | NULL    |                |
| autor_id  | int          | NO   | MUL | NULL    |                |
+-----------+--------------+------+-----+---------+----------------+
```
```
SHOW INDEX FROM libros;
+--------+------------+-------------+--------------+-----------+-----------+
| Table  | Non_unique | Key_name    | Seq_in_index | Column_name | Index_type |
+--------+------------+-------------+--------------+-----------+-----------+
| libros | 0          | PRIMARY     | 1            | id        | BTREE     |
| libros | 0          | isbn        | 1            | isbn      | BTREE     |
| libros | 1          | autor_id    | 1            | autor_id  | BTREE     |
| libros | 1          | idx_autor_id| 1            | autor_id  | BTREE     |
+--------+------------+-------------+--------------+-----------+-----------+
```
---
#Creamos la tabla `socios` con clave primaria y restricciones.

---
```
CREATE TABLE socios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    fecha_alta DATE NOT NULL DEFAULT CURRENT_DATE,
    CHECK (email LIKE '%@%.%')
);

Query OK, 0 rows affected (0.02 sec)
```
---
#Verificamos la estructura de la tabla `socios`.

---
```
DESCRIBE socios;
+-------------+--------------+------+-----+----------------+----------------+
| Field       | Type         | Null | Key | Default        | Extra          |
+-------------+--------------+------+-----+----------------+----------------+
| id          | int          | NO   | PRI | NULL           | auto_increment |
| nombre      | varchar(100) | NO   |     | NULL           |                |
| email       | varchar(120) | NO   | UNI | NULL           |                |
| fecha_alta  | date         | NO   |     | CURRENT_DATE   |                |
+-------------+--------------+------+-----+----------------+----------------+
```
---
#Creamos la tabla `prestamos` con claves primarias y foráneas para registrar préstamos de libros.

---
```
CREATE TABLE prestamos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    socio_id INT NOT NULL,
    libro_id INT NOT NULL,
    fecha_prestamo DATE NOT NULL DEFAULT CURRENT_DATE,
    fecha_devolucion DATE,
    CHECK (fecha_devolucion IS NULL OR fecha_devolucion >= fecha_prestamo),
    FOREIGN KEY (socio_id)
        REFERENCES socios(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (libro_id)
        REFERENCES libros(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);
Query OK, 0 rows affected (0.02 sec)
```
---
#Creamos un índice compuesto para optimizar consultas de prestamos por socio y libro.

---
```
CREATE INDEX idx_prestamos_socio_libro ON prestamos(socio_id, libro_id);
```
---
#Verificamos la estructura de la tabla `prestamos`.

---
```
DESCRIBE prestamos;

+----------------+-----------+------+-----+----------------+----------------+
| Field          | Type      | Null | Key | Default        | Extra          |
+----------------+-----------+------+-----+----------------+----------------+
| id             | int       | NO   | PRI | NULL           | auto_increment |
| socio_id       | int       | NO   | MUL | NULL           |                |
| libro_id       | int       | NO   | MUL | NULL           |                |
| fecha_prestamo | date      | NO   |     | CURRENT_DATE   |                |
| fecha_devolucion | date    | YES  |     | NULL           |                |
+----------------+-----------+------+-----+----------------+----------------+
```
---
#Mostramos los índices de la tabla `prestamos`.

---
```
SHOW INDEX FROM prestamos;

+------------+------------+-----------------------------+--------------+-----------+-----------+
| Table      | Non_unique | Key_name                    | Seq_in_index | Column_name | Index_type |
+------------+------------+-----------------------------+--------------+-----------+-----------+
| prestamos  | 0          | PRIMARY                     | 1            | id        | BTREE     |
| prestamos  | 1          | idx_prestamos_socio_libro   | 1            | socio_id  | BTREE     |
| prestamos  | 1          | idx_prestamos_socio_libro   | 2            | libro_id  | BTREE     |
+------------+------------+-----------------------------+--------------+-----------+-----------+
```
---
#Insertamos autores en la tabla `autores`.

---
```
INSERT INTO autores (nombre, pais) VALUES
('Isabel Allendre', 'Chile'),
('Gabriel García Márquez', 'Colombia'),
('Haruki Murakami', 'Japón');

Query OK, 3 rows affected (0.01 sec)
Records: 3  Duplicates: 0  Warnings: 0
```
---
#Insertamos libros en la tabla `libros`, relacionándolos con autores.

---
```
INSERT INTO libros (titulo, isbn, precio, autor_id) VALUES
('La casa de los espíritus', '9788401352836', 19.90, 1),
('Cien años de soledad', '9780307474728', 24.50, 2 ),
('Kafka en la orilla', '9788499082478', 18.00, 3);

Query OK, 3 rows affected (0.01 sec)
Records: 3  Duplicates: 0  Warnings: 0
```
---
#Insertamos socios en la tabla `socios`.

---
```
INSERT INTO socios (nombre, email) VALUES
('Ana Ruiz', 'ana.ruiz@example.com'),
('Luis Pérez', 'luis.perez@example.com'),
('Haruki Murakami', 'haruki.murakami@example.com');

Query OK, 3 rows affected (0.01 sec)
Records: 3  Duplicates: 0  Warnings: 0
```
---
#Insertamos préstamos de libros a los socios.

---
```
INSERT INTO prestamos (socio_id, libro_id, fecha_prestamo) VALUES (1, 1);

INSERT INTO prestamos (socio_id, libro_id, fecha_prestamo, fecha_devolucion)
VALUES (2, 2, '2024-05-10', '2024-05-20');

Query OK, 1 row affected (0.01 sec)
Query OK, 1 row affected (0.01 sec)
```
---
#Consultamos los datos de todas las tablas.

---
```
SELECT * FROM autores;
SELECT * FROM libros;
SELECT * FROM socios;
SELECT * FROM prestamos;
```
---
#Verificamos todas las tablas existentes con (SHOW TABLES)
y revisamos la estructura de cada tabla con (DESCRIBE autores, DESCRIBE libros, DESCRIBE socios, DESCRIBE prestamos).

---
```
SHOW TABLES;

+----------------+
| Tables_in_biblioteca25 |
+----------------+
| autores        |
| libros         |
| prestamos      |
| socios         |
+----------------+
```
```
DESCRIBE autores;

+--------+-------------+------+-----+---------+----------------+
| Field  | Type        | Null | Key | Default | Extra          |
+--------+-------------+------+-----+---------+----------------+
| id     | int         | NO   | PRI | NULL    | auto_increment |
| nombre | varchar(100)| NO   |     | NULL    |                |
| pais   | varchar(80) | YES  |     | NULL    |                |
+--------+-------------+------+-----+---------+----------------+
```
```
DESCRIBE libros;

+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| titulo   | varchar(200) | NO   |     | NULL    |                |
| isbn     | varchar(20)  | NO   | UNI | NULL    |                |
| precio   | decimal(8,2) | NO   |     | NULL    |                |
| autor_id | int          | NO   | MUL | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
```
```
DESCRIBE socios;

+------------+--------------+------+-----+-------------+----------------+
| Field      | Type         | Null | Key | Default     | Extra          |
+------------+--------------+------+-----+-------------+----------------+
| id         | int          | NO   | PRI | NULL        | auto_increment |
| nombre     | varchar(100) | NO   |     | NULL        |                |
| email      | varchar(120) | NO   | UNI | NULL        |                |
| fecha_alta | date         | NO   |     | CURRENT_DATE|                |
+------------+--------------+------+-----+-------------+----------------+
```
```
DESCRIBE prestamos;

+------------------+-------+------+-----+-------------+----------------+
| Field            | Type  | Null | Key | Default     | Extra          |
+------------------+-------+------+-----+-------------+----------------+
| id               | int   | NO   | PRI | NULL        | auto_increment |
| socio_id         | int   | NO   | MUL | NULL        |                |
| libro_id         | int   | NO   | MUL | NULL        |                |
| fecha_prestamo   | date  | NO   |     | CURRENT_DATE|                |
| fecha_devolucion | date  | YES  |     | NULL        |                |
+------------------+-------+------+-----+-------------+----------------+
```
---
#Tablas finales con datos insertados.

---
```
Tabla de autores:
+----+------------------------+----------+
| id | nombre                 | pais     |
+----+------------------------+----------+
| 1  | Isabel Allendre        | Chile    |
| 2  | Gabriel García Márquez | Colombia |
| 3  | Haruki Murakami        | Japón    |
+----+------------------------+----------+
```
```
Tabla de libros:
+----+-------------------------+----------------+--------+----------+
| id | titulo                  | isbn           | precio | autor_id |
+----+-------------------------+----------------+--------+----------+
| 1  | La casa de los espíritus | 9788401352836 | 19.90  | 1        |
| 2  | Cien años de soledad    | 9780307474728  | 24.50  | 2        |
| 3  | Kafka en la orilla      | 9788499082478  | 18.00  | 3        |
+----+-------------------------+----------------+--------+----------+
```
```
Tabla de socios:
+----+------------------+----------------------------+------------+
| id | nombre           | email                      | fecha_alta |
+----+------------------+----------------------------+------------+
| 1  | Ana Ruiz         | ana.ruiz@example.com       | 2025-10-31 |
| 2  | Luis Pérez       | luis.perez@example.com     | 2025-10-31 |
| 3  | Haruki Murakami  | haruki.murakami@example.com| 2025-10-31 |
+----+------------------+----------------------------+------------+
```
```
Tabla de prestamos:
+----+----------+----------+---------------+-----------------+
| id | socio_id | libro_id | fecha_prestamo | fecha_devolucion|
+----+----------+----------+---------------+-----------------+
| 1  | 1        | 1        | 2025-10-31     | NULL            |
| 2  | 2        | 2        | 2024-05-10     | 2024-05-20      |
+----+----------+----------+---------------+-----------------+
```
---
# Conclusión:
A través de este ejercicio se consigue comprender conceptos fundamentales de BBDD, tales como la creación de tablas, relaciones entre tablas mediante claves foráneas, integridad referencial y uso de índices.
Se comprueba paso a paso la correcta inserción de datos y la relación entre las tablas autores, libros, socios y prestamos, permitiendo gestionar eficientemente la información de una biblioteca.
Este ejercicio sirve como base para el desarrollo de aplicaciones más complejas de gestión de bibliotecas y refuerza buenas prácticas en el diseño y administración de bases de datos relacionales.

---