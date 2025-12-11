<form action="procesaformulario.php" method="POST">

	<label for="titulo">Título de la nueva noticia</label>
	<input type="text" name="titulo" id="titulo">
  
    <label for="contenido">Contenido de la nueva noticia</label>
	<textarea id="contenido" name="contenido"></textarea>
  
    <label for="fecha_publicacion">Fecha de la nueva noticia</label>
	<input type="text" name="fecha_publicacion" id="fecha_publicacion">
  
    <label for="autor_id">Autor de la nueva noticia</label>
	<input type="text" name="autor_id" id="autor_id">
  
    <input type="submit">
    
</form>