<?php
    // Inicio la sesión otra vez
    session_start();
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Destino - Perfil</title>
</head>
<body>
    <h1>Perfil del Jugador</h1>
    <p>
        El nombre recuperado de la sesión es: 
        <strong>
            <?php 
                // Verifico si existe la variable para evitar errores
                if(isset($_SESSION['jugador'])){
                    echo $_SESSION['jugador']; 
                } else {
                    echo "No se ha identificado ningún jugador.";
                }
            ?>
        </strong>
    </p>
    
    <p><em>¡Listo para jugar!</em></p>
</body>
</html>