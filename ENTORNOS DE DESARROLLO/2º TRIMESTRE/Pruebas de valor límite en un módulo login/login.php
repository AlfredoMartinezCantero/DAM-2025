<?php 
session_start();

// 1. Conexión
require_once '../back/inc/conexion_bd.php'; 

$error = "";

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $correo = $_POST['correo'];
    $pass = $_POST['pass'];

    // Validaciones 
    
    // Mido las longitudes
    $longitudCorreo = strlen($correo);
    $longitudPass = strlen($pass);

    // Validamos el correo
    // Mínimo 5, máximo 20
    if ($longitudCorreo < 5) {
        $error = "El identificador es demasiado corto (mínimo 5 caracteres).";
    } elseif ($longitudCorreo > 20) {
        $error = "El identificador es demasiado largo (máximo 20 caracteres).";
    } 
    // Validamos la contraseña 
    // Mínimo 8, máximo 16
    elseif ($longitudPass < 8) {
        $error = "La contraseña es demasiado corta (mínimo 8 caracteres).";
    } elseif ($longitudPass > 16) {
        $error = "La contraseña es demasiado larga (máximo 16 caracteres).";
    } 
    
    // Solo si no hay errores previos, procedemos a la base de datos
    if (empty($error)) {
        // Buscamos el usuario
        $stmt = $pdo->prepare("SELECT * FROM usuario WHERE correo = ?");
        $stmt->execute([$correo]);
        $user = $stmt->fetch();

        // Verificamos contraseña
        if ($user && password_verify($pass, $user['contrasena'])) {
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['nombre']  = $user['nombre_usuario']; 
            header("Location: carrito.php");
            exit;
        } else {
            $error = "Correo o contraseña incorrectos.";
        }
    }
}
?>