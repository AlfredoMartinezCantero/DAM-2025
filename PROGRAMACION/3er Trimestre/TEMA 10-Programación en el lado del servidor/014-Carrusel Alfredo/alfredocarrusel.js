let contenedor = document.querySelector(".alfredocarrusel");
        let contenido = document.querySelectorAll(".alfredocarrusel img")

        contenido.forEach(function(elemento){
            elemento.remove()
        })

        let nuevo_contenedor = document.createElement("section")
        contenedor.appendChild(nuevo_contenedor)

        contenido.forEach(function(elemento){
            nuevo_contenedor.appendChild(elemento)
        })

        let botonatras = document.createElement("button")
        botonatras.textContent = "◀"
        contenedor.appendChild(botonatras)
        
        let botondelante = document.createElement("button")
        botondelante.textContent = "▶"
        contenedor.appendChild(botondelante)

        var anchura = 1280;
        var contador = 0;

        // Botón Derecha (Avanzar)
        botondelante.onclick = function() {
            contador--; 
            if (contador < -7) { 
                contador = 0; // Vuelve al inicio si se pasa del final
            }
            nuevo_contenedor.style.left = (contador * anchura) + "px";
        }

        // Botón Izquierda (Retroceder)
        botonatras.onclick = function() {
            contador++; 
            if (contador > 0) { 
                contador = -7; // Va al final si intenta retroceder desde el inicio
            }
            nuevo_contenedor.style.left = (contador * anchura) + "px";
        }