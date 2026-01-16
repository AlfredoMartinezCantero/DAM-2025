**PROGRAMACIÓN (/back)**

`Archivo: back/inc/conexion_bd.php`

# Introducción:
Todo el proyecto depende de un único punto de entrada a la base de datos, en lugar de repetir las credenciales en cada archivo, las hemos centralizado en `conexion_bd.php`, utilizando la librería `PHP Data Objects` porquue nos permite trabajar con una capa de abstracción segura y orientada a objetos, facilitando el manejo de excepciones mediante `try-catch`.

Aquí definimos las variables de entorno `($host, $db, $user, $pass)` para conectar con el usuario que creamos en la BBDD, configuramos `PDO::ERRMODE_EXCEPTION` para que cualquier fallo de SQL lance un error fatal visible en desarrollo, y `FETCH_ASSOC` para que los resultados vengan siempre como arrays asociativos, lo cual facilita su lectura en el código posterior.

---
```
<?php
$host = 'localhost';
$db   = 'Bar_Bara';
$user = 'admin_bara';
$pass = 'BarBara_2025$';
$charset = 'utf8mb4';

try {
     $pdo = new PDO("mysql:host=$host;dbname=$db;charset=$charset", $user, $pass, [
         PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
         PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
     ]);
} catch (PDOException $e) {
     die("Error de conexión: " . $e->getMessage());
}
?>
```
# Conclusión:
Aquí aprendimos que centralizar la conexión es vital para el mantenimiento, si cambiamos la contraseña de la base de datos, solo tenemos que editar este archivo y el cambio se propaga a todo el proyecto.

---
**CONTROLADORES (LÓGICA DE NEGOCIO /controladores)**

`Archivos: PedidoControlador.php, ProductoControlador.php, UsuarioControlador.php`

# Introducción: PedidoControlador.php
En esta parte del código implementamos la lógica para gestionar transacciones complejas, el desafío principal era que un pedido no es un dato único, sino que consta de dos partes: la cabecera (mesa, fecha, usuario) y las líneas de detalle (los productos específicos).

Para resolver esto, en el método `crearNuevoPedido` realiza una inserción secuencial, primero crea el registro en la tabla pedido estableciendo el estado inicial `pedir_cuenta = 'NO'`, inmediatamente después utilizamos una función clave llamada `lastInsertId()`, esta función es vital porque recupera el ID autogenerado del pedido que se acaba de crear, sin ese ID no se podrían vincular los productos, y una vez tengo ese identificador, utilizamos un bucle `foreach` para recorrer la lista de productos e insertarlos uno a uno en la tabla `contenido_pedido`, vinculándolos mediante la clave foránea `pedido_id`.

---
```
<?php
// controladores/PedidoControlador.php

class PedidoControlador {
    private $db;

    public function __construct($conexion) {
        $this->db = $conexion;
    }

    public function crearNuevoPedido($datos) {
        // El pedido nace con pedir_cuenta = 'NO' (Pendiente de servir)
        $sqlPedido = "INSERT INTO pedido (usuario_id, numero_mesa, fecha, hora, total, pedir_cuenta) 
                      VALUES (?, ?, CURDATE(), CURTIME(), ?, 'NO')";
        $stmt = $this->db->prepare($sqlPedido);
        $stmt->execute([
            $datos['usuario_id'], 
            $datos['numero_mesa'], 
            $datos['total']
        ]);
        $idPedido = $this->db->lastInsertId();

        foreach ($datos['productos'] as $item) {
            $sqlContenido = "INSERT INTO contenido_pedido (pedido_id, producto_id, cantidad, subtotal) 
                             VALUES (?, ?, ?, ?)";
            $stmtDetalle = $this->db->prepare($sqlContenido);
            $stmtDetalle->execute([
                $idPedido, 
                $item['producto_id'], 
                $item['cantidad'], 
                $item['subtotal']
            ]);
        }
        return $idPedido;
    }

    public function marcarComoEntregado($idPedido) {
        // Cambiamos el estado a ENTREGADO para que desaparezca de la lista de cocina
        $sql = "UPDATE pedido 
            SET pedir_cuenta = CASE 
                WHEN pedir_cuenta = 'SI' THEN 'SI_ENTREGADO' 
                ELSE 'ENTREGADO' 
            END 
            WHERE id = ?";
    return $this->db->prepare($sql)->execute([$idPedido]);
    }

    public function solicitarCuenta($idPedido) {
        $sql = "UPDATE pedido SET pedir_cuenta = 'SI' WHERE id = ?";
        return $this->db->prepare($sql)->execute([$idPedido]);
    }

    // NUEVA FUNCIÓN: Marca como PAGADO para limpiar el historial del cliente
    public function marcarComoPagado($idPedido) {
        $sql = "UPDATE pedido SET pedir_cuenta = 'PAGADO' WHERE id = ?";
        return $this->db->prepare($sql)->execute([$idPedido]);
    }
}
```
---

