SELECT

nombre AS 'Nombre del cliente',
apellidos AS 'Apellidos del cliente',
edad AS 'Edad del cliente'

FROM 

clientes

ORDER BY
apellidos ASC;  

-- El resultado es el mismo pero le indicamos nosotros que es lo que queremos y no lo dejamos por defecto

+--------------------+-----------------------+------------------+
| Nombre del cliente | Apellidos del cliente | Edad del cliente |
+--------------------+-----------------------+------------------+
| Clara              | Benítez               |               22 |
| Natalia            | Calvo                 |               35 |
| Carmen             | Cano                  |               30 |
| Alicia             | Carrasco              |               24 |
| Diego              | Castro                |               39 |
| Luis               | Díaz                  |               41 |
| Rubén              | Ferrer                |               40 |
| Beatriz            | Fuentes               |               26 |
| Raúl               | García                |               33 |
| Carlos             | Gómez                 |               34 |
| María              | Hernández             |               52 |
| Sergio             | Iglesias              |               44 |
| Laura              | Jiménez               |               27 |
| Hugo               | Lara                  |               37 |
| Óscar              | León                  |               49 |
| Juan               | Lopez                 |               45 |
| Javier             | Martínez              |               46 |
| Patricia           | Molina                |               32 |
| Eva                | Montoya               |               53 |
| Rocío              | Morales               |               28 |
| Sofía              | Navarro               |               31 |
| Víctor             | Peña                  |               51 |
| Lucía              | Pérez                 |               25 |
| Elena              | Ramírez               |               38 |
| Ignacio            | Ramos                 |               50 |
| Fernando           | Reyes                 |               55 |
| Adrián             | Ruiz                  |               42 |
| Pedro              | Santos                |               47 |
| Ana                | Serrano               |               29 |
| Marta              | Torres                |               36 |
| Alberto            | Vargas                |               48 |
| Jorge              | Vidal                 |               43 |
+--------------------+-----------------------+------------------+