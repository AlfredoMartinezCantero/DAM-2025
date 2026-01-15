**INDEX.PHP (PÁGINA PRINCIPAL)**

# Introducción:
Antes de profundizar en las vistas tuvimos que organizar el proyecto, separando claramente la lógica en dos carpetas, `front/` y `back/`.

El flujo del usuario lo diseñamos de forma lineal, primero se muestra el `index.php` para captar visualmente la atención, despúes iríamos al `catálogo` para la selección de productos, a continuación una confirmación mediante `carrito.php` y una vez tienes los artículos seleccionados has de pasar por el `registro.php/login.php` para vincular tu carrito a un usuario, y ya por último el bloque de `finalizacion.php`, el cual muestra un feedback positivo cuando se procesa el pedido.

La vista `index.php` funciona como escaparate. Aquí el objetivo que tuvimos fue utilizar HTML5 para jerarquizar el contenido y CSS Flexbox para centrar los elementos perfectamente en cualquier pantalla, también hemos evitado el uso excesivo de `<div>` genéricos, prefiriendo etiquetas con significado como `<main>` para el contenido principal y `<footer>` para el pie de página.

**HTML**

---
```
<main class="hero-section">
    <img src="img/logo_home.png" class="hero-logo-img">
    <div class="action-grid">
        <a href="catalogo.php" class="btn-hero">Ver La Carta</a>
        </div>
</main>
```
---
**CSS**

---
```
.hero-section {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 70vh;
}
```
---

**Explicación del HTML**

`<main>` indica al navegador que este es el contenido único y central de esta página específica. 
`<a>` es como usar "anclas" para la navegación, pero visualmente las transformamos en botones mediante clases CSS.

**Explicación del CSS**

`display: flex;` organiza los elementos en una sola dirección, ya sea en una fila horizontal o vertical.
`flex-direction: column;` alinea los elementos (logo, texto, botones) uno debajo de otro en lugar de en fila. 
`align-items: center; y justify-content: center;` centran el contenido tanto vertical como horizontalmente.

# Conclusión:
Con este bloque del proyecto mi compañera y yo hemos conseguido comprender la base del uso y personalización que se puede lograr, flexbox además permite un control total sobre la distribución del espacio, independientemente del tamaño de la pantalla del dispositivo.

Un error común es que al intentar centrar verticalmente con Flexbox a veces olvidábamos definir una altura, si no hubiesemos puesto `min-height: 70vh`, el contenedor solo mediría lo que ocupa su contenido, y la propiedad `justify-content: center;` no tendría espacio "sobrante" para repartir, por lo que el centrado vertical no funcionaría.

---
**ESTRATEGIA VISUAL CSS**
Para garantizar el atractivo visual en toda la web y facilitar el mantenimiento, implementamos el uso de `Variables CSS` definidas en el `:root`.

---
```
:root {
    --primario: #e67e22; 
    --oscuro: #2c3e50;   
    --error: #ef4444;    
}
```
Esto nos permite cambiar la identidad visual de la marca modificando únicamente estas líneas, sin tener que buscar y reemplazar códigos hexadecimales en cientos de líneas de código.

---
**CATÁLOGO (GRID)**

# Introducción:
Para la parte de `catalogo.php`, el reto fue el mostrar una colección dinámica de productos, aquí mi compañera y yo abandonamos `Flexbox` para utilizar `CSS Grid`, que es la herramienta más potente para diseños de filas y columnas, además, utilizamos formularios independientes `<form>` para cada producto, lo que permite enviar datos específicos (ID y cantidad) al carrito de compras.

**CSS**

---
```
.catalogo-grid { 
    display: grid; 
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 25px; 
}

.categorias-nav {
    position: sticky;
    top: 0px;
    z-index: 900;
}
```
---
**HTML**

---
```
<form action="carrito.php" method="POST">
    <div class="cantidad-control">
         <button type="button" onclick="this.nextElementSibling.stepDown()">-</button>
         <input type="number" name="cantidad" value="1" min="1" readonly>
         <button type="button" onclick="this.previousElementSibling.stepUp()">+</button>
    </div>
    <input type="hidden" name="id" value="<?php echo $row['id']; ?>">
    <button type="submit" name="add">Añadir al pedido</button>
</form>
```
---

**Explicación del CSS Grid**

`display: grid;` define el contenedor como una rejilla. 

`repeat(auto-fill, minmax(280px, 1fr))` esta es la línea clave para la responsividad, básicamente le dice al navegador que tiene que crear tantas columnas como quepan, siempre que midan al menos 280px y si sobra espacio, lo reparta (1fr) equitativamente.
Esto lo que hace es que la web se adapte a móviles y ordenadores sin necesidad de `media queries` complejas.

`position sticky` nos permite que el menú de categorías se desplace con la página pero se quede "pegado" al borde superior de la pantalla al hacer scroll, facilitando la navegación y teniendo siempre acceso a los filtros.

**Interactividad del HTML**

`<input type="number">` esto hace que haya un control semántico que impide al usuario escribir letras en la cantidad, mejorando la validación del navegador. 
`input type="hidden"` envía el ID del producto de forma silenciosa sin que el usuario lo vea.

