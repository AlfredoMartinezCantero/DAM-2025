<?php
// Defino la variable con un número entero
$edad = 24;

function clasificarEdad($edadRecibida){
    // Verifico que el parámetro recibito sea menor que 30
    if ($edadRecibida < 30){
        $resultado = "Eres un jovenzuelo";
    }else{
        $resultado = "Ya no eres tan joven";
    }
    // Devuelvo el resultado
    return $resultado;
}

$mensajeFinal = clasificarEdad($edad);

// Muestro el resultado por pantalla
echo "Tengo $edad años" . $mensajeFinal;
?>