# Introducción: ProductoControlador.php
En esta parte implementamos la lógicaa de lectura del catálogo, el objetivo principal de esta clase es servir de puente entre la tabla producto de la base de datos y las vistas donde el cliente elige qué comer, decidimos definir dos métodos diferenciados según la necesidad, el primero es `listarTodo()`, este método se utiliza para llenar el `Grid` del catálogo principal, como la consulta `SELECT * FROM` producto no requiere parámetros externos, utilizamos el método directo `$this->db->query($sql)` y al esperar múltiples filas, utilizamos `fetchAll()`, que me devuelve un array de arrays conteniendo todo el inventario de golpe.

Y luego usamos `obtenerPorId($id)`, sste método es muy importando para cuando necesitamos detalles de un solo producto específico, por ejemplo, al añadirlo al carrito para verificar su precio real, aquí dado que el `$id` viene de fuera es obligatorio usar Sentencias Preparadas para evitar inyecciones SQL.

---
```
<?php
// controladores/ProductoControlador.php

class ProductoControlador {
    private $db;

    public function __construct($conexion) {
        $this->db = $conexion;
    }

    public function listarTodo() {
        // Obtenemos todos los campos: nombre, precio, descripción, categoria e imagen
        $sql = "SELECT * FROM producto";
        $stmt = $this->db->query($sql);
        return $stmt->fetchAll();
    }

    public function obtenerPorId($id) {
        $sql = "SELECT * FROM producto WHERE id = ?";
        $stmt = $this->db->prepare($sql);
        $stmt->execute([$id]);
        return $stmt->fetch();
    }
}
```
---

# Introducción: UsuarioControlador.php
En este bloque del código, mi compañera y yo implementamos la clase `UsuarioControlador` para centralizar la lógica de seguridad y acceso a datos de los usuarios, definimos un constructor `__construct` que recibe la conexión a la base de datos, lo que permite reutilizar la misma conexión en todos los métodos de la clase.

Para el método registrar priorizamos la seguridad utilizando la función nativa `password_hash` con el algoritmo `PASSWORD_BCRYPT`. Esto convierte la contraseña introducida por el usuario en una cadena alfanumérica ilegible antes de enviarla a la base de datos, además en lugar de concatenar variables directamente en la consulta SQL utilizamos Sentencias Preparadas `(mediante prepare y execute con signos de interrogación ?)`, esto indica al motor de la base de datos que trate los datos como parámetros y no como código ejecutable, eliminando el riesgo de Inyección SQL.

Para el método login, implementamos la verificación inversa, es decir, se recupera el usuario buscando por su correo y utilizo `password_verify`, que compara la contraseña introducida en el formulario con el hash almacenado en la base de datos, devolviendo true solo si coinciden matemáticamente.

---
```
<?php
// controladores/UsuarioControlador.php

class UsuarioControlador {
    private $db;

    public function __construct($conexion) {
        $this->db = $conexion;
    }

    public function registrar($datos) {
        // Encriptamos la contraseña para seguridad
        $passwordSegura = password_hash($datos['contrasea'], PASSWORD_BCRYPT);
        
        $sql = "INSERT INTO usuario (nombre_usuario, apellidos, correo, contrasea) VALUES (?, ?, ?, ?)";
        $stmt = $this->db->prepare($sql);
        return $stmt->execute([
            $datos['nombre_usuario'], 
            $datos['apellidos'], 
            $datos['correo'], 
            $passwordSegura
        ]);
    }

    public function login($correo, $password) {
        $sql = "SELECT * FROM usuario WHERE correo = ?";
        $stmt = $this->db->prepare($sql);
        $stmt->execute([$correo]);
        $usuario = $stmt->fetch();

        if ($usuario && password_verify($password, $usuario['contrasea'])) {
            return $usuario; // Login exitoso
        }
        return false;
    }
}
```
---
# Conclusión:
En el desarrollo de estos tres controladores mi compañera y yo aprendimos la arquitectura base de la aplicación, entendiendo que el Backend no es un único bloque, sino un sistema de piezas especializadas que colaboran entre sí.

- En el apartado de seguridad y acceso (UsuarioControlador), aprendimos que la seguridad es la primera capa, no basta con guardar datos, hay que protegerlos. 
La implementación de `password_hash` y la verificación de credenciales actúan como el "portero" de la aplicación, asegurando que solo usuarios legítimos puedan interactuar con el sistema.

- Gestión de Inventario (ProductoControlador), aqui comprendimos la importancia de separar la lectura de datos de la lógica de negocio, este controlador actúa como un proveedor eficiente de información, permitiendo que la vista del catálogo se alimente dinámicamente de la base de datos sin necesidad de incrustar consultas SQL en el HTML.

- PedidoControlador, esto el corazón del sistema, aquí he gestionamos la Integridad Referencial desde el código, coordinando la cabecera de un pedido con sus múltiples líneas de productos. 
Hemos podido ver cómo el código PHP debe replicar y respetar las relaciones que definimos previamente en el diagrama entidad-relación de la base de datos (1 a N).

