SELECT COUNT(color)
FROM productos; --resumen del otro dia

SELECT COUNT(color),color
FROM productos
GROUP BY color
ORDER BY count(color) ASC;

+--------------+----------+
| COUNT(color) | color    |
+--------------+----------+
|            1 | Rojo     |
|            1 | Morado   |
|            2 | Marrón   |
|            2 | Plateado |
|            3 | Gris     |
|            3 | Azul     |
|            9 | Blanco   |
|           12 | Negro    |
+--------------+----------+