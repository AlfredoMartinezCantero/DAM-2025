/* ===========================================================
   CREACIÓN DE TABLAS
   =========================================================== */

-- 1. Categorías de patos
CREATE TABLE categorias (
    id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT
);

-- 2. Productos (patos de goma)
CREATE TABLE productos (
    id_producto INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    id_categoria INT NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

-- 3. Clientes
CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL, 
    telefono VARCHAR(50),
    direccion TEXT
);

-- 4. Pedidos
CREATE TABLE pedidos (
    id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    fecha_pedido DATETIME NOT NULL,
    estado VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

-- 5. Líneas de pedido
CREATE TABLE lineas_pedido (
    id_linea INT PRIMARY KEY AUTO_INCREMENT,
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- 6. Stock
CREATE TABLE stock (
    id_stock INT PRIMARY KEY AUTO_INCREMENT,
    id_producto INT NOT NULL,
    almacen VARCHAR(100) NOT NULL,
    cantidad INT NOT NULL,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);


/* ===========================================================      VOY POR AQUI
   CREACIÓN DE VISTAS
   =========================================================== */

-- Vista: productos con su categoría
CREATE VIEW vw_productos_categorias AS
SELECT p.id_producto, p.nombre AS producto, p.descripcion, p.precio,
       c.nombre AS categoria
FROM productos p
JOIN categorias c ON p.id_categoria = c.id_categoria;

-- Vista: líneas de pedido con nombres de productos y cliente
CREATE VIEW vw_lineas_detalladas AS
SELECT lp.id_linea, pe.id_pedido, cl.nombre AS cliente,
       pr.nombre AS producto, lp.cantidad, lp.precio_unitario, 
       (lp.cantidad * lp.precio_unitario) AS subtotal
FROM lineas_pedido lp
JOIN pedidos pe ON lp.id_pedido = pe.id_pedido
JOIN clientes cl ON pe.id_cliente = cl.id_cliente
JOIN productos pr ON lp.id_producto = pr.id_producto;

-- Vista: stock de productos con nombres
CREATE VIEW vw_stock_productos AS
SELECT s.id_stock, p.nombre AS producto, s.almacen, s.cantidad
FROM stock s
JOIN productos p ON s.id_producto = p.id_producto;


/* ===========================================================
   INSERCIÓN DE DATOS DE EJEMPLO
   =========================================================== */

-- 1. Categorías
INSERT INTO categorias (nombre, descripcion) VALUES
('Patos Clásicos', 'Patos de goma amarillos tradicionales'),
('Patos Temáticos', 'Patos con disfraces o motivos especiales'),
('Patos de Colección', 'Ediciones limitadas y de coleccionista');

-- 2. Productos (requiere categorías)
INSERT INTO productos (nombre, descripcion, precio, id_categoria) VALUES
('Pato Clásico Amarillo', 'El pato de goma tradicional', 3.99, 1),
('Pato Pirata', 'Pato de goma disfrazado de pirata', 7.49, 2),
('Pato Ninja', 'Pato negro estilo ninja', 6.99, 2),
('Pato Edición Oro', 'Edición limitada bañada en dorado', 29.99, 3);

-- 3. Clientes
INSERT INTO clientes (nombre, email, telefono, direccion) VALUES
('Carlos Pérez', 'carlos@example.com', '600123456', 'Calle Sol 15, Madrid'),
('Laura Gómez', 'laura@example.com', '611987654', 'Av. Luna 42, Barcelona');

-- 4. Pedidos (requiere clientes)
INSERT INTO pedidos (id_cliente, fecha_pedido, estado) VALUES
(1, NOW(), 'Pendiente'),
(2, NOW(), 'Procesado');

-- 5. Líneas de pedido (requiere pedidos y productos)
INSERT INTO lineas_pedido (id_pedido, id_producto, cantidad, precio_unitario) VALUES
(1, 1, 2, 3.99),     -- Carlos compra 2 patos clásicos
(1, 2, 1, 7.49),     -- Carlos compra 1 pato pirata
(2, 4, 1, 29.99),    -- Laura compra 1 pato edición oro
(2, 3, 3, 6.99);     -- Laura compra 3 patos ninja

-- 6. Stock (requiere productos)
INSERT INTO stock (id_producto, almacen, cantidad) VALUES
(1, 'Almacén Central', 120),
(2, 'Almacén Central', 50),
(3, 'Almacén Norte', 35),
(4, 'Almacén Coleccionistas', 10);

