**PROGRAMACIÓN (/back)**

`Archivo: back/inc/conexion_bd.php`

# Introducción:
Todo el proyecto depende de un único punto de entrada a la base de datos, en lugar de repetir las credenciales en cada archivo, las hemos centralizado en `conexion_bd.php`, utilizando la librería `PHP Data Objects` porque nos permite trabajar con una capa de abstracción segura y orientada a objetos, facilitando el manejo de excepciones mediante `try-catch`.

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
En esta parte implementamos la lógica de lectura del catálogo, el objetivo principal de esta clase es servir de puente entre la tabla producto de la base de datos y las vistas donde el cliente elige qué comer, decidimos definir dos métodos diferenciados según la necesidad, el primero es `listarTodo()`, este método se utiliza para llenar el `Grid` del catálogo principal, como la consulta `SELECT * FROM` producto no requiere parámetros externos, utilizamos el método directo `$this->db->query($sql)` y al esperar múltiples filas, utilizamos `fetchAll()`, que me devuelve un array de arrays conteniendo todo el inventario de golpe.

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

- Lógica de Negocio (PedidoControlador), esto el corazón del sistema, aquí he gestionamos la Integridad Referencial desde el código, coordinando la cabecera de un pedido con sus múltiples líneas de productos. 
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

