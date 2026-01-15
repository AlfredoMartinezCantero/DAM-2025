**CREACIÓN DE USUARIO**

# Introducción:
En este bloque del proyecto en lugar de utilizar la cuenta de superusuario por defecto, he configurado el usuario `admin_bara` vinculándolo estrictamente al @localhost, esta es una medida de seguridad esencial, ya que garantiza que el acceso solo sea posible desde la propia máquina donde reside la base de datos, cerrando la puerta a intentos de conexión remotos no autorizados.

Durante el trabajo hemos profundizado en el sistema de privilegios de MySQL, al principio, utilizamos la cláusula `GRANT USAGE sobre *.*`, lo cual permite al usuario entrar al sistema pero sin permisos de lectura o escritura en ninguna tabla.

Después, mediante `ALTER USER`, he configurado restricciones de uso como` MAX_QUERIES_PER_HOUR y MAX_USER_CONNECTIONS`, estableciéndolas en 0 para permitir un flujo ilimitado de trabajo en este entorno de desarrollo.

Finalmente, he otorgado `ALL PRIVILEGES` exclusivamente sobre la base de datos Bar_Bara, asegurando que este usuario tenga control total sobre su proyecto específico sin comprometer otras bases de datos del servidor.

Este comando crea la identidad digital del usuario en el servidor MySQL.
`admin_bara` es el nombre de usuario

`@localhost` es una medida de seguridad, indica que este usuario solo tiene permitido conectarse si la conexión se realiza desde la misma máquina donde está la base de datos.

`IDENTIFIED BY` asigna la contraseña, en este caso `BarBara_2025$`.

---
```
CREATE USER 
'admin_bara'@'localhost'
IDENTIFIED  BY 'BarBara_2025$';
```
---

`GRANT USAGE ON...` otorga el permiso de conectarse al servidor sin poder hacer nada más, ni leer, ni escribir, ni borrar.

`*.*` esto significa "en todas las bbdd y tablas pero al poner `USAGE` solo dejamos que entre al "pasillo" pero las "puertas" siguen cerradas.

---
```
GRANT USAGE ON *.* TO 'admin_bara'@'localhost';
```
---

Aquí se modifican las restricciones de uso del usuario.

`REQUIRE NONE` hace que no se exija una conexión encriptada.

El uso de los `0` es quitar el límite de acceso, es decir, que el usuario creado puede hacer consultas, actualizaciones y conexiones infinitas.

---
```
ALTER USER 'admin_bara'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;
```
---

Por último, este comando le da las "llaves" de las "puertas" para la base de datos `Bar_Bara`.

`ALL PRIVILEGES` permite hacer `SELECT, INSERT, UPDATE, DEETE, CREATE, DROP, etc.`

Y `FLUSH PRIVILEGES;` obliga al servidor a recargar la tabla de permisos en la RAM, sin este comando los cambios podrían no tener efecto inmediato hasta que se reiniciase el servicio.

---
```
GRANT ALL PRIVILEGES ON Bar_Bara.* 
TO 'admin_bara'@'localhost';

FLUSH PRIVILEGES;
```
```
mysql> SELECT * FROM usuario;
+----+----------------+------------------+-------------------+--------------------------------------------------------------+
| id | nombre_usuario | apellidos        | correo            | contrasena                                                   |
+----+----------------+------------------+-------------------+--------------------------------------------------------------+
|  1 | Alfredo        | Martinez Cantero | alfredo@gmail.com | $2y$10$Wtpuaf8TIOP..3uuB4pBd.dybriXaGlW3xEZuMGhYayJPpG3Ecg56 |
|  2 | Alfredo        | Martinez Cantero | alfredo@gmail.com | $2y$10$LSqaENFVMGtOQ4BrtK1EP.kWlomQ.Sa693RbRh9IMPYT/Is.odzZi |
|  3 | Pedro          | Perez            | pedro@gmail.com   | $2y$10$9wHlDY6Dr0lDkOVOF7UqsuPwa1sNxdFhWdej0my0zrq7zuVxzrgxa |
+----+----------------+------------------+-------------------+--------------------------------------------------------------+
```
---
# Conclusión:
Con esta parte del código mi compañera y yo hemos aprendido a gestionar la seguridad de acceso en un servidor de bases de datos, separando la creación del usuario de la asignación de sus permisos específicos mediante comandos como `GRANT ALL PRIVILEGES`, puedo otorgar un control total sobre una base de datos concreta, mientras que con `ALTER USER` y sus parámetros `MAX_QUERIES_PER_HOUR` o `MAX_CONNECTIONS_PER_HOUR` establecemos límites de recursos para evitar abusos o ataques.

Un error frecuente es que siempre que se modifiquen permisos a mano en las tablas de MySQL, los cambios no se aplican hasta que ejecute `FLUSH PRIVILEGES`, lo que podría hacerme perder mucho tiempo buscando errores de conexión inexistentes.

---
**PRODUCTOS**

