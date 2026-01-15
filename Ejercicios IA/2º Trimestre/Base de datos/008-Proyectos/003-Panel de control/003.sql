-- 1. Creación de la base de datos y selección
DROP DATABASE IF EXISTS periodico;
CREATE DATABASE periodico;
USE periodico;

-- 2. Creación de la tabla independiente (Autores)
CREATE TABLE autores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    fecha_registro DATE DEFAULT (CURRENT_DATE)
);

-- 3. Creación de la tabla dependiente (Historias/Noticias)
CREATE TABLE historias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    contenido TEXT,
    fecha_publicacion DATE DEFAULT (CURRENT_DATE),
    autor_id INT,
    -- Definición de la relación: Si se borra el autor, se borran sus noticias (CASCADE)
    CONSTRAINT fk_autor_noticia 
    FOREIGN KEY (autor_id) 
    REFERENCES autores(id) 
    ON DELETE CASCADE 
    ON UPDATE CASCADE
);

-- 4. Inserción de datos: Autores
-- Es importante insertarlos primero para generar los IDs 1, 2 y 3.
INSERT INTO autores (nombre, email) VALUES 
('María López', 'maria.lopez@periodico.com'),
('Carlos Fernández', 'carlos.fernandez@periodico.com'),
('Ana Martínez', 'ana.martinez@periodico.com');

-- 5. Inserción de datos: Historias de prueba
-- Asocio cada noticia al ID del autor correspondiente
INSERT INTO historias (titulo, contenido, fecha_publicacion, autor_id) VALUES 
('El auge de la IA en 2026', 'La inteligencia artificial sigue transformando el sector tecnológico...', '2026-01-10', 1),
('Avances en energías renovables', 'España lidera la producción de energía solar en el sur de Europa...', '2026-01-11', 2),
('La cultura del teletrabajo', 'Nuevos estudios revelan el impacto del trabajo híbrido en la salud mental...', '2026-01-12', 3),
('Entrevista exclusiva con el Ministro', 'Hablamos sobre las nuevas políticas de educación digital...', '2026-01-13', 1),
('Crisis en el mercado de chips', 'La escasez de semiconductores afecta nuevamente a la industria automotriz...', '2026-01-14', 2);

-- 6. Comprobación visual (JOIN para ver nombres en lugar de IDs)
SELECT 
    historias.titulo, 
    historias.fecha_publicacion, 
    autores.nombre AS 'Escrito por'
FROM historias
JOIN autores ON historias.autor_id = autores.id;