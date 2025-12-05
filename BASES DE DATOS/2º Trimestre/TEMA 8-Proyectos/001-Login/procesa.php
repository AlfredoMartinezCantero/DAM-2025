<?php

  $host = "localhost";
  $user = "superaplicacion";
  $pass = "Superaplicacion123$";
  $db   = "superaplicacion";

  $conexion = new mysqli($host, $user, $pass, $db);
  
	// Comprobacion exitosa pero mirando los datos que vienen del formulario en POST
  $sql = "
  	SELECT 
    *
    FROM usuarios
    WHERE
    usuario = '".$_POST['usuario']."'
    AND
    contrasena = '".$_POST['contrasena']."';
  ";

  $resultado = $conexion->query($sql);

  if ($fila = $resultado->fetch_assoc()) {
    header("exito.php");
  }else{
  	header("login.html");
  }

  $conexion->close();
  
?>