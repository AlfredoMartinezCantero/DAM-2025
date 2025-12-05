<?php
	function codificaRomana($cadena){
  	for($i = 0;$i<strlen($cadena);$i++){
    	$cadena[$i] = chr(ord($cadena[$i])+10);
    }
    return $cadena;
  }
  function descodificaRomana($cadena){
  	for($i = 0;$i<strlen($cadena);$i++){
    	$cadena[$i] = chr(ord($cadena[$i])-10);
    }
    return $cadena;
  }
  $original = "Hola";
  echo $original;
  echo "<br>";
  
  $codificado =  codificaRomana("Hola");
  
  echo $codificado;
  echo "<br>";
  
  $descodificado =  descodificaRomana($codificado);
  
  echo $descodificado;
  echo "<br>";
?>