# Introducción:
En esta parte del trabajo hemos aprendido a automatizar el proceso de poblado de datos en una base de datos relacional utilizando sentencias SQL con ayuda de IA.

`INSERT INTO producto (id, nombre_producto, precio, descripcion, categoria, imagen) VALUES` este comando es el estándar para poblar una tabla, lo que se encuentra entre paréntesis es la lista de destino.

Estas tienen un mapeo posicional 1 a 1, es decir, el 1 va a la columna `id(INT)`, `Cerveza Lager` va a `nombre_producto(VARCHAR)` y `2.50` va a `precio(DECIMAL)`.

En lugar de escribir 100 veces `INSERT INTO` se escribe todo en una sola sentencia separadas por comas.

El script inserta productos agrupados por su columna `categoria`, por ejemplo:
`'Cervezas' (ID 1-10)`
`'Vinos' (ID 11-20)`

---
```
INSERT INTO producto (id, nombre_producto, precio, descripcion, categoria, imagen) VALUES
-- CERVEZAS
(1, 'Cerveza Lager', 2.50, 'Agua, malta de cebada, maíz, lúpulo', 'Cervezas', 'cerveza.jpg'),
(2, 'Cerveza IPA', 4.50, 'Agua, malta de cebada, lúpulo Citra, levadura Ale', 'Cervezas', 'cerveza.jpg'),
(3, 'Cerveza de Trigo', 4.00, 'Agua, malta de trigo, malta de cebada, lúpulo, levadura', 'Cervezas', 'cerveza.jpg'),
(4, 'Cerveza Negra', 4.20, 'Agua, cebada tostada, lúpulo, levadura', 'Cervezas', 'cerveza.jpg'),
(5, 'Cerveza Sin Alcohol', 3.00, 'Agua, malta de cebada, lúpulo, aromas naturales', 'Cervezas', 'cerveza.jpg'),
(6, 'Cerveza Radler', 2.80, 'Cerveza lager, zumo de limón natural, azúcar', 'Cervezas', 'cerveza.jpg'),
(7, 'Cerveza Artesana Roja', 5.00, 'Agua, maltas caramelizadas, lúpulo, levadura', 'Cervezas', 'cerveza.jpg'),
(8, 'Cerveza de Abadía', 6.00, 'Agua, malta de cebada, jarabe de glucosa, lúpulo', 'Cervezas', 'cerveza.jpg'),
(9, 'Cerveza Doble Malta', 4.50, 'Agua, exceso de malta de cebada, lúpulo', 'Cervezas', 'cerveza.jpg'),
(10, 'Cerveza Pilsen', 2.50, 'Agua, malta de cebada, lúpulo de Saaz', 'Cervezas', 'cerveza.jpg'),

-- VINOS Y VERMUT
(11, 'Vino Tinto Crianza', 3.50, 'Uva Tempranillo, sulfitos', 'Vinos', 'vinos.jpeg'),
(12, 'Vino Blanco Rueda', 3.00, 'Uva Verdejo, sulfitos', 'Vinos', 'vinos.jpeg'),
(13, 'Vino Rosado', 3.00, 'Uva Garnacha tinta, sulfitos', 'Vinos', 'vinos.jpeg'),
(14, 'Vino Albariño', 4.00, 'Uva Albariño 100%, sulfitos', 'Vinos', 'vinos.jpeg'),
(15, 'Copa de Cava', 4.50, 'Uva Macabeo, Parellada, Xarel·lo, sulfitos', 'Vinos', 'vinos.jpeg'),

etc.

SELECT * FROM producto;
+-----+-----------------------+--------+-----------------------------------------------------------+------------+---------------+
| id  | nombre_producto       | precio | descripcion                                               | categoria  | imagen        |
+-----+-----------------------+--------+-----------------------------------------------------------+------------+---------------+
|   1 | Cerveza Lager         |   2.50 | Agua, malta de cebada, maíz, lúpulo                       | Cervezas   | cerveza.jpg   |
|   2 | Cerveza IPA           |   4.50 | Agua, malta de cebada, lúpulo Citra, levadura Ale         | Cervezas   | cerveza.jpg   |
|   3 | Cerveza de Trigo      |   4.00 | Agua, malta de trigo, malta de cebada, lúpulo, levadura   | Cervezas   | cerveza.jpg   |
|   4 | Cerveza Negra         |   4.20 | Agua, cebada tostada, lúpulo, levadura                    | Cervezas   | cerveza.jpg   |
|   5 | Cerveza Sin Alcohol   |   3.00 | Agua, malta de cebada, lúpulo, aromas naturales           | Cervezas   | cerveza.jpg   |
|   6 | Cerveza Radler        |   2.80 | Cerveza lager, zumo de limón natural, azúcar              | Cervezas   | cerveza.jpg   |
|   7 | Cerveza Artesana Roja |   5.00 | Agua, maltas caramelizadas, lúpulo, levadura              | Cervezas   | cerveza.jpg   |
|   8 | Cerveza de Abadía     |   6.00 | Agua, malta de cebada, jarabe de glucosa, lúpulo          | Cervezas   | cerveza.jpg   |
|   9 | Cerveza Doble Malta   |   4.50 | Agua, exceso de malta de cebada, lúpulo                   | Cervezas   | cerveza.jpg   |
|  10 | Cerveza Pilsen        |   2.50 | Agua, malta de cebada, lúpulo de Saaz                     | Cervezas   | cerveza.jpg   |

```
---
# Conclusión:
Con este trabajo hemos creado la base del catálogo de productos, aprendiendo que la inserción masiva es la forma más profesional y eficiente de inicializar tablas con grandes volúmenes de datos.

