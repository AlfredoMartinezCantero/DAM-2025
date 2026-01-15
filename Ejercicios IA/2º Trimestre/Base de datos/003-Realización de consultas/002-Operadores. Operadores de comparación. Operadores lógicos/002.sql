-- sudo mysql -u root -p

-- accedemos a la base de datos
USE clientes_ejercicio;

-- sumamos 500 a la edad
SELECT nombre, apellidos, edad + 500 FROM clientes;
+--------+-----------+------------+
| nombre | apellidos | edad + 500 |
+--------+-----------+------------+
| Juan   | Pérez     |        530 |
| María  | López     |        525 |
| Carlos | González  |        540 |
+--------+-----------+------------+
3 rows in set (0,01 sec)

-- restamos 500 a la edad
SELECT nombre, apellidos, edad - 500 FROM clientes;
+--------+-----------+------------+
| nombre | apellidos | edad - 500 |
+--------+-----------+------------+
| Juan   | Pérez     |       -470 |
| María  | López     |       -475 |
| Carlos | González  |       -460 |
+--------+-----------+------------+
3 rows in set (0,01 sec)

-- multiplicamos la edad por 500
SELECT nombre, apellidos, edad * 500 FROM clientes;
+--------+-----------+------------+
| nombre | apellidos | edad * 500 |
+--------+-----------+------------+
| Juan   | Pérez     |      15000 |
| María  | López     |      12500 |
| Carlos | González  |      20000 |
+--------+-----------+------------+
3 rows in set (0,00 sec)

-- dividimos la edad entre 500
SELECT nombre, apellidos, edad / 500 FROM clientes;
+--------+-----------+------------+
| nombre | apellidos | edad / 500 |
+--------+-----------+------------+
| Juan   | Pérez     |     0.0600 |
| María  | López     |     0.0500 |
| Carlos | González  |     0.0800 |
+--------+-----------+------------+
3 rows in set (0,00 sec)

-- filtramos clientes menores de 30 años
SELECT nombre, apellidos, edad, edad < 30 AS 'Menor de 30 años' FROM clientes;
+--------+-----------+------+-------------------+
| nombre | apellidos | edad | Menor de 30 años  |
+--------+-----------+------+-------------------+
| Juan   | Pérez     |   30 |                 0 |
| María  | López     |   25 |                 1 |
| Carlos | González  |   40 |                 0 |
+--------+-----------+------+-------------------+
3 rows in set (0,01 sec)

-- filtramos clientes entre 30 y 40 años
SELECT nombre, apellidos, edad, edad >= 30 AND edad < 40 AS 'Entre 30 y 40 años' FROM clientes;
+--------+-----------+------+---------------------+
| nombre | apellidos | edad | Entre 30 y 40 años  |
+--------+-----------+------+---------------------+
| Juan   | Pérez     |   30 |                   1 |
| María  | López     |   25 |                   0 |
| Carlos | González  |   40 |                   0 |
+--------+-----------+------+---------------------+
3 rows in set (0,01 sec)

-- filtro los clientes que sean mayores de 40 años
SELECT nombre, apellidos, edad, edad > 40 AS 'Mayor de 40 años' FROM clientes;
+--------+-----------+------+-------------------+
| nombre | apellidos | edad | Mayor de 40 años  |
+--------+-----------+------+-------------------+
| Juan   | Pérez     |   30 |                 0 |
| María  | López     |   25 |                 0 |
| Carlos | González  |   40 |                 0 |
+--------+-----------+------+-------------------+
3 rows in set (0,00 sec)
