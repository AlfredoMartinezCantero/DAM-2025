<!doctype html>
<html lang="es">
	<head>
  	<title>Camaron viviendas</title>
    <meta charset="utf-8">
    <style>
    body { font-family: sans-serif; background: #f0f2f5; margin: 0; color: #333; }
    header { background: #1a252f; color: white; padding: 10px 20px; display: flex; justify-content: space-between; align-items: center; }
    h1 { margin: 0; font-size: 1.2rem; text-transform: uppercase; }
    
    nav { background: white; padding: 15px; border-bottom: 1px solid #ddd; text-align: center; }
    select, input { padding: 5px; border: 1px solid #ccc; border-radius: 3px; }
    input[type="submit"] { background: #2c3e50; color: white; border: none; padding: 5px 15px; cursor: pointer; }

    main { max-width: 1000px; margin: 20px auto; padding: 0 10px; }
    
    /* Compact Row Style */
    article { 
      background: white; margin-bottom: 8px; padding: 12px; border-radius: 4px;
      display: grid; 
      grid-template-columns: 1.5fr 1fr 1fr 1fr 2fr; 
      gap: 10px; align-items: center; border-left: 5px solid #3498db;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }

    article h3 { margin: 0; font-size: 1rem; color: #2c3e50; }
    article p { margin: 0; font-size: 0.85rem; color: #666; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    
    /* Highlighting key data */
    .price { font-weight: bold; color: #27ae60; font-size: 1rem !important; }
    .specs { color: #2980b9; font-weight: 600; }
    .desc { font-style: italic; color: #888; grid-column: 1 / -1; border-top: 1px dotted #eee; pt: 5px; }

    footer { text-align: center; font-size: 0.7rem; color: #999; margin: 20px; }
  </style>
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
        <input type="number" name="precio_minimo" value="0">
        <input type="number" name="precio_maximo" value="1000000000" min=0>
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
            SELECT * FROM viviendas 
            WHERE 
            localidad LIKE '%".$_POST['localidad']."%'
            AND precio > ".$_POST['precio_minimo']."
            AND precio < ".$_POST['precio_maximo']."
            ;
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