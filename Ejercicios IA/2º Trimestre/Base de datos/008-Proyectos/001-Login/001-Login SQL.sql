-- creamos base de datos
CREATE DATABASE IF NOT EXISTS superaplicacion;
USE superaplicacion;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL, -- Almacenará el HASH, no el texto plano
    nombre_completo VARCHAR(100)
);

-- Insertamos un usuario de prueba (La contraseña es '1234' hasheada)
INSERT INTO usuarios (nombre_usuario, password, nombre_completo) 
VALUES ('admin', '$2y$10$e.g./exampleHashFor1234...', 'Administrador del Sistema');

-- creamos usuario.sql
-- Creamos un usuario específico para la aplicación por seguridad
CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'App_Secure_Pass$2025';
GRANT SELECT, INSERT, UPDATE ON superaplicacion.* TO 'app_user'@'localhost';
FLUSH PRIVILEGES;