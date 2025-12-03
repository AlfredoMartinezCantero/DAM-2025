<?php
    $cliente = [];
    $cliente['nombre'] = "Alfredo";
    $cliente['apellidos'] = "Martínez Cantero";
    $cliente['email'] = "alfredomartinezcantero@gmail.com";

    $json = json_encode($cliente);
    echo $json;
?>