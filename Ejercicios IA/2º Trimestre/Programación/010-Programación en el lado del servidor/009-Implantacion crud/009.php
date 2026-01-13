<?php
    $host = "localhost";
    $user = "periodico";
    $pass = "Periodico123$";  
    $db   = "periodico";

    $conexion = new mysqli($host, $user, $pass, $db);

    if ($conexion->connect_error) {
        die("Error de conexión: " . $conexion->connect_error);
    }

    $conexion->set_charset("utf8");

    $sql = "SELECT * FROM noticias";
    $resultado = $conexion->query($sql);

    while ($fila = $resultado->fetch_assoc()) {
        echo '<article>';
        echo '  <h3>' . $fila['titulo'] . '</h3>';
        echo '  <time>' . $fila['fecha_publicacion'] . '</time>';
        echo '  <p>' . $fila['contenido'] . '</p>';
        echo '</article>';
    }

    $conexion->close();
?>