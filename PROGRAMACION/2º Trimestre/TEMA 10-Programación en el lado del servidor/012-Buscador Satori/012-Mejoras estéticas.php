<!doctype html>
<html lang="es">
  <head>
    <title>Satori Búsqueda</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <style>
        :root {
            --primary: #2563eb;
            --bg-body: #f8fafc;
            --bg-card: #ffffff;
            --text-main: #1e293b;
            --text-muted: #64748b;
            --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        }

        body, html { margin: 0; padding: 0; font-family: system-ui, -apple-system, sans-serif; background-color: var(--bg-body); color: var(--text-main); }
        
        header { background-color: var(--bg-card); box-shadow: var(--shadow); padding: 1.5rem 1rem; display: flex; flex-direction: column; align-items: center; gap: 1rem; position: sticky; top: 0; z-index: 10; }
        .brand { display: flex; align-items: center; gap: 15px; }
        .brand img { width: 50px; border-radius: 8px; }
        .brand h1 { font-size: 1.8rem; margin: 0; }
        
        form { width: 100%; max-width: 600px; }
        input[type="text"] { width: 100%; padding: 12px 20px; font-size: 1rem; border: 2px solid #e2e8f0; border-radius: 50px; outline: none; box-sizing: border-box; transition: all 0.3s ease; }
        input[type="text"]:focus { border-color: var(--primary); box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.1); }
        
        main { max-width: 800px; margin: 2rem auto; padding: 0 1rem; display: grid; gap: 1.5rem; }
        
        article { background: var(--bg-card); border-radius: 12px; border: 1px solid #e2e8f0; transition: transform 0.2s, box-shadow 0.2s; overflow: hidden; }
        article:hover { transform: translateY(-3px); box-shadow: var(--shadow); border-color: var(--primary); }
        
        .card-link { display: block; padding: 1.5rem; text-decoration: none; color: inherit; height: 100%; }
        .card-link h3 { margin: 0 0 0.5rem 0; font-size: 1.25rem; color: var(--primary); }
        article:hover h3 { text-decoration: underline; }
        .url-text { color: var(--text-muted); font-size: 0.85rem; display: block; word-break: break-all; }

        @media (min-width: 768px) { header { flex-direction: row; justify-content: center; gap: 2rem; } }
    </style>
  </head>
  <body>
    <header>
        <div class="brand">
            <img src="satorilogo.png" alt="Logo">
            <h1>Satori</h1>
        </div>
        <form method="POST" action="?">
            <input 
                type="text" 
                name="criterio" 
                placeholder="Busca algo interesante..."
                value="<?= $_POST['criterio'] ?? '' ?>"
                autocomplete="off">
        </form>
    </header>

    <main>
        <?php
        $host = "localhost";
        $user = "satori";
        $pass = "Satori123$";
        $db   = "satori";

        @$conexion = new mysqli($host, $user, $pass, $db);
        
        if (!$conexion->connect_error) {
            $criterio = $_POST['criterio'] ?? '';
            
            // OPTIMIZACIÓN SQL:
            // Usamos DISTINCT para forzar a la base de datos a eliminar duplicados exactos
            // de título y URL antes de enviarlos a PHP.
            $sql = "SELECT DISTINCT titulo, url FROM paginas WHERE titulo LIKE '%".$criterio."%'";
            
            $resultado = $conexion->query($sql);

            if ($resultado && $resultado->num_rows > 0) {
                                while ($fila = $resultado->fetch_assoc()) { ?>
                                    <article>
                                        <a href="<?= $fila['url'] ?>" class="card-link">
                                            <h3><?= htmlspecialchars($fila['titulo']) ?></h3>
                                            <span class="url-text"><?= htmlspecialchars($fila['url']) ?></span>
                                        </a>
                                    </article>
                                <?php }
                            } else {
                                echo '<p style="text-align: center; color: var(--text-muted);">No se encontraron resultados.</p>';
                            }
                            $conexion->close();
                        } else {
                            echo '<p style="text-align: center; color: red;">Error de conexión a la base de datos.</p>';
                        }
                        ?>
                    </main>
                  </body>
                </html>