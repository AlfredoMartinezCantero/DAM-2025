<?php include "inc/cabecera.php"; ?>

Hola que tal yo soy el carrito<br>
Vamos a ver si atrapamos correctamente el producto<br>
<?php
	echo "El producto es: ".$_POST['id']."<br>";
  echo "Las unidades son: ".$_POST['unidades']."<br>";
?>

<?php include "inc/piedepagina.php"; ?>