---
**BACKEND Y API**

`Archivos: index.php, listar_productos.php, peticion_login.php, peticion_pedido.php`

# Introducción: index.php
`index.php`, es decir, el panel de administración en el back es la única vista visual del back, esta muestra las comandas pendientes y alertas de cobro y utiliza lógica de refresco automático y formularios `POST` para cambiar estados.

---
```
<?php
// index.php en la raíz del back
require_once 'inc/conexion_bd.php';
require_once 'controladores/PedidoControlador.php';
require_once 'controladores/ProductoControlador.php';

$pedidoCtrl = new PedidoControlador($pdo);
$productoCtrl = new ProductoControlador($pdo);

// --- LÓGICA DE ACCIONES ---

// 1. Marcar como entregado (Cocina)
if (isset($_POST['entregar_id'])) {
    $pedidoCtrl->marcarComoEntregado($_POST['entregar_id']);
}

// 2. Marcar como pagado (Barra) y limpiar historial del cliente
if (isset($_POST['cobrar_id'])) {
    $idPedido = $_POST['cobrar_id'];
    // Ejecutamos el cambio a 'PAGADO' directamente o mediante el controlador
    $sql = "UPDATE pedido SET pedir_cuenta = 'PAGADO' WHERE id = ?";
    $stmt = $pdo->prepare($sql);
    $stmt->execute([$idPedido]);
}

try {
    $totalProductos = count($productoCtrl->listarTodo());
    
    // COMANDAS POR SERVIR: Solo las que están en estado 'NO'
    $pendientes = $pdo->query("SELECT * FROM pedido WHERE pedir_cuenta IN ('NO', 'SI') ORDER BY hora ASC")->fetchAll();    
    // ALERTAS DE COBRO: Solo las que están en estado 'SI'
    $alertas = $pdo->query("SELECT * FROM pedido WHERE pedir_cuenta IN ('SI', 'SI_ENTREGADO') ORDER BY hora ASC")->fetchAll();
    
    $conteoAlertas = count($alertas);
} catch (Exception $e) {
    die("Error en la base de datos: " . $e->getMessage());
}
?>
```
---

# Introducción: listar_productos.php
En esta parte del back implementamos un endpoint de API en PHP para servir la lista de productos, en lugar de mezclar HTML y PHP en el mismo archivo.

Utilizamos `require_once` para importar la conexión a la base de datos y la clase del controlador, asegurándonos de que el script se detenga inmediatamente si no encuentra estos archivos críticos, evitando errores en cascada, un paso fundamental ha sido configurar la cabecera HTTP mediante `header("Content-Type: application/json");` esto instruye al navegador o cliente que recibe la respuesta para que interprete los datos como un objeto JSON y no como texto plano o HTML.

Por último aplicamos la inyección de dependencias al instanciar `new ProductoControlador($pdo)`, pasando la conexión activa al controlador para que este pueda operar y para rematar, usamos la función `json_encode` para serializar el array de productos que me devuelve el controlador, convirtiéndolo en una cadena de texto estándar que cualquier cliente JavaScript puede leer.

---
```
<?php
require_once 'inc/conexion_bd.php';
require_once 'controladores/ProductoControlador.php';
header("Content-Type: application/json");
$controlador = new ProductoControlador($pdo);
echo json_encode($controlador->listarTodo());
```
---

# Introducción: peticion_login.php
En el login desarrollamos el script encargado de validar las credenciales del usuario mediante una petición asíncrona, aquí los datos viajan como una cadena JSON cruda.

Para capturar esta información, tuvimos que utilizar la instrucción `file_get_contents("php://input")`, ya que el array superglobal `$_POST` no es capaz de leer cuerpos de mensaje en formato JSON, una vez capturada la cadena de texto, utilizamos `json_decode(..., true)` para transformarla en un array asociativo de PHP que pueda manipular fácilmente.

Por último instanciamos el `UsuarioControlador`, inyectándole la conexión PDO y llamamos al método login, finalmente utilizamos un operador para construir una respuesta JSON inmediata, y si el login es correcto, devuelvo exito `=> true` junto con el ID del usuario.

---
```
<?php
require_once 'inc/conexion_bd.php';
require_once 'controladores/UsuarioControlador.php';
header("Content-Type: application/json");
$datos = json_decode(file_get_contents("php://input"), true);
$controlador = new UsuarioControlador($pdo);
$usuario = $controlador->login($datos['correo'], $datos['pass']);
echo json_encode($usuario ? ["exito" => true, "id" => $usuario['id']] : ["exito" => false]);
```
---

