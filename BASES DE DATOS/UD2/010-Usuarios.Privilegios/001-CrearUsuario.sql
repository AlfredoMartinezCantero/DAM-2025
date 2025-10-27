-- crea usuario nuevo con contraseña nueva
-- creamos el nombre de usuario que queramos
CREATE USER
'alfredo'@'localhost'
IDENTIFIED  BY 'Alfredo7?';
-- permite acceso a ese usuario
GRANT USAGE ON *.* TO 'alfredo'@'localhost';

-- quitale todos los limites que tenga
ALTER USER 'alfredo'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON empresaDAM.*  
TO 'alfredo'@'localhost';

-- recarga la tabla de privilegios
FLUSH PRIVILEGES;
