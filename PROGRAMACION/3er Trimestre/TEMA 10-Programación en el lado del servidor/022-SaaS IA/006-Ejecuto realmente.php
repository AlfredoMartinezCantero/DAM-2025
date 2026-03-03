<?php
declare(strict_types=1);

/* ===CONFIGURACIÓN
===*/
$OLLAMA_URL = "http://localhost:11434/api/generate";
$MODEL      = "qwen2.5-coder:7b";

$db_host = "localhost";
$db_user = "saasia";
$db_pass = "SaasIA123$";
$db_name = "saasia";

/* ===FUNCIONES
===*/

function h($s){
    return htmlspecialchars((string)$s, ENT_QUOTES, 'UTF-8');
}

function ejecutarSQL($sql, $db_host, $db_user, $db_pass, $db_name){
    $mysqli = new mysqli($db_host, $db_user, $db_pass, $db_name);

    if($mysqli->connect_errno){
        return ["error" => "Error conexión DB: ".$mysqli->connect_error];
    }

    $resultado = $mysqli->query($sql);

    if($resultado === false){
        return ["error" => $mysqli->error];
    }

    // SELECT devuelve resultset
    if($resultado instanceof mysqli_result){
        $filas = [];
        while($row = $resultado->fetch_assoc()){
            $filas[] = $row;
        }
        return ["type" => "select", "data" => $filas];
    }

    // INSERT/UPDATE/DELETE
    return [
        "type" => "action",
        "affected" => $mysqli->affected_rows
    ];
}

/* ===PROCESAMIENTO
===*/

$sql_generado = "";
$resultado_db = null;
$error = "";

if($_SERVER["REQUEST_METHOD"] === "POST" && !empty($_POST["peticion"])){

    $peticion = trim($_POST["peticion"]);

    $prompt = "
Tengo una base de datos que tiene una tabla clientes con esta estructura:

CREATE TABLE clientes (
  id INT(11) NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(255),
  apellidos VARCHAR(255),
  email VARCHAR(255),
  poblacion VARCHAR(255),
  fecha_de_nacimiento DATE,
  PRIMARY KEY (id)
);

Lo que quiero es que me des el SQL para responder a
la siguiente petición por parte del usuario:

".$peticion."

Lo que necesito es que me des el codigo SQL para esa peticion.
No me des nada más que código SQL. Tampoco quiero fences.
Cuando hagas consultas con Where, usa WHERE x LIKE '%y%'.
El codigo resultante debe ser SQL puro, nunca markdown.
";

    $data = [
        "model" => $MODEL,
        "prompt" => $prompt,
        "stream" => false
    ];

    $ch = curl_init($OLLAMA_URL);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        "Content-Type: application/json"
    ]);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));

    $response = curl_exec($ch);
    curl_close($ch);

    $result = json_decode($response, true);
    $sql_generado = trim($result["response"] ?? "");

    // Validación básica: solo permitir SELECT, INSERT, UPDATE, DELETE
    if(!preg_match("/^(SELECT|INSERT|UPDATE|DELETE)/i", $sql_generado)){
        $error = "El modelo no devolvió una sentencia SQL válida.";
    } else {
        $resultado_db = ejecutarSQL(
            $sql_generado,
            $db_host,
            $db_user,
            $db_pass,
            $db_name
        );
    }
}
?>
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>SaasIA SQL Runner</title>
<style>
/*ESTILO GLOBAL*/
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;
    background: #f3f4f6;
    color: #1f2937;
    line-height: 1.6;
}

/*HEADER*/
header {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    color: white;
    padding: 30px 20px;
    text-align: center;
    box-shadow: 0 2px 6px rgba(0,0,0,0.25);
}

header h1 {
    margin: 0;
    font-weight: 600;
    font-size: 28px;
}

/*CONTENEDOR PRINCIPAL*/
main {
    padding: 40px 20px;
    max-width: 1000px;
    margin: auto;
    animation: fadeIn 0.3s ease-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
}

/*FORMULARIO*/
form {
    display: flex;
    gap: 12px;
    margin-bottom: 30px;
}

input[type=text] {
    flex: 1;
    padding: 14px;
    border: 1px solid #d1d5db;
    background: #ffffff;
    border-radius: 8px;
    font-size: 16px;
    transition: 0.2s ease;
}

input[type=text]:focus {
    outline: none;
    border-color: #2563eb;
    box-shadow: 0 0 0 3px rgba(37,99,235,0.25);
}

button {
    padding: 14px 24px;
    background: #2563eb;
    border: none;
    color: white;
    border-radius: 8px;
    font-size: 15px;
    cursor: pointer;
    transition: 0.2s ease;
    font-weight: 500;
}

button:hover {
    background: #1d4ed8;
}

/*SQL BOX*/
.sql-box {
    background: #0f172a;
    color: #93c5fd;
    padding: 18px;
    font-family: "JetBrains Mono", monospace;
    border-radius: 8px;
    margin-bottom: 20px;
    white-space: pre-wrap;
    border: 1px solid #1e293b;
    box-shadow: 0 2px 6px rgba(0,0,0,0.20);
}

/*TABLAS*/
table {
    width: 100%;
    border-collapse: collapse;
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}

th {
    background: #f1f5f9;
    padding: 12px;
    text-align: left;
    font-size: 14px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.03em;
}

td {
    padding: 12px;
    border-top: 1px solid #e5e7eb;
    font-size: 15px;
}

tr:hover {
    background: #f9fafb;
}

/*ALERTAS*/
.info,
.error {
    padding: 14px 18px;
    border-radius: 8px;
    margin-bottom: 20px;
    font-size: 15px;
}

.info {
    background: #ecfdf5;
    border-left: 4px solid #059669;
}

.error {
    background: #fee2e2;
    border-left: 4px solid #dc2626;
}
</style>
</head>
<body>

<header>
<h1>SaasIA - Generador y Ejecutor SQL</h1>
</header>

<main>

<form method="POST">
    <input type="text" name="peticion" placeholder="Ej: clientes de Valencia">
    <button type="submit">Ejecutar</button>
</form>

<?php if($sql_generado): ?>
    <div class="sql-box"><?= h($sql_generado) ?></div>
<?php endif; ?>

<?php if($error): ?>
    <div class="error"><?= h($error) ?></div>
<?php endif; ?>

<?php if($resultado_db): ?>

    <?php if(isset($resultado_db["error"])): ?>
        <div class="error"><?= h($resultado_db["error"]) ?></div>
    <?php elseif($resultado_db["type"] === "select"): ?>

        <?php if(empty($resultado_db["data"])): ?>
            <div class="info">Consulta ejecutada correctamente. Sin resultados.</div>
        <?php else: ?>
            <table>
                <thead>
                    <tr>
                        <?php foreach(array_keys($resultado_db["data"][0]) as $col): ?>
                            <th><?= h($col) ?></th>
                        <?php endforeach; ?>
                    </tr>
                </thead>
                <tbody>
                    <?php foreach($resultado_db["data"] as $fila): ?>
                        <tr>
                            <?php foreach($fila as $valor): ?>
                                <td><?= h($valor) ?></td>
                            <?php endforeach; ?>
                        </tr>
                    <?php endforeach; ?>
                </tbody>
            </table>
        <?php endif; ?>

    <?php elseif($resultado_db["type"] === "action"): ?>
        <div class="info">
            Sentencia ejecutada correctamente.
            Filas afectadas: <?= h($resultado_db["affected"]) ?>
        </div>
    <?php endif; ?>

<?php endif; ?>

</main>
</body>
</html>