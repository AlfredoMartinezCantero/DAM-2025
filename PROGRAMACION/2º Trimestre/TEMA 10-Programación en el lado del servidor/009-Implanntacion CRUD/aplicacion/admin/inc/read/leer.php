<?php
	session_start(); // Arranco una sesion
  $host = "localhost";
  $user = "periodico";
  $pass = "Periodico123$";
  $db   = "periodico";

  $conexion = new mysqli($host, $user, $pass, $db);
  
	// Comprobacion exitosa pero mirando los datos que vienen del formulario en POST
  $sql = "
  	SELECT * FROM noticias;
  ";
	
  $resultado = $conexion->query($sql);
  while ($fila = $resultado->fetch_assoc()) {
  	var_dump($fila);			// Vomito en pantalla y ya luego formateare
  }
	
  	
  $conexion->close();
  
?>