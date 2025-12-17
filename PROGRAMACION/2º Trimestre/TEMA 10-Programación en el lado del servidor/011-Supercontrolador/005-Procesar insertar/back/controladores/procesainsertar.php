<!doctype html>
<html>
    <head>
  	<link rel="stylesheet" href="css/estilo.css">
  </head>
  <body>
		<?php include "inc/conexion_bd.php"; ?>
    <nav>
    	<?php include "controladores/poblar_menu.php" ?>
    </nav>
    <main>

<?php
    $sql = "INSERT INTO ".$_GET['tabla']." VALUES ";
    foreach($_POST as $clave=>$valor){
        if($clave == "id"){
            $sql.= "NULL,";
        }else{
            $sql.="'".$valor."',";
        }
  }
  $sql = substr($sql, 0, -1);       // Le quito la última coma al SQL
  echo $sql;
?>