Un error común es cometer fallos de sintaxis en el mapeo posicional, como olvidar una coma entre registros o intentar insertar una cadena de texto en una columna definida como INT.

---
**CREACIÓN DE TABLAS**

# Introducción:
En este bloque del trabajo mi compañera y yo hemos diseñado y estructurado una base de datos relacional, hemos utilizado el comando `CREATE TABLE` para generar entidades robustas como usuario, pedido y producto. 

Para garantizar la precisión en los datos numéricos, implementamos el tipo `DECIMAL(10,2)`, evitando así los errores de redondeo que suelen surgir al utilizar tipos de coma flotante como `FLOAT`.

Para asegurar la integridad de la información, configuramos relaciones mediante `CONSTRAINT y FOREIGN KEY`.
Del mismo modo, estructuramos la tabla `contenido_pedido` como una entidad de detalle que conecta cada pedido con sus respectivos productos, permitiendo un desglose exacto de las ventas.

`CREATE TABLE` este comando genera una nueva entidad
`INT` para números enteros (IDs, cantidades, números de mesa en este caso, etc.)
`VARCHAR(255)` para texto variable (nombres, correos, etc.)
`DECIMAL(10,2) y DECIMAL(4,2)` esto guarda números con exactitud de dos decimales, para evitar errores de redondeo que ocurrirían si usaramos `FLOAT`
`PRIMARY KEY (id)` define que el campo `id` es único e irrepetible.

El comandos de `CONSTRAINT fk_pedido_1 FOREIGN KEY (usuario_id) REFERENCES usuario(id)` obliga a que el dato introducido en `usuario` de la tabla `pedido` exista previamente, si no fuese asi la base de datos rechazaría crear un pedido para un usuario fantasma.


`CONSTRAINT fk_contenido_pedido_1 FOREIGN KEY (pedido_id) REFERENCES pedido(id)` vincula el contenido con el pedido, en el caso de borrarlo, esta relación ayuda a mantener el orden.

---
```
CREATE TABLE usuario (
  id INT NOT NULL,
  nombre_usuario VARCHAR(255),
  apellidos VARCHAR(255),
  correo VARCHAR(255),
  contrasena VARCHAR(255),
  PRIMARY KEY (id)
);

CREATE TABLE pedido (
  id INT NOT NULL,
  usuario_id INT,
  numero_mesa INT,
  fecha VARCHAR(255),
  hora VARCHAR(255),
  productos VARCHAR(255),
  cantidad_producto INT,
  total DECIMAL(10,2),
  pedir_cuenta VARCHAR(255),
  PRIMARY KEY (id),
  CONSTRAINT fk_pedido_1 FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);

CREATE TABLE producto (
  id INT NOT NULL,
  nombre_producto VARCHAR(255),
  precio DECIMAL(4,2),
  descripcion VARCHAR(255),
  categoria VARCHAR(255),
  imagen VARCHAR(255),
  PRIMARY KEY (id)
);

CREATE TABLE contenido_pedido (
  id INT NOT NULL,
  pedido_id INT,
  cantidad INT,
  subtotal DECIMAL(10,2),
  producto_id INT,
  PRIMARY KEY (id),
  CONSTRAINT fk_contenido_pedido_1 FOREIGN KEY (pedido_id) REFERENCES pedido(id),
  CONSTRAINT fk_contenido_pedido_2 FOREIGN KEY (producto_id) REFERENCES producto(id)
);
```
---
# Conclusión:
Con esta parte del código mi compañera y yo consolidamos la base del sistema de persistencia, asegurando que cada tabla cumpla con una función específica sin duplicar información innecesariamente. Aprendimos en el proceso que el uso de `AUTO_INCREMENT` en las claves primarias facilita enormemente la inserción de nuevos registros, ya que delegamos en el motor de la base de datos la gestión de los identificadores únicos.

Un error común que puede surgir es que si dejamos las credenciales visibles dentro de los scripts lógicos de PHP, se pone en riesgo la seguridad de todo el sistema. Por ello, es crítico mover variables como `$pass` a un archivo `config.php` externo y protegido.
En este caso como es un proyecto en `localhost` de clase sabemos que podemos hacer esto pero de cara a las empresas o cosas que quisieramos publicar deberíamos  seguir los pasos que he mencionado anteriormente.