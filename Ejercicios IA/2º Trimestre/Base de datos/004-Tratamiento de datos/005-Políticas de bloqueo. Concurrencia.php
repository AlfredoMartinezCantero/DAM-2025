<?php
    // Defino una contraseña de prueba
    $contrasena = "BarBara_2025$";

    echo "<h3>1. Codificación Base64 Simple</h3>";
    
    // Codifico la cadena una sola vez
    $codificado = base64_encode($contrasena);
    echo "Original: $contrasena <br>";
    echo "Codificado: $codificado <br>";
    
    // Decodifico para comprobar que es reversible
    $decodificado = base64_decode($codificado);
    echo "Decodificado: $decodificado <br>";

    echo "<hr>";

    echo "<h3>2. Función Personalizada (Bucle 9 veces)</h3>";

    // Función que recibe una cadena y la codifica 9 veces seguidas
    function codifica9veces($cadena){
        for ($i = 0; $i < 9; $i++){
            $cadena = base64_encode($cadena);
        }
        return $cadena;
    }

    // Función que recibe una cadena y la decodifica 9 veces seguidas
    function decodifica9veces($cadena){
        for ($i = 0; $i < 9; $i++){
            $cadena = base64_decode($cadena);
        }
        return $cadena;
    }

    // Pruebo mis funciones
    $superCodificado = codifica9veces($contrasena);
    echo "Contraseña codificada 9 veces: <br>";
    // Uso wordwrap para que no se salga de la pantalla al ser muy larga
    echo wordwrap($superCodificado, 80, "<br>", true) . "<br><br>";

    $superDecodificado = decodifica9veces($superCodificado);
    echo "Contraseña recuperada: $superDecodificado <br>";

    echo "<hr>";

    echo "<h3>3. Manipulación ASCII (ord y chr)</h3>";
    
    // Obtengo el primer carácter de la contraseña
    $primerCaracter = $contrasena[0]; // Es la 'B'
    
    // Convierto el carácter a su valor numérico ASCII
    $valorAscii = ord($primerCaracter);
    echo "El valor ASCII de '$primerCaracter' es: $valorAscii <br>";
    
    // Recupero el carácter desde el número
    $caracterRecuperado = chr($valorAscii);
    echo "Si convierto $valorAscii de nuevo a carácter obtengo: $caracterRecuperado <br>";
?>