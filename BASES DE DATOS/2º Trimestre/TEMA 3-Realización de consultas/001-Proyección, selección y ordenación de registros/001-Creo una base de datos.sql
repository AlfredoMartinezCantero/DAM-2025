-- sudo mysql -u root -p

CREATE DATABASE clientes;
USE clientes;

CREATE TABLE clientes(
    nombre VARCHAR(255),
    apellidos VARCHAR(255),
    edad INT
);

INSERT INTO clientes VALUES("Juan","Lopez",45);
INSERT INTO clientes VALUES("Javier","Martínez",46);
-- podéis usar IA para crear más inserts
-- 30 clientes adicionales
INSERT INTO clientes VALUES ("Carlos","Gómez",34);
INSERT INTO clientes VALUES ("Ana","Serrano",29);
INSERT INTO clientes VALUES ("María","Hernández",52);
INSERT INTO clientes VALUES ("Luis","Díaz",41);
INSERT INTO clientes VALUES ("Elena","Ramírez",38);
INSERT INTO clientes VALUES ("Pedro","Santos",47);
INSERT INTO clientes VALUES ("Lucía","Pérez",25);
INSERT INTO clientes VALUES ("Raúl","García",33);
INSERT INTO clientes VALUES ("Sofía","Navarro",31);
INSERT INTO clientes VALUES ("Diego","Castro",39);
INSERT INTO clientes VALUES ("Laura","Jiménez",27);
INSERT INTO clientes VALUES ("Adrián","Ruiz",42);
INSERT INTO clientes VALUES ("Marta","Torres",36);
INSERT INTO clientes VALUES ("Alberto","Vargas",48);
INSERT INTO clientes VALUES ("Carmen","Cano",30);
INSERT INTO clientes VALUES ("Fernando","Reyes",55);
INSERT INTO clientes VALUES ("Patricia","Molina",32);
INSERT INTO clientes VALUES ("Sergio","Iglesias",44);
INSERT INTO clientes VALUES ("Rocío","Morales",28);
INSERT INTO clientes VALUES ("Ignacio","Ramos",50);
INSERT INTO clientes VALUES ("Beatriz","Fuentes",26);
INSERT INTO clientes VALUES ("Hugo","Lara",37);
INSERT INTO clientes VALUES ("Natalia","Calvo",35);
INSERT INTO clientes VALUES ("Rubén","Ferrer",40);
INSERT INTO clientes VALUES ("Alicia","Carrasco",24);
INSERT INTO clientes VALUES ("Óscar","León",49);
INSERT INTO clientes VALUES ("Eva","Montoya",53);
INSERT INTO clientes VALUES ("Jorge","Vidal",43);
INSERT INTO clientes VALUES ("Clara","Benítez",22);
INSERT INTO clientes VALUES ("Víctor","Peña",51);