# Conclusión:
El uso de CSS Grid nos permitió crear un diseño de tarjetas robusto y flexible, además nos dimos cuenta de que Grid es superior a Flexbox, mientras que Flexbox sigue siendo ideal para alinear elementos pequeños dentro de por ejemplo, centrar los textos o botones.

Un error al trabajar con formularios múltiples en una misma página es olvidar el atributo `name` en los inputs, al principio, nuestro archivo `carrito.php` no recibía nada porque, aunque el input existía visualmente, sin el atributo `name="id"` o `name="cantidad"`, asi que PHP no podía capturar el dato en el array `$_POST`.

---

**CARRITO Y FORMULARIOS (RESPONSIVE)**

# Introducción:
En la vista carrito.php y contacto.php, hemos trabajado con estructuras de datos tabulares y formularios de entrada de usuario, el mayor problema que nos encontramos aquí fue hacer que una `<table`>, que es rígida por naturaleza, se viera bien en un teléfono móvil, y para ello utilizamos CSS Media Queries

Para el carrito, utilizamos la superglobal `$_SESSION` de PHP como una "memoria temporal" que viaja con el usuario, esto nos permite mantener el estado de la compra (qué productos se han elegido) aunque el usuario cambie de página o recargue el navegador
**HTML**

---
```
<table class="tabla-bar-bara">
    <?php foreach ($_SESSION['carrito'] as $p): ?> <tr class="fila-producto">
        <td><?php echo htmlspecialchars($p['nombre']); ?></td> </tr>
    <?php endforeach; ?>
</table>
```
---
**CSS**

---
```
@media (max-width: 600px) {
    .tabla-bar-bara, tbody, tr, td { 
        display: block; 
        width: 100%; 
    }
    .total-card { flex-direction: column; }
}
```
---

**Explicación del HTML**

`<table>, <thead>, <tbody>` estas son etiquetas semánticas correctas para poder sacar la factura, si hubiesemos usado `divs` aquí habría sido un error semántico. 
`<label>` esta etiqueta en formularios es fundamental para la accesibilidad ya que vincula el texto visual con su `input`, permitiendo hacer clic en el texto para activar el campo.



**Explicación del CSS responsivo**

`@media (max-width: 600px)` detecta si el dispositivo es un móvil. 
`display: block;` rompe el comportamiento normal de la tabla, es decir, en lugar de celdas una al lado de otra las fuerza a ponerse una encima de otra en bloque, haciendo que la información sea legible en pantallas verticales.

# Conclusión:
Con este bloque finalizamos la interfaz de usuario asegurando tanto la accesibilidad visual como la seguridad de los datos, hemos aprendido que `Responsive Design` implica a veces romper la estructura semántica visual para adaptarse al dispositivo.

Un error muy común en esta parte es olvidar colocar `session_start()` en la primera línea del archivo PHP, si se olvida o se pone después de cualquier código HTML, el servidor no puede iniciar la "memoria" del usuario y el carrito aparecerá siempre vacío al recargar la página, arruinando la experiencia de compra.

---
**PANEL DE ADMINISTRACIÓN (BACK)**

# Introducción:
En el back desarrollamos el área de gestión en `back/index.php`, a diferencia del `Front/`, aquí el diseño prioriza la utilidad sobre la estética, en pocas palabras, no es tán "bonito" visualmente como lo es el front, el back es un panel de control unificado.

---
```
<meta http-equiv="refresh" content="30"> <div class="card" style="border-left: 10px solid var(--error);"> 
    <h2>MESA <?php echo $a['numero_mesa']; ?></h2>
    <p>Estado: SOLICITANDO CUENTA</p>
</div>
```
---
**Explicación del HTML**

Aquí implementamos un sistema de estado visual mediante CSS dinámico, por ejemplo, si el pedido tiene el estado de `pedir_cuenta = "SI"`, se muestra una tarjeta con borde rojo `(var(--error))`, si es una comanda pendiente, se mostraría en otro bloque, además utilizamos la etiquea `<meta http-equiv="refresh">` en el head para que la pantalla se actualice sola cada 30 segundos, permitiendo al personal recibir pedidos en tiempo real sin tener que refrescar manualmente la página.

# Conclusión:
En este bloque del código del /back aprendimos que la experiencia de usuario no es solo para el cliente final, sino también para el empleado.

En el /back no buscamos "vender" sino informar, por eso usamos colores como el rojo o el verde definidos en el CSS, todo para que visualmente sea de ayuda al camarero y entienda el estado de los pedidos de un solo vistazo, sin tener que leer textos pequeños.

Un error que cometimos fue olvidar el incluir el `input type="hidden"` con el ID del pedido dentro del formulario, al principio teníamos el botón visual de "Marcar como cobrado" pero al pulsarlo no ocurría nada en la base de datos, esto pasaba por que aunuqe enviábamos la orden de cobro el servidor no sabia a qué mesa tenía que aplicársela, así que tuvimos que añadir el ID `(value="<?php echo $a['id']; ?>")` para que la el servidor identificase la mesa que enviaba esa orden.