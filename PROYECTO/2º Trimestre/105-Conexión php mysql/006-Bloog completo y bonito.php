<!doctype html>
<html>
	<head>
  </head>
  <body>
  	<header>
    	<h1>Alfredo Martinez Cantero</h1>
      <h2>Blog superinteresante</h2>
    </header>
    <main>
      <?php

        $host = "localhost";
        $user = "blogphp";
        $pass = "Blogphp123$";
        $db   = "blogphp";

        $conexion = new mysqli($host, $user, $pass, $db);

        $sql = "SELECT * FROM blog";

        $resultado = $conexion->query($sql);

        while ($fila = $resultado->fetch_assoc()) {
          echo '
            <article>
              <h3>'.$fila['titulo'].'</h3>
              <time>'.$fila['fecha'].'</time>
              <p>'.$fila['autor'].'</p>
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


