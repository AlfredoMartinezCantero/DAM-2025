<?php
$host = 'localhost';
$db   = 'usuarios_valor_limite'; 
$user = 'root';
$pass = 'AlumnoDAM2025!'; 
$charset = 'utf8mb4';

$dsn = "mysql:host=$host;dbname=$db;charset=$charset";

try {
     $pdo = new PDO($dsn, $user, $pass, [
         PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
         PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
     ]);
} catch (\PDOException $e) {
     die("Error al conectar a la base de datos: " . $e->getMessage());
}