<?php

// Conecta a la base de datos
$host = "localhost";
$user = "empleados";
$pass = "Empleados123$";
$db   = "empleados";

$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Obtiene el ID del empleado a actualizar
$id = $_POST['id'];

// Actualiza la información de la base de datos
$sql = "
    UPDATE empleados SET
        nombre = '".$$_POST['nombre']."',
        puesto = '".$$_POST['puesto']."',
        salario = '".$$_POST['salario']."',
        fecha_contratacion = '".$$_POST['fecha_contratacion']."',
        departamento = '".$$_POST['departamento']."' 
    WHERE id = ".$id."
";
$conn->query($sql);

// Cierra la conexión
$conn->close();

?>