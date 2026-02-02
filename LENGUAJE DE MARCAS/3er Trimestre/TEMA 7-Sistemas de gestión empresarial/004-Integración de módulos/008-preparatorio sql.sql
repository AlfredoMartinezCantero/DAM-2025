sudo mysql -u root -p

CREATE DATABASE microtienda;
USE microtienda;

CREATE TABLE productos(
    nombre VARCHAR(255),
    descripcion TEXT,
    precio INT(255)
);


INSERT INTO productos VALUES(
	'Zapatillas',
    'Zapatillas chulas de deporte',
    30
);

INSERT INTO productos (nombre, descripcion, precio) VALUES
('Camiseta Algodón', 'Camiseta básica 100% algodón, color blanco', 15),
('Pantalones Vaqueros', 'Vaqueros de corte recto, azul clásico', 40),
('Sudadera con Capucha', 'Sudadera urbana con forro polar interior', 35),
('Gorra Deportiva', 'Gorra ajustable con visera curva', 12),
('Reloj Inteligente', 'Smartwatch con monitor de ritmo cardíaco', 120),
('Auriculares Bluetooth', 'Auriculares inalámbricos con cancelación de ruido', 85),
('Mochila Ejecutiva', 'Mochila con compartimento acolchado para portátil', 50),
('Ratón Gaming', 'Ratón ergonómico con luces RGB y 3200 DPI', 25),
('Teclado Mecánico', 'Teclado retroiluminado con switches rojos', 70),
('Gafas de Sol', 'Gafas con protección UV400 y montura de pasta', 20);