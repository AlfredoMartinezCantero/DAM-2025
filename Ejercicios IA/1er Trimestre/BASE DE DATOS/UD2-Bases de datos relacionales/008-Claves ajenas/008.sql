-- Crear las tablas "personas" y "emails".
CREATE TABLE personas(
    Identificador INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Apellidos VARCHAR(50)
);

CREATE TABLE emails(
    ID INT PRIMARY KEY,
    persona INT,
    email VARCHAR(100),
    FOREIGN KEY (persona) REFERENCES personas(Identificador)
);

-- Insertar un registro en la tabla "personas".
INSERT INTO personas (Identificador, Nombre, Apellidos)
VALUES (1, 'Alfredo', 'Martínez Cantero');

-- Insertar varios registros en la tabla "emails".
INSERT INTO emails (ID, persona, email)
VALUES 
(1, 1, 'alfredo@gmail.com'), 
(2, 1, 'alfredomartinezcantero@gmail.com');

-- Realizar una petición cruzada para obtener los correos electrónicos junto con el nombre y apellidos.
SELECT 
    p.Nombre,
    p.Apellidos,
    e.email
FROM 
    personas p
JOIN 
    emails e
ON 
    p.Identificador = e.persona;
