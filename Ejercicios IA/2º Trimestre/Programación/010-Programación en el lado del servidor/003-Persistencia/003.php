<?php
    $musica = [];
    $musica['nombre'] = "Extremoduro";
    $musica['genero'] = "Rock";
    $musica['artista'] = "Robe";

    $jsonMusica = json_encode($musica);
    echo $jsonMusica;
?>