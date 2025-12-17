<!doctype html>
<html>
	<head>
  	<link rel="stylesheet" href="css/estilo.css">
  </head>
  <body>
    <?php include "inc/conexion_bd.php"; ?>
    <nav>
    <?php
      // Ahora lo que quiero es un listado de las tablas en la base de datos
        $resultado = $conexion->query("
          SHOW TABLES;
        ");
        while ($fila = $resultado->fetch_assoc()) {
          echo '<a href="?tabla='.$fila['Tables_in_'.$db].'">'.$fila['Tables_in_'.$db].'</a>';
        }
    ?>
    </nav>
    <main>
      <table>
      <?php
      // PRIMERO CREO LAS CABECERAS //////////////////
        $resultado = $conexion->query("
          SELECT * FROM ".$_GET['tabla']." LIMIT 1;
        ");	// SOLO QUIERO UN ELEMENTO !!!!!!!!!!!!!!!!
        while ($fila = $resultado->fetch_assoc()) {
          echo "<tr>";
          foreach($fila as $clave=>$valor){
            echo "<th>".$clave."</th>";		// En lugar de enseñarme el valor, enseñame la clave
          }
          echo "</tr>";
         }
      ?>
      <?php
      // Y LUEGO EL RESTO DE DATOS //////////////
        $resultado = $conexion->query("
          SELECT * FROM ".$_GET['tabla'].";
        ");
        while ($fila = $resultado->fetch_assoc()) {
          echo "<tr>";
          foreach($fila as $clave=>$valor){
            echo "<td>".$valor."</td>";
          }
          echo "</tr>";
         }
      ?>
      </table>
    </main>
  </body>
</html>