# Introduicción: peticion_pedido.php
En esta última parte del back optimizamos la estructura de la API agrupando múltiples operaciones en un único punto endpoint, utilizando la `superglobal $_GET['accion']`, si la acción es crear, el script toma el JSON completo recibido por `php://input` y se lo pasa al controlador para que genere un nuevo registro en la base de datos (tablas pedido y contenido_pedido ). Si la acción es cuenta, extraigo únicamente el `pedido_id` del JSON para actualizar el estado de esa mesa específica, de esta forma conseguimos gestionar diferentes intenciones dentro de un mismo archivo, manteniendo el código ordenado y reduciendo el número de archivos en el servidor.

---
```
<?php
require_once 'inc/conexion_bd.php';
require_once 'controladores/PedidoControlador.php';
header("Content-Type: application/json");
$datos = json_decode(file_get_contents("php://input"), true);
$controlador = new PedidoControlador($pdo);
$accion = $_GET['accion'] ?? '';

if ($accion === 'crear') {
    $id = $controlador->crearNuevoPedido($datos);
    echo json_encode(["status" => "creado", "pedido_id" => $id]);
} elseif ($accion === 'cuenta') {
    $controlador->solicitarCuenta($datos['pedido_id']);
    echo json_encode(["status" => "cuenta_solicitada"]);
}
```
---
# Conclusión:
- El backend presenta una arquitectura híbrida dividida en dos funciones claras, gestión visual con `index.php`, un panel de administración tradicional `HTML/PHP` para que el personal de cocina y barra controle el flujo de pedidos y cobros en tiempo real.

- `API REST`, esto es un conjunto de endpoints que sirven datos crudos en formato JSON a la aplicación cliente, manejando autenticación (login), lectura (listar) y escritura (pedidos).

El uso de `php://input` para recibir JSON en lugar de formularios tradicionales en la API, también la implementación de patrón MVC mediante Controladores, separando la lógica de negocio de las vistas y endpoints, y por último el enrutamiento, sencillo en `peticion_pedido.php` para manejar varias acciones en un solo archivo.

---

**FRONTEND**

# Introducción: cabecera.php
En esta parte del front mi compañera y yo implementamos la gestión de la sesión del usuario para mantener la persistencia de los datos mientras navega por la tienda, comenzamos utilizando la función `session_status()` para verificar si la sesión ya está activa, esto es fundamental para evitar errores si incluyo este archivo varias veces en una misma ejecución (por ejemplo, en un include de cabecera ), luego, para calcular el número de artículos que el usuario lleva comprados, verificamos primero si existe la variable superglobal `$_SESSION['carrito']` utilizando `isset()`, si existe, recorro el array mediante un bucle `foreach`, sumando la propiedad `['cantidad']` de cada producto a mi variable acumuladora `$cantidad_total` y por último, utilizamos una estructura condicional simplificada para definir el nombre que se mostrará en la interfaz, si la clave nombre está definida en la sesión, se utiliza, de lo contrario, se asigna el valor genérico `'Cliente'`.

---
```
<?php
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

$cantidad_total = 0;
if (isset($_SESSION['carrito'])) {
    foreach ($_SESSION['carrito'] as $producto) {
        $cantidad_total = $cantidad_total + $producto['cantidad'];
    }
}

$usuario_conectado = isset($_SESSION['user_id']);
$nombre_usuario = isset($_SESSION['nombre']) ? $_SESSION['nombre'] : 'Cliente';
?>
```
---

# Introducción: piedepagina.php
En esta parte desarrollamos el módulo del `footer`, que actúa como el cierre estándar para todas las vistas de la aplicación web, empezamos cerrando el contenedor principal con la etiqueta `</div>`, asegurando que el flujo del documento HTML quede correctamente estructurado antes de renderizar el pie de página, para el diseño del pie, utilizamos la etiqueta semántica `<footer>`, aunque en el resto del proyecto utilizamos hojas de estilo externas, en este caso aplicamos estilos en línea `(style="")` para forzar propiedades críticas como `margin-top: auto`, esta propiedad es fundamental en el diseño de Flexbox, ya que "empuja" el pie de página hacia el fondo de la ventana visualmente, evitando que se quede flotando a mitad de pantalla si el contenido de la página es escaso.

---
```
</div> 

<footer style="background: #2c3e50; color: white; text-align: center; padding: 20px; margin-top: auto; width: 100%;">
    
    <p>&copy; 2026 Bar Bara - Todos los derechos reservados.</p>
    
    <p style="font-size: 0.8em; color: #bdc3c7; margin-top: 10px;">
        Calle Pedro Antonio de Alarcón, 17 - Granada, 18001
    </p>

</footer>

</body>
</html>
```
---
# Conclusión:
Con la implementación de estos dos archivos conseguimos entender la arquitectura base del proyecto, también aprendimos que una aplicación web profesional no se construye copiando y pegando el mismo código en cada página, sino mediante la modularización, por un lado, el archivo de Lógica de Sesión actúa como el "cerebro" invisible de la web, es decir, se encarga de mantener la continuidad del usuario a través de la superglobal `$_SESSION` y, por otro lado, el `Footer` actúa como el "marco" visual, garantizando que la identidad corporativa y la información legal estén siempre presentes y estandarizadas gracias a la maquetación con estilos en línea y Flexbox.

