Definimos la tabla:
```
CREATE TABLE clientes (
	dni VARCHAR(9),
	nombre VARCHAR(50),
	apellidos VARCHAR(255),
	email VARCHAR(100)
);
```

Insertamos registros:
```
INSERT INTO clientes (dni, nombre, apellidos, email)
VALUES 
('12345678Z', 'Alfredo', 'Martínez Cantero', 'alfredomartinezcantero@gmail.com');
```

--Esta actividad refuerza la idea de que elegir el tipo de dato correcto es esencial para organizar la información de manera efectiva y útil.
--Hay que tener muy en cuenta los datos que se introducen, por ejemplo, si `dni VARCHAR(9)` está definido así, cuando introduzcamos los datos el dni ha de tener 9 caracteres, si tuviera 8 o 10 daría error y no se podría insertar.
--De igual manera tenemos que ser conscientes de que al final de cada parte del código hemos de poner `;` , sino lo hiciéramos al intentar insertar la tabla o lo que queramos insertar nos daría error.