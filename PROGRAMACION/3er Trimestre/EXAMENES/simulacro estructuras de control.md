# 1. Elegir qué operación debe ejecutar el programa:

El proyecto necesita comportarse de forma distinta según lo que esté procesando: armas, armaduras, usuarios, etc
Condicionales (if, elseif).
Aqui se decide que se muestra a la hora de cargar armas o armaduras.

```
if ($tabla === 'armas') {
} elseif ($tabla === 'armaduras') {
}
```

# 2. Controlar errores:

Detección de fallos y parar el programa con un mensaje en caso de fallo.

```
if (!$resArmas) {
    die("Error al cargar armas: " . $conexion->error);
}
```

# 3. Comprobar si algo existe antes de usarlo:

Por ejemplo, cuando se agrupan armas por tipo me aseguro de que la clave exista en el array.

```
if (!isset($armasPorTipo[$tipo])) {
    $armasPorTipo[$tipo] = [];
}
```

# 4. Recorrer datos de la base de datos (bucles while):

Cargo listas de armas, armaduras, usuarios, etc.

```
while ($fila = $resultado->fetch_assoc()) {
    // Procesar cada arma o armadura
}
```

# 5. Verificación de usuarios + contraseña:

Compruebo que el usuario existe, que se quiere loguear y verifico que su contraseña encaja con el hash almacenado en la base de datos, por último se guardan los datos importantes en la sesión para usar en la web

```
if ($res && mysqli_num_rows($res) == 1) {

    $u = mysqli_fetch_assoc($res);

        if (password_verify($pass, $u['password_hash'])) {

            $_SESSION['id_usuario'] = $u['id'];
            $_SESSION['usuario'] = $u['nickname'];
            $_SESSION['rol'] = $u['role'];
```