---

# Introducción: carrito.php
En la parte del `carrito.php`, mi compañera y yo desarrollamos el controlador del carrito de compras, encargado de gestionar la persistencia de los productos seleccionados por el usuario mientras navega por la web.

Una cosa muy importante que tuvimos que implementar fue el lograr que el navegador recordara la selección de productos del usuario, asi que utilizamos la función `session_start()` al inicio del archivo, lo que permite acceder al array `$_SESSION`.

Para añadir los productos capturamos el ID y hacemos una consulta a la base de datos para obtener el precio del producto y el nombre, para posteriormente, recorrer el array `$_SESSION['carrito']` usando el bucle `foreach`.

Para eliminar productos tuvimos que localizar su índice y utilizar un `unset()`, pero eso puede cargarse los bucles, asi que tuvimos que aplicar la función `array_values()` para reorganizar los índices y que el array volviera a estar limpio.

Por último tuvimos que hacer un calculo del coste total sobre los artículos que se vayan introduciendo al carrito, multiplicando `precio * cantidad` en cada vuelta, dejando la variable `$total` lista para ser mostrada en la vista.

---
```
<?php
session_start();

include '../back/inc/conexion_bd.php';

// 1. LÓGICA: AÑADIR PRODUCTO (Viene del Catálogo)
if (isset($_POST['add'])) {
    $id_producto = $_POST['id'];
    $cantidad = isset($_POST['cantidad']) ? (int)$_POST['cantidad'] : 1; // Leemos la cantidad del formulario 

    $stmt = $pdo->prepare("SELECT * FROM producto WHERE id = :id");
    $stmt->execute([':id' => $id_producto]);
    $producto_bd = $stmt->fetch(PDO::FETCH_ASSOC);

    if ($producto_bd) {
        if (!isset($_SESSION['carrito'])) {
            $_SESSION['carrito'] = [];
        }

        $ya_existe = false;
        foreach ($_SESSION['carrito'] as $indice => $item) {
            if ($item['id'] == $id_producto) {
                $_SESSION['carrito'][$indice]['cantidad'] += $cantidad; // Sumamos la cantidad elegida [cite: 108, 331]
                $ya_existe = true;
                break;
            }
        }

        if (!$ya_existe) {
            $_SESSION['carrito'][] = [
                'id' => $producto_bd['id'],
                'nombre' => $producto_bd['nombre_producto'],
                'precio' => $producto_bd['precio'],
                'cantidad' => $cantidad // Guardamos la cantidad seleccionada
            ];
        }
    }
    header("Location: catalogo.php");
    exit;
}

// 2. LÓGICA: ELIMINAR PRODUCTO
if (isset($_POST['btn_eliminar'])) {
    $id_a_borrar = $_POST['id_eliminar'];

    // Recorremos el carrito para encontrar el ID y borrarlo
    foreach ($_SESSION['carrito'] as $indice => $producto) {
        if ($producto['id'] == $id_a_borrar) {
            unset($_SESSION['carrito'][$indice]); // Lo borramos
            // Re-organizamos los índices del array para que no queden huecos
            $_SESSION['carrito'] = array_values($_SESSION['carrito']); 
            break; 
        }
    }
    // Recargamos para ver el cambio
    header("Location: carrito.php");
    exit;
}

// 3. CALCULAR TOTAL
$total = 0;
if (isset($_SESSION['carrito'])) {
    foreach ($_SESSION['carrito'] as $item) {
        $total += $item['precio'] * $item['cantidad'];
    }
}


include 'inc/cabecera.php'; 
?>
```
---

# Conclusión:
Con esto conseguimos gestionar los estados de la web manteniendo la continuidad de los artículos que los clientess seleccionen.

Un error común que puede ocurrir es olvidar es poner un `echo` antes de llamar a `session_start()`, si pasase esto el script fallaría y el carrito aparecería siempre vacío al recargar la página por que el servidor no puede recordar al usuario.

---

# Introducción: catalogo.php
En esta parte preparamos los datos antes, realizando dos consultas principales, la primera usando `DISTINCT` para obtener un array de categorías y la segunda consulta completa para traer todos los productos, utilzando el metodo `fetchAll(PDO::FETCH_COLUMN)` para las categorías, lo que devuelve directamente el carray simple indexado.

---
```
<?php 
session_start();
require_once '../back/inc/conexion_bd.php'; 
include 'inc/cabecera.php'; 

// Preparamos los datos antes de mostrar el HTML
$res_cat = $pdo->query("SELECT DISTINCT categoria FROM producto ORDER BY categoria");
$categorias = $res_cat->fetchAll(PDO::FETCH_COLUMN);

$stmt = $pdo->query("SELECT * FROM producto ORDER BY categoria, nombre_producto");
?>
```
---
# Conclusión: 
Con esto pudimos reenderizar dinámicamente el catalogo completo, gracias al uso de `PDO::FETCH_ASSOC` dentro de un bucle `while`.

