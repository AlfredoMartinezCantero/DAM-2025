<?php
session_start();

// Si la variable 'usuario' no está definida en la sesión, expulsamos al visitante.
if (!isset($_SESSION['usuario'])) {
    echo "<h1>ACCESO DENEGADO</h1>";
    echo "<p>Has intentado colar, pero el sistema de sesiones te ha detectado.</p>";
    echo "<a href='index.html'>Volver al Login</a>";
    // Detenemos la ejecución del script para que no se cargue nada más
    exit(); 
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Panel de Control</title>
</head>
<body>
    <h1>¡Bienvenido, <?php echo htmlspecialchars($_SESSION['usuario']); ?>!</h1>
    <p>Has iniciado sesión con éxito en la SuperAplicación.</p>
    
    <hr>
    <a href="logout.php">Cerrar Sesión</a>
</body>
</html>