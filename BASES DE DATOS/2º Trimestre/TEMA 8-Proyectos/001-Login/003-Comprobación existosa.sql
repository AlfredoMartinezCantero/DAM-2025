SELECT * 
FROM usuarios
WHERE
usuario = 'jlopez'
AND
contrasena = '1234segura';

+----+---------+------------+-----------------------+------------------------+---------------------+
| id | usuario | contrasena | nombrecompleto        | email                  | creado_en           |
+----+---------+------------+-----------------------+------------------------+---------------------+
|  1 | jlopez  | 1234segura | Juan López Martínez   | juan.lopez@example.com | 2025-12-05 10:30:20 |
+----+---------+------------+-----------------------+------------------------+---------------------+
1 row in set (0.00 sec)