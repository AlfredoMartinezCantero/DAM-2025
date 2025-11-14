-- Creación de la vista
CREATE VIEW personas_correos AS
SELECT 
    personas.identificador,
    emails.direccion,
    personas.nombre,
    personas.apellidos
FROM emails
LEFT JOIN personas
ON emails.persona = personas.Identificador;
-- Verificación de la vista
SELECT * FROM personas_correos;