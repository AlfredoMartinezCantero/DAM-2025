USE clientes;

SELECT
    ROUND(AVG(edad))    -- Redondeo
FROM clientes;

SELECT
    FLOOR(AVG(edad))    -- Redondeo a la baja
FROM clientes;

SELECT
    CEIL(AVG(edad))     -- Redondeo a la alza
FROM clientes;