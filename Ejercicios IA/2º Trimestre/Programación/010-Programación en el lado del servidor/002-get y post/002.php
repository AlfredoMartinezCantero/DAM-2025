<!-- EJERCICIO 1 -->
<?php
  echo $_GET['nombre'];
?>

<!-- EJERCICIO 2 -->
<?php
  echo $_POST['nombre'];
?>
 
<form action="006-post.php" method="POST">
  <p>Introduce tu nombre</p>
  <input type="text" name="nombre">
  <input type="submit">
</form>


<!-- EJERCICIO 3 -->
<?php
  echo $_POST['nombre'];
?>
<form action="?" method="POST">
  <p>Introduce tu nombre</p>
  <input type="text" name="nombre">
  <input type="submit">
</form>