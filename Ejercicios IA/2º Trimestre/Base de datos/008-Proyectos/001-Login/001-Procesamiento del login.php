<?php
session_start(); // Iniciamos el motor de sesiones

$host = "localhost";
$user = "app_user";
$pass = "App_Secure_Pass$2025";
$db   = "superaplicacion";

$conexion = new mysqli($host, $user, $pass, $db);

if ($conexion->connect_error) {
    die("Error de conexión: " . $conexion->connect_error);
}

// Recogemos los datos del formulario de forma segura
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $usuario = $_POST['usuario'];
    $password_ingresada = $_POST['password'];

    $sql = "SELECT id, nombre_usuario, password FROM usuarios WHERE nombre_usuario = ?";
    
    $stmt = $conexion->prepare($sql);
    $stmt->bind_param("s", $usuario);
    $stmt->execute();
    $resultado = $stmt->get_result();

    if ($fila = $resultado->fetch_assoc()) {
        // Verificamos la contraseña hasheada
        if (password_verify($password_ingresada, $fila['password'])) {
            // LOGIN EXITOSO: Creamos la sesión
            $_SESSION['usuario'] = $fila['nombre_usuario'];
            $_SESSION['id'] = $fila['id'];
            
            // Redirigimos a la zona privada
            header("Location: exito.php");
            exit(); 
        } else {
            // Contraseña incorrecta
            echo "Error: Credenciales inválidas.";
        }
    } else {
        // Usuario no encontrado
        echo "Error: El usuario no existe.";
    }

    $stmt->close();
}
$conexion->close();
?>