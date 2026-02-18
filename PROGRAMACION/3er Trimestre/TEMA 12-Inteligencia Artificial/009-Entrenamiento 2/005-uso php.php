<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['prompt'])) {
    header('Content-Type: text/plain; charset=UTF-8');

    $prompt = trim($_POST['prompt']);
    if ($prompt === '') {
        http_response_code(400);
        echo "No prompt provided";
        exit;
    }
    if (mb_strlen($prompt) > 4000) {
        http_response_code(413);
        echo "Prompt too long";
        exit;
    }

    // Python que SÍ tiene torch instalado
    $python = '/usr/bin/python3';

    // Script Python que hace la inferencia
    $script = __DIR__ . DIRECTORY_SEPARATOR . '003-Inferir.py';

    if (!is_file($script)) {
        http_response_code(500);
        echo "Python infer script not found: $script";
        exit;
    }

    $escapedScript = escapeshellarg($script);
    $escapedPrompt = escapeshellarg($prompt);

    // NO USAR entidades HTML → usar 2>&1 real
    $cmd = $python . ' ' . $escapedScript . ' ' . $escapedPrompt . ' 2>&1';

    $output = shell_exec($cmd);

    if ($output === null) {
        http_response_code(500);
        echo "Error executing the model.";
        exit;
    }

    echo trim($output);
    exit;
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mini ChatGPT (Local)</title>
<style>
:root {
    --bg: #0f172a;
    --panel: #111827;
    --panel-2: #0b1220;
    --text: #e5e7eb;
    --muted: #9ca3af;
    --accent: #22c55e;
    --accent-2: #10b981;
    --user: #1d4ed8;
    --bot: #334155;
    --border: #1f2937;
}
* { box-sizing: border-box; }
body {
    margin: 0;
    background: linear-gradient(180deg, var(--bg), var(--panel-2));
    color: var(--text);
    font-family: Arial, sans-serif;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}
.wrap {
    width: 100%;
    max-width: 900px;
    height: 92vh;
    display: flex;
    flex-direction: column;
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow: hidden;
    background: #111827;
}
.header {
    padding: 16px 20px;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 10px;
}
.logo {
    width: 34px;
    height: 34px;
    border-radius: 10px;
    display: grid;
    place-items: center;
    background: green;
    color: white;
    font-weight: bold;
}
.title { font-weight: 700; font-size: 16px; }
.sub { color: var(--muted); font-size: 12px; }
.chat {
    flex: 1;
    overflow-y: auto;
    padding: 16px;
}
.msg {
    display: flex;
    gap: 10px;
    margin: 8px 0;
    max-width: 85%;
}
.msg.user {
    margin-left: auto;
    flex-direction: row-reverse;
}
.bubble {
    padding: 12px 14px;
    border-radius: 14px;
    background: #333;
    border: 1px solid #444;
}
.user .bubble { background: #1d4ed8; }
.bot .bubble { background: #334155; }
.avatar {
    width: 28px;
    height: 28px;
    border-radius: 8px;
    display: grid;
    place-items: center;
    background: #666;
    color: white;
}
.footer {
    padding: 14px;
    border-top: 1px solid var(--border);
}
.form {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 10px;
}
.input {
    padding: 10px;
    border-radius: 8px;
    border: 1px solid #555;
    background: #222;
    color: white;
}
.btn {
    padding: 10px 16px;
    border-radius: 8px;
    border: none;
    background: #22c55e;
    color: black;
    font-weight: bold;
    cursor: pointer;
}
</style>
</head>
<body>
<div class="wrap">
    <div class="header">
        <div class="logo">AI</div>
        <div>
            <div class="title">Mini ChatGPT (local)</div>
            <div class="sub">Modelo offline</div>
        </div>
    </div>

    <div id="chat" class="chat">
        <div class="msg bot">
            <div class="avatar bot">A</div>
            <div class="bubble">¡Hola! Envíame un mensaje.</div>
        </div>
    </div>

    <div class="footer">
        <form id="form" class="form" autocomplete="off">
            <input id="input" class="input" type="text" required>
            <button id="send" class="btn">Enviar</button>
        </form>
    </div>
</div>

<script>
const chat = document.getElementById('chat');
const form = document.getElementById('form');
const input = document.getElementById('input');
const sendBtn = document.getElementById('send');

function addMessage(role, text) {
    const wrap = document.createElement('div');
    wrap.className = 'msg ' + role;
    wrap.innerHTML = `
        <div class="avatar ${role}">${role === 'user' ? 'U' : 'A'}</div>
        <div class="bubble">${text}</div>
    `;
    chat.appendChild(wrap);
    chat.scrollTop = chat.scrollHeight;
}

form.addEventListener('submit', async e => {
    e.preventDefault();

    const prompt = input.value.trim();
    if (!prompt) return;

    addMessage('user', prompt);
    input.value = '';

    const res = await fetch("", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: "prompt=" + encodeURIComponent(prompt)
    });

    const text = await res.text();
    addMessage('bot', text);
});
</script>
</body>
</html>