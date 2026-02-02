<!DOCTYPE html>
<html lang="es">
    <head>
        <title>Tienda</title>
        <style>
            /* Mobile-only styles (Screen width up to 768px) */
@media screen and (max-width: 768px) {
    main {
        padding: 20px;
        flex-grow: 1; /* Pushes footer to bottom if content is short */
    }

    /* Stack products vertically */
    #productos div {
        display: flex;
        flex-direction: column;
        gap: 15px;
    }

    article {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px;
        border: 1px solid #ddd;
        border-radius: 8px;
        background: #f9f9f9;
    }

    /* Larger buttons for easy tapping */
    button {
        padding: 12px 24px;
        font-size: 1.1rem;
        background-color: #000;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        -webkit-tap-highlight-color: transparent;
    }

    button:active {
        background-color: #444; /* Visual feedback on touch */
        transform: scale(0.98);
    }

    /* Form styling */
    input[type="text"] {
        display: block;
        width: 100%;
        margin-bottom: 15px;
        padding: 15px;
        box-sizing: border-box; /* Ensures padding doesn't break width */
        font-size: 16px; /* Prevents iOS auto-zoom on focus */
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    /* Style the div acting as a button */
    #enviar {
        background: #28a745;
        color: white;
        text-align: center;
        padding: 18px;
        font-weight: bold;
        border-radius: 5px;
        margin-top: 10px;
        text-transform: uppercase;
        cursor: pointer;
    }

    #enviar:active {
        background: #218838;
    }

    h3 {
        margin-top: 30px;
        border-bottom: 2px solid #eee;
        padding-bottom: 10px;
    }
}
        </style>
        <meta charset="utf-8">
    </head>
    <body>
        <header>
            <h1>Microtienda</h1>
        </header>
        <main>
            <section id="productos">
        <h3>Productos</h3>
        <div>
          <?php
            $host = "localhost";
            $user = "microtienda";
            $pass = "Microtienda123$";
            $db   = "microtienda";
            $conexion = new mysqli($host, $user, $pass, $db);
            $sql = "SELECT * FROM productos;";
            $resultado = $conexion->query($sql);
            while ($fila = $resultado->fetch_assoc()) {
          ?>
            <article>
              <h4><?= $fila['nombre'] ?></h4>
              <button nombre="<?= $fila['nombre'] ?>"><?= $fila['precio'] ?>€</button>
            </article>
          <?php }?>
        </div>
      </section>
        <section>
            <h3>Datos de cliente</h3>
            <div>
                <input type="text" id="nombre" placeholder="nombre">
                <input type="text" id="apellidos" placeholder="apellidos">
                <input type="text" id="email" placeholder="email">
                <div id="enviar">Enviar pedido</div>
            </div>
        </section>
        </main>
        <footer>
            (c) 2026 Alfredo Martínez Cantero
        </footer>
    </body>
    <script>
        var fecha = new Date();
        var pedido = {
            cliente:{},                 // UN cliente
            productos:[],               // VARIOS productos, por eso se usa "[]"
            pedido:{                    // UN pedido
                "numero":Date.now(),
                "fecha":fecha.getFullYear()+"-"+(fecha.getMonth()+1)+"-"+fecha.getDate()
            }    
        };

        ////// Atrapa productos y los mete en el carro
        let botones = document.querySelectorAll("button"); // Siempre que hagamos un querySelectorAll usaremos a continuación un "forEach"
        botones.forEach(function(boton){
            boton.onclick = function(){
                pedido.productos.push({
                    "nombre":this.getAttribute("nombre"),
                    "precio":this.textContent
                    })
                    console.log(pedido)
            }
        })
        ////// Atrapa los datos del cliente
        let boton_enviar = document.querySelector("#enviar");
        boton_enviar.onclick = function(){
            let nombre_cliente = document.querySelector("#nombre").value;
            let apellidos_cliente = document.querySelector("#apellidos").value;
            let email_cliente = document.querySelector("#email").value;
            pedido.cliente = {
                "nombre":nombre_cliente,
                "apellidos":apellidos_cliente,
                "email":email_cliente
            }
            console.log(pedido)
        }
    </script>
</html>