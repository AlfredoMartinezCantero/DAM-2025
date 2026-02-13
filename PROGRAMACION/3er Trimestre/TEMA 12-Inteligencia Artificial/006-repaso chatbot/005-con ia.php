<?php
// Si no existe, creo una memoria de preguntas y respuestas
    session_start();
    if(!isset($_SESSION['preguntas'])){
        $_SESSION['preguntas'] = [];
    }
    if(!isset($_SESSION['respuestas'])){
        $_SESSION['respuestas'] = [];
    }
?>

<!DOCTYPE html>
<html>
    <head>
        <style>         
html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
    background: #e5ddd5; /* fondo tipo WhatsApp */
    color: #111827;
}

body {
    display: flex;
    justify-content: center;
    align-items: center;
}

/* Contenedor principal */
form {
    background: #f7f8fa;
    border: 1px solid #e6ebf2;
    padding: 16px;
    border-radius: 16px;
    height: 540px;            /* más alto */
    width: 420px;             /* un poco más ancho */
    display: flex;
    flex-direction: column;
    gap: 12px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
    overflow: hidden;         /* oculta desbordes del contenedor */
}

/* Área de conversación (es el primer <p> dentro del form) */
form > p:first-child {
    flex: 1;
    margin: 0;
    padding: 12px;
    background: linear-gradient(180deg, #f1f4f8 0%, #eef2f7 100%);
    border: 1px solid #e6ebf2;
    border-radius: 14px;
    overflow-y: auto;         /* scroll para el chat */
    display: flex;
    flex-direction: column;
}

/* Estilo base de cada burbuja (los <p> que se pintan dentro) */
form > p:first-child > p {
    position: relative;
    max-width: 92%;           /* más grande */
    padding: 14px 18px;       /* más acolchado */
    border-radius: 18px;
    margin: 8px 0;
    font-size: 15.5px;        /* un poco mayor */
    line-height: 1.5;
    box-shadow: 0 1px 2px rgba(0,0,0,0.06);
    word-wrap: break-word;
    white-space: pre-wrap;
    border: 1px solid transparent;
}

/* Tus mensajes (preguntas) — a la derecha en verde suave */
form > p:first-child > p:nth-child(odd) {
    align-self: flex-end;
    margin-left: auto;
    background: #e7f7df;               /* verde pastel profesional */
    border-color: #cfeec4;
    color: #0f5132;                     /* texto verde oscuro legible */
}

/* Cola (tail) de la burbuja derecha */
form > p:first-child > p:nth-child(odd)::after {
    content: "";
    position: absolute;
    right: -6px;
    bottom: 12px;
    width: 12px;
    height: 12px;
    background: #e7f7df;
    border-right: 1px solid #cfeec4;
    border-bottom: 1px solid #cfeec4;
    transform: rotate(45deg);
    border-bottom-right-radius: 2px;
}

/* Respuestas de la IA — a la izquierda en blanco */
form > p:first-child > p:nth-child(even) {
    align-self: flex-start;
    margin-right: auto;
    background: #ffffff;
    border-color: #e6ebf2;
    color: #111827;
}

/* Cola (tail) de la burbuja izquierda */
form > p:first-child > p:nth-child(even)::after {
    content: "";
    position: absolute;
    left: -6px;
    bottom: 12px;
    width: 12px;
    height: 12px;
    background: #ffffff;
    border-left: 1px solid #e6ebf2;
    border-bottom: 1px solid #e6ebf2;
    transform: rotate(45deg);
    border-bottom-left-radius: 2px;
}

/* Inputs */
input[type="text"] {
    padding: 12px 14px;
    border-radius: 24px;
    border: 1px solid #cfd8e3;
    outline: none;
    background: #ffffff;
    font-size: 14.5px;
    transition: border-color 0.2s, box-shadow 0.2s;
}

input[type="text"]:focus {
    border-color: #94b8ff;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15);
}

/* Botón enviar */
input[type="submit"] {
    padding: 12px 16px;
    border-radius: 24px;
    border: none;
    background: #22c55e;      /* verde profesional */
    color: white;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.2s, transform 0.02s;
    box-shadow: 0 1px 2px rgba(0,0,0,0.08);
}

input[type="submit"]:hover {
    background: #16a34a;
}

input[type="submit"]:active {
    transform: translateY(1px);
}

/* Ajustes generales para cualquier <p> suelto que no sea burbuja */
p {
    margin: 0;
}

        </style>
    </head>
    <body>
        <form action="?" method="post">
            <p>
            <?php
            // En primer lugar enviamos la pregunta a la IA
                $OLLAMA_URL = "http://localhost:11434/api/generate";
                $MODEL = "qwen2.5-coder:7b";
                $prompt = $_POST['mensaje'].". Resume tu respuesta en una unica frase";
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

                // Ahora metro la pregunta y respuesta en los arrays
                $_SESSION['preguntas'][] = $_POST['mensaje'];
                $_SESSION['respuestas'][] = $result["response"];

                // Y ahora con un bucle for, pintamos la conversación
                for($i = 0;$i<count($_SESSION['preguntas']);$i++){
                    echo '<p>'.$_SESSION['preguntas'][$i].'</p>';
                    echo '<p>'.$_SESSION['respuestas'][$i].'</p>';
                }
            ?>
            </p>
            <input type="text" name="mensaje">
            <input type="submit">
        </form>
    </body>
</html>