Un error sería olvidarse del atributo `name` en el array `$_POST`, puesto que sin ese atributo el valor sería invisible para el back.

---

# Introducción: contacto.php
En el apartado de contacto tuvimos que implementar una estructura de control `if ($_SERVER["REQUEST_METHOD"] == "POST")`, la cual es necesaria para asegurar que el código de procesamiento solo se ejecuta cuando el usuario ha pulsado el botón de enviar y no cuando se cargue la página.

Una vez verificado el envío, recogemos los datos del array en `$_POST`.

---
```
<?php 
include 'inc/cabecera.php'; 

// --- Lógica de procesamiento del formulario ---
$mensaje_estado = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Recogemos los datos y los limpiamos para evitar inyecciones de código
    $nombre  = htmlspecialchars($_POST['nombre']);
    $email   = htmlspecialchars($_POST['email']);
    $asunto  = htmlspecialchars($_POST['asunto']);
    $mensaje = htmlspecialchars($_POST['mensaje']);

    if (!empty($nombre) && !empty($email) && !empty($mensaje)) {
        $mensaje_estado = "<div style='background: #d4edda; color: #155724; padding: 15px; border-radius: 5px; margin-bottom: 20px; border: 1px solid #c3e6cb;'>
            ¡Gracias, <strong>$nombre</strong>! Hemos recibido tu mensaje sobre '$asunto'. Te responderemos pronto a <em>$email</em>.
        </div>";
    } else {
        $mensaje_estado = "<div style='background: #f8d7da; color: #721c24; padding: 15px; border-radius: 5px; margin-bottom: 20px; border: 1px solid #f5c6cb;'>
            Por favor, rellena todos los campos obligatorios.
        </div>";
    }
}
?>
```
---
# Conclusión:
Aquí vimos la interacción entre cliente y servidor, separando la recepción de datos de la presentación de los mismos, además de la importancia de limpiar la información.

---

# Introducción: historial.php
En esta parte del códgio implementamos el historial de la compra del cliente, es decir, todo lo que ha pedido, el subtotal de la cuenta por el momento y la solicitud de cuenta al camarero.

Primero gestionamos la sesión iniciandola con `session_start()` para recuperar al usuario con un `user_id`, después procesamos la cueta para detectar si el usuario ha pulsado el botón de "Pedir Cuenta", si lo ha hecho, ejecutamos un `UPDATE` en la base de datos para cambiar la columna de `pedir_cuenta`, por último recuperamos el detalle del pedido, esto se consigue haciendo un `JOIN` de las tablas `pedido`, `contenido_pedido` y `producto`, filtrado los pedidos que no estén ya en estado de `PAGADO`, y finalmente usamos `fetchall()` para obtener un array que filtre los productos y calcule el total.

---
```
<?php 
session_start();
require_once '../back/inc/conexion_bd.php';
include 'inc/cabecera.php';

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit;
}

$user_id = $_SESSION['user_id'];
$mensaje = "";

// Lógica para pedir la cuenta desde aquí
if (isset($_POST['pedir_cuenta_total'])) {
    $stmt = $pdo->prepare("UPDATE pedido SET pedir_cuenta = 'SI' WHERE usuario_id = ? AND pedir_cuenta != 'PAGADO'");
    $stmt->execute([$user_id]);
    $mensaje = "🔔 ¡Aviso enviado! El camarero traerá la cuenta en breve.";
}

// Consultamos todos los productos pedidos por el usuario en esta sesión
$query = "SELECT p.id as pedido_id, pr.nombre_producto, cp.cantidad, cp.subtotal, p.pedir_cuenta
          FROM pedido p
          JOIN contenido_pedido cp ON p.id = cp.pedido_id
          JOIN producto pr ON cp.producto_id = pr.id
          WHERE p.usuario_id = ? AND p.pedir_cuenta != 'PAGADO'
          ORDER BY p.id DESC";

$stmt = $pdo->prepare($query);
$stmt->execute([$user_id]);
$items = $stmt->fetchAll();

$total_mesa = 0;
?>
```
---
# Conclusión:
Gracias a este código separamos el pedir la cuennta y la lógica detrás de listar los productos, gracias al uso de `PDO` aseguramos que ninguna manipulación del formulario pueda alterar pedidos de otros usaros, además con el `$total_mesa` acumulamos los subtotales obtenidos de la consuta, garantizando que el precio mostrado al cliente coincida con el registro de la BBDD.

Un error común, por ejemplo, puede ser a la hora de hacer redirrecciones con `header("Location: ")` es olvidar poner `exit;` justo después, puesto que si no detenemos el script el servidor seguirá envíando información aunque el usuario ya no esté en esa página.

---

