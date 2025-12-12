<?php include "inc/cabecera.php"; ?>
<section id="heroe">
    <h3>Motivo por el cual debería comprar</h3>
    <p>Frase sugerente al respecto</p>
    <a href="catalogo.php">Vamos a ver esa maravilla de catálogo</a>
</section>
<style>
    #heroe{
    background:darkorchid;
    height:400px;
    display:flex;
    flex-direction:column;
    color:white;
    justify-content:center;
    align-items:center;
    }

  #heroe a{
  	color:darkorchid;
    background:white;
    text-decoration:none;
    padding:10px;
    border-radius:5px;
    }

</style>
<?php include "inc/piedepagina.php"; ?>