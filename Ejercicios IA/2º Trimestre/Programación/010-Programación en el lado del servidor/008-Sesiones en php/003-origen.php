<?php
    // Inicio una sesión
    session_start();

    // Declaro la variable localmente
    $nombre = "Jose Vicente";

    // Guardo el valor de la sesión
    $_SESSION['jugador'] = $nombre;
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Origen - Shooter</title>
</head>
<body>
    <h1>Configuración de Jugador</h1>
    <p>El jugador <?php echo $nombre; ?> ha sido registrado en la sesión.</p>
    
    <a href="004-destino.php">Ir a ver el perfil del jugador</a>
</body>
</html>