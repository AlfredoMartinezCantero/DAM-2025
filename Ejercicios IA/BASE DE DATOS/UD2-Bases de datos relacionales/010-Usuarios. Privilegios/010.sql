-- Mostrar usuarios en el sistema.
SELECT USER, HOST FROM mysql.user;

-- Crear un nuevo usuario.
CREATE USER 'tunombredeusuario'@'tuservidor' IDENTIFIED BY 'tucontraseña';

GRANT USAGE ON *.* TO 'tunombredeusuario'@'tuservidor';

GRANT ALL PRIVILEGES ON empresadam.* TO 'tunombredeusuario'@'tuservidor';

FLUSH PRIVILEGES;



