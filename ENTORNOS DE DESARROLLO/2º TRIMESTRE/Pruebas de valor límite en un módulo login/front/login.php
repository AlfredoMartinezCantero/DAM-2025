<?php
session_start();
require_once '../back/inc/conexion_bd.php';

$hashSeguro = password_hash('12345678', PASSWORD_BCRYPT);
$repair = $pdo->prepare("UPDATE usuario SET contrasena = ? WHERE nombre_usuario = 'admin'");
$repair->execute([$hashSeguro]);

$error = "";

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Limpiamos espacios con trim()
    $usuarioInput = trim($_POST['correo']); 
    $passInput = trim($_POST['pass']);

    // PRUEBA DE VALORES LÍMITE
    $longitudUser = strlen($usuarioInput);
    $longitudPass = strlen($passInput);

    if ($longitudUser < 5) {
        $error = "CASO 1: Rechazo. Usuario demasiado corto ($longitudUser caracteres).";
    } elseif ($longitudUser > 20) {
        $error = "CASO 4: Rechazo. Usuario demasiado largo ($longitudUser caracteres).";
    } 
    elseif ($longitudPass < 8) {
        $error = "CASO 5: Rechazo. Contraseña demasiado corta ($longitudPass caracteres).";
    } elseif ($longitudPass > 16) {
        $error = "CASO 8: Rechazo. Contraseña demasiado larga ($longitudPass caracteres).";
    } 
    else {
        // Buscamos en la BD
        $stmt = $pdo->prepare("SELECT * FROM usuario WHERE nombre_usuario = ?");
        $stmt->execute([$usuarioInput]);
        $user = $stmt->fetch();

        if ($user) {
            $hashBD = trim($user['contrasena']);

            if (password_verify($passInput, $hashBD)) {
                echo "<div style='background: #d4edda; color: #155724; padding: 20px; text-align: center; border: 1px solid #c3e6cb; font-family: sans-serif; position: relative; z-index: 100;'>
                        <h3>✅ ACCESO CONCEDIDO</h3>
                        <p>Los datos cumplen los límites y el usuario es correcto.</p>
                      </div>";
            } else {
                $error = "Contraseña incorrecta. (Longitud enviada: " . strlen($passInput) . " | Longitud en BD: " . strlen($hashBD) . ")";
            }
        } else {
            $error = "Límites correctos, pero el usuario [$usuarioInput] no existe en la BD.";
        }
    }
}
?>

<?php @include 'inc/cabecera.php'; ?>

<link rel="stylesheet" href="css/estilo.css">

<div class="container" style="max-width: 450px; margin: 50px auto; padding: 20px; font-family: sans-serif;">
    
    <div style="text-align: center; margin-bottom: 20px;">
        <h2 style="color: #333;">Control de Acceso</h2>
        <p style="font-size: 0.8em; color: #666;">Pruebas de Valores Límite</p>
    </div>

    <?php if(!empty($error)): ?>
        <div style="background: #f8d7da; color: #721c24; padding: 10px; border-radius: 5px; margin-bottom: 15px; border: 1px solid #f5c6cb;">
            ⚠️ <?= $error ?>
        </div>
    <?php endif; ?>

    <form method="POST" style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        
        <div style="margin-bottom: 15px;">
            <label style="font-weight: bold; display: block; margin-bottom: 5px;">Usuario (5-20 carac.)</label>
            <input type="text" name="correo" required placeholder="Escribe 'admin'" style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 8px; box-sizing: border-box;">
        </div>

        <div style="margin-bottom: 25px;">
            <label style="font-weight: bold; display: block; margin-bottom: 5px;">Contraseña (8-16 carac.)</label>
            <input type="password" name="pass" required placeholder="Escribe '12345678'" style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 8px; box-sizing: border-box;">
        </div>

        <button type="submit" style="width: 100%; background: #28a745; color: white; border: none; cursor: pointer; padding: 15px; border-radius: 8px; font-size: 1rem; font-weight: bold;">
            Validar Datos
        </button>
    </form>
</div>

<?php @include 'inc/piedepagina.php'; ?>