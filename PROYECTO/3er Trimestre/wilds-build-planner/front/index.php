<?php include "../inc/cabecera.php"; ?>

<main>
    <section id="planner">
        <div class="selector-pieza" id="casco">
            <img src="img/iconos/helmet.png" alt="Casco">
            <select name="select-casco">
                <option value="0">Selecciona casco...</option>
            </select>

            <select name="select-pechera">
                <option value="0">Selecciona pechera...</option>
            </select>

            <select name="select-barzos">
                <option value="0">Selecciona barzos...</option>
            </select>

            <select name="select-faja">
                <option value="0">Selecciona faja...</option>
            </select>

            <select name="select-botas">
                <option value="0">Selecciona botas...</option>
            </select>
        </div>
        <div id="visualizador-personaje">
            <div class="placeholder-hunter"></div>
        </div>
    </section>

    <aside id="stats-panel">
        <div class="card" id="total-stats">
            <h3>Estadísticas Totales</h3>
            <ul>
                <li>Defensa: <span id="def-val">0</span></li>
                <li>Fuego: <span id="fire-val">0</span></li>
                </ul>
        </div>

        <div class="card" id="ia-assistant">
            <h3>Asistente de Build (IA)</h3>
            <p>¿Qué buscas cazar hoy?</p>
            <input type="text" placeholder="Ej: Build para Rathalos...">
            <button id="btn-consultar-ia">Consultar</button>
        </div>
    </aside>
</main>

<?php include "../inc/pie.php"; ?>