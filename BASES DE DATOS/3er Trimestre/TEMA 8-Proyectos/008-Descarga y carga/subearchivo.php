<?php
// sudo chmod 777 -R "nombre de la bbdd" (esto en un entorno real nunca habría que hacerlo)
// subearchivo.php (ultra-minimal)

mkdir('uploads');

move_uploaded_file(
  $_FILES['archivo']['tmp_name'],
  'uploads/' . $_FILES['archivo']['name']
);

echo 'OK';
?>

