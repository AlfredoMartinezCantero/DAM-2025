-- Conectar a la base de datos
sudo mysql -u root -p
-- Seleccionar la base de datos
USE empresadam;
-- Mostrar las tablas disponibles
SHOW TABLES;
-- Describir la tabla artistas
DESCRIBE artistas;
-- Se añade una clave primaria a la tabla artistas
ALTER TABLE artistas
ADD COLUMN id_artista INT AUTO_INCREMENT PRIMARY KEY FIRST;
-- Se inserta un nuevo artista
INSERT INTO artistas (nombre, genero)
VALUES ('Extremoduro', 'Electronica');
-- Verifica los datos insertados
SELECT * FROM artistas;