# Introducción: login.php
En esta parte del código implementamos un login de usuarios, validando las credenciales de un usuario y asegurándonos de proteeger la aplicación.

Para ello iniciamos el script con `session_start()`, como ya hemos visto en los diferentes apartados esto es fundamental para que el servidor recuerde al usuario una vez se loguee correctamente, a continuación implementamos `require_once` para aseguar que si falla la conexión el script se detenga inmediatamente por seguridad.

Para verificar si el servidor ha recibido una petición usamos el `POST` para capturar el correo y la contraseña introducidos, finalmente recuperamos el usuario con `$stmt->fetch()` y utilizamos la función nativa `password_verify()` para que se copare la contraseña escrita con el hash encriptado y almacenado en la BBDD, si estos dos coinciden, se guarda el `id` y el `nombre` en la variable `$_SESSIOn` y llevamos al usuario al panel principal con la función `header()`.

---
```
<?php 
session_start();

// 1. Conexión
require_once '../back/inc/conexion_bd.php'; 

$error = "";

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $correo = $_POST['correo'];
    $pass = $_POST['pass'];

    // Buscamos el usuario
    $stmt = $pdo->prepare("SELECT * FROM usuario WHERE correo = ?");
    $stmt->execute([$correo]);
    $user = $stmt->fetch();

    // Verificamos contraseña
    if ($user && password_verify($pass, $user['contrasena'])) {
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['nombre']  = $user['nombre_usuario']; 
        header("Location: index.php");
        exit;
    } else {
        $error = "Correo o contraseña incorrectos.";
    }
}
?>
```
---
# Conclusión:
Con esto conseguimos gestionar la autenticación usando `PDO::prepare` para evitar inyecciones SQL, además verificando que la contraseñas deben estar siempre con un hash fuerte como `password_verify` y asi evitando comparaciones directas de texto.

---

# Introducción: logout.php
Aquí implementamos la funcion de poder salir de tu cuenta, para empezar siempre tenemos que poner el `session_start()` ya que el servidor necesita saber que sesión va a eliminar de la memoria y una vez recuperada usamos la función `session_destroy()`, la cual se encarga de borrar toda la informacón del usuario del sservidor.

Un detalle importante que implementamos fue hacer uso de la función `header("Location: ")`, que sirve para redireccionar al usuario a la página de inicio una vez el usuario haga el logout.

---
```
<?php
// front/logout.php
session_start();

// Destruimos todas las variables de sesión (nombre, id, carrito...)
session_destroy();

// Redirigimos al usuario a la portada
header("Location: index.php");
exit;
?>
```
---
# Conclusión:
Con este script acabamos con la autenticación que empezó con el login.
Un error común al usar las reedirecciones es escribir contenido HTML o espacios antes de la etiqueta `<?php` o antes de llamar al `header()`, si cometieramos estos errores PHP mostraría un error impidiento que la redirección funcione correctamente.

---

# Introducción: procesar_pedido.php
Aquí desarrollamos un script encargado de procesar la confirmación de compra, actuando como un "puente" entre la información de la sesión del usuario y la base de datos.

Utilizamos `require_once` para cargar las dependencias necesarias, incluyendo un archivo para la conexión a la BBDD y la clase `PedidoControlador` para que se verifique que el usuario esta logeado mediante la función `isset($_SESSION['user_id']);` y, en el caso de que no lo estuviera usamos `header()` para redirigirlo al registro.

Una vez validada la sesión instanciamos el objeto `$pedidoCtrl` pasando a conexión a `$pdo`, asi estructurando los datos en un array que incluye datos del pedido con los productos del carrito, lo que nos permite enviar la información al método `crearNuevoPedido`, por último, mediante un bloque `try-cathc` capturamos cualquier excepción que pueda surgir en la BBDD y si algo fallase, el programa se detenga con `die()`.

---
```
<?php
session_start();
require_once '../back/inc/conexion_bd.php';
require_once '../back/controladores/PedidoControlador.php';

// Si no hay sesión, mandamos al usuario a registrarse/loguearse
if (!isset($_SESSION['user_id'])) {
    header("Location: registro.php");
    exit;
}

if (isset($_POST['confirmar_pedido']) && !empty($_SESSION['carrito'])) {
    $pedidoCtrl = new PedidoControlador($pdo);

    $datosPedido = [
        'usuario_id'  => $_SESSION['user_id'],
        'numero_mesa' => $_POST['numero_mesa'],
        'total'       => $_POST['total_pagar'],
        'productos'   => []
    ];

    foreach ($_SESSION['carrito'] as $item) {
        $datosPedido['productos'][] = [
            'producto_id' => $item['id'],
            'cantidad'    => $item['cantidad'],
            'subtotal'    => $item['precio'] * $item['cantidad']
        ];
    }

    try {
        $idPedido = $pedidoCtrl->crearNuevoPedido($datosPedido);
        unset($_SESSION['carrito']); // Vaciamos carrito tras éxito
        header("Location: finalizacion.php?finalizado=" . $idPedido);
        exit;
    } catch (Exception $e) {
        die("Error al guardar el pedido: " . $e->getMessage());
    }
} else {
    header("Location: catalogo.php");
    exit;
}
```
---
# Conclusión:
Lo que hace este archivo básicamente es ordenar los controladores y manejar las sesiónes y redirecciones, a la par que guarda en la base de datos la información requerida para los pedidos, esto hace que sea más fácil de mantener encargándose solo de recibir datos para prepararlos y responder al usuario.

