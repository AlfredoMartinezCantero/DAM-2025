-- Tabla de Clientes
CREATE TABLE Cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE
);

-- Tabla de Pedidos
CREATE TABLE Pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    cliente_id INT NOT NULL,
    CONSTRAINT fk_pedido_cliente 
        FOREIGN KEY (cliente_id) REFERENCES Cliente(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- Tabla LineaPedido
CREATE TABLE LineaPedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL DEFAULT 1,
    CONSTRAINT fk_linea_pedido 
        FOREIGN KEY (pedido_id) REFERENCES Pedido(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_linea_producto 
        FOREIGN KEY (producto_id) REFERENCES Producto(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- Tabla de Productos
CREATE TABLE Producto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL CHECK (precio >= 0)
);