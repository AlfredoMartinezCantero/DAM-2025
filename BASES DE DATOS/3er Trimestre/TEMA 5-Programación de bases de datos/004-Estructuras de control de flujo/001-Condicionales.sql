DELIMITER //

CREATE PROCEDURE insertar()
BEGIN

    IF (SELECT COUNT(*) 
        FROM clientes 
        WHERE email='alfredo@gmail.com') = 0
    THEN
        INSERT INTO clientes
        VALUES(
            NULL,
            'Alfredo',
            'Martinez Cantero',
            'alfredo@gmail.com',
            'La calle de Alfredo'
        );
    END IF;

END //

DELIMITER ;