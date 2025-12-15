<?php include "inc/cabecera.php"; ?>

Vamos a asegurarnos de que lo hemos traído todo<br>

El nombre del cliente es:<br>
<?= $_POST['nombre_cliente']?><br>
<br>
Los apellidos del cliente son<br>
<?= $_POST['apellidos']?><br>
<br>
El email del cliente es<br>
<?= $_POST['email']?><br>
<br>
La direcion del cliente es:<br>
<?= $_POST['direccion']?><br>
<br>
El teléfono del cliente es:<br>
<?= $_POST['telefono']?><br>
<br>

El producto que ha pedido es:<br>
<?= $_POST['idproducto']?><br>
<br>
La cantidad que ha pedido es:<br>
<?= $_POST['unidades']?><br>
<br>

<?php
// Y ahora es cuando toca guardar cosas en la base de datos
// CUIIDADO CON LAS FK(foreing keys)
// Aquellas tablas que no tengan dependencias, van primero
// Las tablas que tengan dependencias van después

    $host = "localhost";
    $user = "tiendaonlinedamdaw";
    $pass = "Tiendaonlinedamdaw123$";
    $db   = "tiendaonlinedamdaw";

    $conexion = new mysqli($host, $user, $pass, $db);

    $sql = "SELECT * FROM producto;";

    $resultado = $conexion->query($sql);

// Primero guardamos el cliente
    $resultado = $conexion->query("
        INSERT INTO cliente VALUES(
        NULL,
        '".$_POST['nombre_cliente']."',
        '".$_POST['apellidos']."',
        '".$_POST['email']."',
        '".$_POST['direccion']."',
        '".$_POST['telefono']."'
        )
    ");
    $id_cliente_insertado = $conexion->insert_id;

    // Segundo, guardaremos el pedido (necesita un id de cliente)

    // Tercero, guardaremos lineas de pedido (neecesita un id de pedido)

?>

<?php include "inc/piedepagina.php"; ?>











