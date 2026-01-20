<?php
// Conexión a la base de datos SQLite
$db = new PDO("sqlite:empresa2026.db");

// Opcional: obtener resultados como arrays asociativos
// $db->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);

$sql = "SELECT * FROM clientes";
$stmt = $db->query($sql);

foreach ($stmt as $row) {
    print_r($row);
}

// Cerrar conexión
$db = null;
