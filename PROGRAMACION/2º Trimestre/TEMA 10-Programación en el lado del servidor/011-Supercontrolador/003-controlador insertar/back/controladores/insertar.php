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