SET @nombre = 'Alfredo';
SET @apellidos = 'Martinez Cantero';
SET @email = 'alfredo@gmail.com';
SET @direccion = 'La calle de Alfredo';

INSERT INTO clientes(
    nombre,
    apellidos,
    email,
    direccion
)
VALUES(
    @nombre,
    @apellidos,
    @email,
    @direccion
);