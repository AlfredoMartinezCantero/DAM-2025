-- Revisar la estructura de una tabla existente.
DESCRIBE clientes;

-- Añadir una nueva columna y eliminarla.
ALTER TABLE clientes
ADD COLUMN direccion VARCHAR(255)

DESCRIBE clientes;

-- Elimina la columna direccion.
ALTER TABLE clientes 
DROP COLUMN direccion;

DESCRIBE clientes

-- Renombrar una columna y gestionar restricciones.
ALTER TABLE clientes 
DROP CONSTRAINT comprobar_dni_nie_letra;

ALTER TABLE clientes
RENAME COLUMN dni TO dninie;

DESCRIBE clientes;

-- Añadir una nueva restricción.
ALTER TABLE clientes
  ADD CONSTRAINT comprobar_dni_nie_letra
  CHECK (
    (
      /* DNI: 8 dígitos + letra */
      dninie REGEXP '^[0-9]{8}[A-Za-z]$'
      AND
      UPPER(SUBSTRING(dninie, 9, 1)) =
      SUBSTRING('TRWAGMYFPDXBNJZSQVHLCKE',
                (CAST(SUBSTRING(dninie, 1, 8) AS UNSIGNED) MOD 23) + 1,
                1)
    )
    OR
    (
      /* NIE: X/Y/Z + 7 dígitos + letra */
      dninie REGEXP '^[XYZxyz][0-9]{7}[A-Za-z]$'
      AND
      UPPER(SUBSTRING(dninie, 9, 1)) =
      SUBSTRING('TRWAGMYFPDXBNJZSQVHLCKE',
                (
                  CAST(CONCAT(
                        CASE UPPER(SUBSTRING(dninie, 1, 1))
                          WHEN 'X' THEN '0'
                          WHEN 'Y' THEN '1'
                          WHEN 'Z' THEN '2'
                        END,
                        SUBSTRING(dninie, 2, 7)
                  ) AS UNSIGNED) MOD 23
                ) + 1,
                1)
    )
  );

-- Insertar registros y verificar restricciones.
INSERT INTO clientes VALUES (
  NULL,
  '12345678Z'
  'Alfredo'
  'Martínez Cantero'
  'alfredomartinezcantero@gmail.com'
);

-- Vaciar y truncar la tabla.
DELETE FROM clientes;

SELECT * FROM clientes;

TRUNCATE TABLE clientes;

-- Crear una nueva tabla con restricciones.
CREATE TABLE productos (
  Identificador INTEGER PRIMARY KEY AUTOINCREMENT,
  Nombre VARCHAR(255) NOT NULL,
  Descripcion TEXT,
  Precio DECIMAL(7,2) NOT NULL,
  Stock INT NOT NULL,
  CONSTRAINT chk_stock_non_negative CHECK (Stock >= 0),
  CONSTRAINT chk_precio_range CHECK (Precio >= 0 AND Precio <= 5000),
  CONSTRAINT chk_nombre_length CHECK (LENGTH(Nombre) >= 5)
);

-- Insertar registros en la tabla productos.
INSERT INTO productos (Nombre, Descripcion, Precio, Stock) VALUES
('Producto A', 'Descripción del Producto A', 150.00, 10),
('Producto B', 'Descripción del Producto B', 3000.00, 5),
('Prod C', 'Descripción del Producto C', 6000.00, 3), -- Esto debería fallar por el precio
('Producto D', 'Descripción del Producto D', 250.00, -2); -- Esto debería fallar por el stock
