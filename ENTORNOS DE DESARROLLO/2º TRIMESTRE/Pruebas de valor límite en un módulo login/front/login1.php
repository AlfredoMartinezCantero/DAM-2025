<?php
session_start();
require_once '../back/inc/conexion_bd.php';

/**
 * --- BLOQUE DE REPARACIÓN PARA CLASES DE EQUIVALENCIA ---
 * Esto asegura que 'usuario123' exista con la clave 'Pass1234'
 */
$hashEquivalencia = password_hash('Pass1234', PASSWORD_BCRYPT);
// Primero intentamos insertarlo, si ya existe, actualizamos su contraseña
$check = $pdo->prepare("SELECT id FROM usuario WHERE nombre_usuario = 'usuario123'");
$check->execute();
if (!$check->fetch()) {
    $ins = $pdo->prepare("INSERT INTO usuario (nombre_usuario, contrasena) VALUES ('usuario123', ?)");
    $ins->execute([$hashEquivalencia]);
} else {
    $upd = $pdo->prepare("UPDATE usuario SET contrasena = ? WHERE nombre_usuario = 'usuario123'");
    $upd->execute([$hashEquivalencia]);
}
// -------------------------------------------------------

$error = "";

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $usuarioInput = trim($_POST['correo']); 
    $passInput = trim($_POST['pass']);

    // --- VALIDACIÓN DE FORMATO (Clases de Equivalencia) ---
    if (empty($usuarioInput)) {
        $error = "Usuario vacío.";
    } elseif (strlen($usuarioInput) < 5 || strlen($usuarioInput) > 20) {
        $error = "Usuario: longitud incorrecta (5-20).";
    } elseif (!ctype_alnum($usuarioInput)) {
        $error = "Usuario: solo se permiten letras y números.";
    }
    elseif (empty($passInput)) {
        $error = "Contraseña vacía.";
    } elseif (strlen($passInput) < 8 || strlen($passInput) > 16) {
        $error = "Contraseña: longitud incorrecta (8-16).";
    } 
    elseif (!preg_match('/[A-Za-z]/', $passInput) || !preg_match('/[0-9]/', $passInput)) {
        $error = "Contraseña: debe combinar letras y números.";
    }
    // --- VALIDACIÓN DE IDENTIDAD ---
    else {
        $stmt = $pdo->prepare("SELECT * FROM usuario WHERE nombre_usuario = ?");
        $stmt->execute([$usuarioInput]);
        $user = $stmt->fetch();

        if ($user && password_verify($passInput, $user['contrasena'])) {
            echo "<div style='background: #d4edda; color: #155724; padding: 20px; text-align: center; border: 1px solid #c3e6cb; font-family: sans-serif;'>
                    <h3>✅ ACCESO CONCEDIDO (Clase Válida)</h3>
                    <p>Usuario: <b>" . htmlspecialchars($user['nombre_usuario']) . "</b></p>
                  </div>";
        } else {
            // Debug para saber qué está fallando
            $error = "Formato OK, pero no coincide en BD. (Input: $usuarioInput | Pass: $passInput)";
        }
    }
}
?>

<?php @include 'inc/cabecera.php'; ?>
<div style="max-width: 450px; margin: 40px auto; font-family: sans-serif;">
    <form method="POST" style="background: #fff; padding: 25px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); border: 1px solid #ccc;">
        <h2 style="text-align: center;">Test de Equivalencia</h2>
        
        <?php if($error): ?>
            <div style="background: #f8d7da; color: #721c24; padding: 10px; margin-bottom: 15px; border-radius: 4px; border: 1px solid #f5c6cb;">
                ⚠️ <?= $error ?>
            </div>
        <?php endif; ?>

        <div style="margin-bottom: 15px;">
            <label style="display:block; margin-bottom:5px;">Nombre de usuario:</label>
            <input type="text" name="correo" required style="width: 100%; padding: 8px; box-sizing: border-box;" placeholder="usuario123">
        </div>

        <div style="margin-bottom: 15px;">
            <label style="display:block; margin-bottom:5px;">Contraseña:</label>
            <input type="password" name="pass" required style="width: 100%; padding: 8px; box-sizing: border-box;" placeholder="Pass1234">
        </div>

        <button type="submit" style="width: 100%; padding: 10px; background: #007bff; color: #fff; border: none; border-radius: 4px; cursor: pointer; font-weight: bold;">
            Ejecutar Prueba
        </button>
    </form>
</div>
<?php @include 'inc/piedepagina.php'; ?>