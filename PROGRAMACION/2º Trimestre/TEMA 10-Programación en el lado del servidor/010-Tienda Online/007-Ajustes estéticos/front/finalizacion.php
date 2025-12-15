<?php include "inc/cabecera.php"; ?>

<h1>Pedido finalizado</h1>
<p>Muchas gracias por su compra</p>

<p>Datos del pedido:</p>
<?= $_POST['nombre_cliente']?> <?= $_POST['apellidos']?><br>
<?= $_POST['email']?><br>
<?= $_POST['direccion']?><br>
<?= $_POST['telefono']?><br>
<br>

El producto que ha pedido es:<br>
<?= $_POST['idproducto']?><br>
<br>
La cantidad que ha pedido es:<br>
<?= $_POST['unidades']?><br>
<br>

<?php
	$host = "localhost";
  $user = "tiendaonlinedamdaw";
  $pass = "Tiendaonlinedamdaw123$";
  $db   = "tiendaonlinedamdaw";

  $conexion = new mysqli($host, $user, $pass, $db);

    // Y ahora es cuando toca guardar cosas en la base de datos
    // CUIDADO CON LAS FK
    // Aquellas tablas que no tengan dependencias, van primero
    // Las tablas que tengan dependencias van despues
  
    // Primero guardaremos el cliente
    // Guardo los datos que vienen por post (del formulario anterior)
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
    // Y me quedo en memoria con el id del ultimo cliente insertado
    $id_cliente_insertado = $conexion->insert_id;
  
    // Segundo, guardaremos el pedido (necesita un id de cliente)
    // Ahora creo un pedido con la fecha actual y el id anterior
    $resultado = $conexion->query("
        INSERT INTO pedido VALUES(
            NULL,
        '".date('Y-m-d H:i:s')."',
        ".$id_cliente_insertado."
        )
    ");
    $id_pedido_insertado = $conexion->insert_id; // MAGIA NEGRA !!!!!!!!!!!!!!!!!!
    
    // Tercero, guardaremos lineas de pedido (necesita un id de pedido)
    // Ahora creo una linea  de pedido con el id de pedido insertado y las lineas que venian de la pantalla anterior
    $sql = "
        INSERT INTO lineaspedido VALUES(
            NULL,
        ".$id_pedido_insertado.",
        '".$_POST['unidades']."',
        ".$_POST['idproducto']."
        )
    ";
    echo $sql;
    $resultado = $conexion->query($sql);
    ?>

<?php include "inc/piedepagina.php"; ?>