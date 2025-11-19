SELECT COUNT(color)
FROM productos; --resumen del otro dia

SELECT COUNT(color),color
FROM productos
GROUP BY color;