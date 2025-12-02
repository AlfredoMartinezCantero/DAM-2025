CREATE DATABASE IF NOT EXISTS blogphp
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

USE blogphp;

CREATE TABLE IF NOT EXISTS blog (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    contenido TEXT NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    autor VARCHAR(100) DEFAULT 'Administrador'
);

INSERT INTO blog (titulo, contenido, autor) VALUES
('Bienvenidos a mi nuevo blog',
 'Este es el primer artículo del blog. Aquí compartiré tutoriales, noticias y recursos útiles sobre programación y tecnología.',
 'Alfredo Martinez Cantero'),

('Cómo instalar PHP y Apache en Ubuntu',
 'En este artículo aprenderás a instalar un entorno AMP en Ubuntu utilizando los repositorios oficiales y configurando los módulos necesarios.',
 'Alfredo Martinez Cantero'),

('Introducción a SQL para principiantes',
 'SQL es un lenguaje fundamental para trabajar con bases de datos. En esta guía veremos las instrucciones básicas: SELECT, INSERT, UPDATE y DELETE.',
 'Administrador'),

('Consejos para mejorar tu productividad como programador',
 'Organizar el tiempo, dividir el trabajo en tareas pequeñas y mantener un entorno ordenado puede ayudarte a avanzar más rápidamente en tus proyectos.',
 'Administrador');
