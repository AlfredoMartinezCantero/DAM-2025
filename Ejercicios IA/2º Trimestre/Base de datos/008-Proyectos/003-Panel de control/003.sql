DROP DATABASE IF EXISTS periodico;
CREATE DATABASE periodico;
USE periodico;

CREATE TABLE autores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    fecha_registro DATE DEFAULT (CURRENT_DATE)
);


CREATE TABLE historias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    contenido TEXT,
    fecha_publicacion DATE DEFAULT (CURRENT_DATE),
    autor_id INT,
    CONSTRAINT fk_autor_noticia 
    FOREIGN KEY (autor_id) 
    REFERENCES autores(id) 
    ON DELETE CASCADE 
    ON UPDATE CASCADE
);


INSERT INTO autores (nombre, email) VALUES 
('María López', 'maria.lopez@periodico.com'),
('Carlos Fernández', 'carlos.fernandez@periodico.com'),
('Ana Martínez', 'ana.martinez@periodico.com');


INSERT INTO historias (titulo, contenido, fecha_publicacion, autor_id) VALUES 
('El auge de la IA en 2026', 'La inteligencia artificial sigue transformando el sector tecnológico...', '2026-01-10', 1),
('Avances en energías renovables', 'España lidera la producción de energía solar en el sur de Europa...', '2026-01-11', 2),
('La cultura del teletrabajo', 'Nuevos estudios revelan el impacto del trabajo híbrido en la salud mental...', '2026-01-12', 3),
('Entrevista exclusiva con el Ministro', 'Hablamos sobre las nuevas políticas de educación digital...', '2026-01-13', 1),
('Crisis en el mercado de chips', 'La escasez de semiconductores afecta nuevamente a la industria automotriz...', '2026-01-14', 2);

SELECT 
    historias.titulo, 
    historias.fecha_publicacion, 
    autores.nombre AS 'Escrito por'
FROM historias
JOIN autores ON historias.autor_id = autores.id;