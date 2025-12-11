<!doctype html>
<html lang="es">
	<head>
  	<title>El AAMC - Noticias tecnológicas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="css/estilo.css">
  </head>
  <body>
  	<header>
    	<h1>El AAMC</h1>
      <h2>Noticias tecnológicas</h2>
    </header>
    <main>
    	<?php
        $host = "localhost";
        $user = "periodico";
        $pass = "Periodico123$";
        $db   = "periodico";
        $conexion = new mysqli($host, $user, $pass, $db);
        $sql = "SELECT * FROM noticias";
        $resultado = $conexion->query($sql);
        while ($fila = $resultado->fetch_assoc()) {
          echo '
            <article>
              <h3>'.$fila['titulo'].'</h3>
              <time>'.$fila['fecha_publicacion'].'</time>
              <p>'.$fila['autor_id'].'</p>
              <p>'.$fila['contenido'].'</p>
            </article>
          ';
        }
        $conexion->close();
      ?>
    </main>
    <footer>
    </footer>
  </body>
</html>