---

# Introducción: producto.php
Aqui empezamos recibiendo un parámetro a traves de la url utilizando la función `isset($_GET['id'])`, a continuación seleccionamos desde la base de datos con `$stmt = $pdo->prepare("SELECT * FROM producto WHERE id = ?");` los productos que se encuentren en la misma mediante el uso del `id` y finalmente recuperamos el registro con `$stmt->fetch()`, también hemos añadido una estructura de control `if` para gestionar un supuesto en el que un producto no existiera, asi deteniendo la ejecución con un `exit`.

---
```
<?php 
// 1. Incluimos la conexión desde la carpeta back
include '../back/inc/conexion_bd.php'; 

// 2. Incluimos la cabecera (diseño superior)
include 'inc/cabecera.php'; 

// 3. Capturamos el ID y verificamos que el producto existe
$id = isset($_GET['id']) ? $_GET['id'] : 0;
$stmt = $pdo->prepare("SELECT * FROM producto WHERE id = ?");
$stmt->execute([$id]);
$p = $stmt->fetch();

// Si el producto no existe (ej. alguien cambia el ID en la URL a mano)
if (!$p) {
    echo "<div style='text-align:center; padding:100px;'><h2>El producto no existe.</h2><a href='catalogo.php'>Volver a la carta</a></div>";
    include 'inc/piedepagina.php';
    exit;
}
?>
```
---
# Conclusión:
Con este código controlamos el flujo de datos entre páginas utilizando parámetros `GET` y aseguramos las consultas con la base de datos a la par que validamos la exitencia de los datos con el `if` antes de intentar mostrarlos, asi evitamos que la pagina se rompa o muestre errores al usuario.

---

# Introducción: registro.php
Como siempre, emppezamos con un `session_start()`.

Para la conexión a la BBDD utilizamos `require_once` para importar el archivo, asegurándo que no se repitan credenciales en cada archivo.

El núcleo del script comprueba básicamente si la petición llega por un método `POST`, si es así, guardamos los datos del formulario, para la seguridad no se guarda nada en texto plano, utilizamos la función `password_hash()` junto con `PASSWORD_BCRYPT` para que se genere un hash seguro.

Finalmente tras insertar el usuario, obtenemos su ID generado mediante `$pdo->lastInsertId()` y lo guardamos en la sesión, para que luego el sistema lea si el usuario tenía cosas en el carrito con `$_SESSION['carrito']`, y, si es así, lo envíe directamente a dónde se encontraba en ese momento con `header("Location: carrito.php");`

---
```
<?php 
session_start();
// Usamos la conexión centralizada
require_once '../back/inc/conexion_bd.php'; 

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $nombre = $_POST['nombre'];
    $apellidos = $_POST['apellidos'];
    $correo = $_POST['correo'];
    $password = $_POST['pass'];

    // CORRECCIÓN AQUÍ: Cambiamos 'contrasea' por 'contrasena'
    $sql = "INSERT INTO usuario (nombre_usuario, apellidos, correo, contrasena) VALUES (?, ?, ?, ?)";
    
    try {
        $stmt = $pdo->prepare($sql);
        // Encriptamos la contraseña
        $pass_encriptada = password_hash($password, PASSWORD_BCRYPT);
        
        $stmt->execute([$nombre, $apellidos, $correo, $pass_encriptada]);

        // 2. AUTO-LOGIN 
        $nuevo_id_usuario = $pdo->lastInsertId();
        
        $_SESSION['user_id'] = $nuevo_id_usuario;
        $_SESSION['nombre'] = $nombre;

        // 3. REDIRECCIÓN INTELIGENTE
        if (isset($_SESSION['carrito']) && count($_SESSION['carrito']) > 0) {
            header("Location: carrito.php");
        } else {
            header("Location: index.php");
        }
        exit;

    } catch (PDOException $e) {
        $error = "Error al registrarse: " . $e->getMessage();
    }
}
?>
```
---
# Conclusión:
Con esto creamos contraseñas hasheadas sseguras e irreversibles y sentencias preparadas para proteger tanto a la aplicación como a los usuarios.
Un error sería almacenar las contraseñas en texto plano, puesto que si alguien accediera a la BBDD tendría acceso a todas las cuentas, por eso usamos funciones como `password_hash`, también tenemos que tener cuidado con los nombres de las columnas de la BBDD, pueso que un error tipográfico provocaría que el bloque `try-catch` saltara inmediatamente.