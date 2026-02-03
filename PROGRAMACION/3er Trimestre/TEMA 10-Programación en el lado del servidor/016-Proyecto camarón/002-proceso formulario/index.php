<!doctype html>
<html lang="es">
	<head>
  	<title>Camaron viviendas</title>
    <meta charset="utf-8">
  </head>
  <body>
  	<header><h1>Camarón viviendas</h1></header>
    <nav>
    	<form action="?" method="POST">
      	<select name="localidad">
        	<option>Selecciona una localidad...</option>
          <option value="Valencia">Valencia</option>
          <option value="Alboraya">Alboraya</option>
          <option value="Torrent">Torrent</option>
          <option value="Gandía">Gandía</option>
          <option value="Sagunto">Sagunto</option>
          <option value="Paterna">Paterna</option>
          <option value="Burjassot">Burjassot</option>
          <option value="Xàtiva">Xàtiva</option>
          <option value="Cullera">Cullera</option>
        </select>
        <input type="submit">
      </form>
    </nav>
    <main>
    	<section>
      	<?php
          $host = "localhost";
          $user = "camaron";
          $pass = "Camaron123$";
          $db   = "camaron";

          $conexion = new mysqli($host, $user, $pass, $db);
          $resultado = $conexion->query("
            SELECT * FROM viviendas WHERE localidad = '".$_POST['localidad']."';
          ");
          while ($fila = $resultado->fetch_assoc()) {
            echo '
            	<article>
              	<h3>'.$fila['localidad'].'</h3>
                <p>'.$fila['precio'].'</p>
                <p>'.$fila['metroscuadrados'].'</p>
                <p>'.$fila['aniodeconstruccion'].'</p>
                <p>'.$fila['direccion'].'</p>
                <p>'.$fila['altura'].'</p>
                <p>'.$fila['tipodevivienda'].'</p>
                <p>'.$fila['descripcion'].'</p>
                <p>'.$fila['estado'].'</p>
                <p>'.$fila['banios'].'</p>
                <p>'.$fila['habitaciones'].'</p>
                <p>'.$fila['teniente'].'</p>
              </article>
            ';
          }
    		?>
      </section>
    </main>
    <footer>(c) 2026 No me puedo creer que este proyecto se llame Camarón</footer>
  </body>
</html>