<?php
	// Esto ha empezado siendo un copia pega de eliminar y ahora lo editamos
  
    // Primero recojo lo que viene del formulario
    $titulo = $_POST['titulo'];	
    $contenido = $_POST['contenido'];	
    $fecha_publicacion = $_POST['fecha_publicacion'];	
    $autor_id = $_POST['autor_id'];	
    $id = $_POST['id'];																
        
    // Ahora me conecto a la base de datos
    $host = "localhost";															
    $user = "periodico";
    $pass = "Periodico123$";
    $db   = "periodico";

    $conexion = new mysqli($host, $user, $pass, $db);	// Ejecuto la conexion

    // Le lanzo una peticion de actualización
    $sql = "
        UPDATE noticias
        SET 
        titulo = '".$titulo."',
        contenido = '".$contenido."',
        fecha_publicacion = '".$fecha_publicacion."',
        autor_id = ".$autor_id."
        WHERE id = ".$id.";
    ";																							
    echo $sql;
    $conexion->query($sql);							
        
    // Y cierro y vuelvo
    $conexion->close();																
    header("Location: ../../escritorio.php");
  
?>