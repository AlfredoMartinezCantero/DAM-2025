<form action="" method="POST">
<?php
      // Creamos un formulario dinámico
      
        $resultado = $conexion->query("
          SELECT * FROM ".$_GET['tabla']." LIMIT 1;
        ");	                        // SOLO QUIERO UN ELEMENTO ////
        while ($fila = $resultado->fetch_assoc()) {
          foreach($fila as $clave=>$valor){
            echo "
            	<div class='control_formulario'>
                <label>".$clave."</label>
                <input 
                  type='text' 
                  name='".$clave."'
                  placeholder='".$clave."'>
              </div>
              ";
          }
         }
      ?>
</form>
<style>
    form{
        width:100%;
        display:flex;
        flex-direction:column;
        gap:20px;
    }

    .control_formulario{
        display:flex;
    }

    label{
        flex:1;
    }

    input{
        flex:4;
        padding:10px;
        border:2px solid plum;
    }

</style>