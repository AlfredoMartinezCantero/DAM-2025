# Proyecto Intermodular: Bar Bara

**1. Introducción y Concepto**
Para este Proyecto Intermodular, mi compañera y yo elegimos desarrollar **Bar Bara**, una plataforma de gestión para hostelería que conecta a los clientes con la cocina y la barra en tiempo real.

Elegimos el sector de la hostelería porque identificamos una necesidad, la necesidad de la gente de ser atendida rápido y la capacidad del personal de responder así, Bar Bara no es una web como tal, es una herramienta que aporta una ayuda de trabajo, digitaliza la comanda y ofrece control total sobre la facturación.

---
**2. Detalles del Proyecto y Ejecución**
Este proyecto ha sido desarrollado en colaboración con mi compañera, Ana. 
Hemos operado como un equipo de desarrollo conjunto, no fue como un: Ana tu haces el back y yo el front, los dos íbamos haciendo poco a poco todo en general, igual en la parte del front mientras Ana hacia la parte del login yo estaba haciendo el carrito.

Básicamente hicimos un trabajo conjunto total, ambos colaboramos en la integración del Frontend con el Backend, asegurando que la experiencia fuera fluida.

Usamos PHP y decidimos implementar una arquitectura MVC propia sin frameworks pesados, demostrando todo lo que hemos ido aprendiendo durante estos dos primeros trimestres sobre el lenguaje, el cual nos permite un control total sobre el código.

Usamos MySQL y PDO para la persistencia de datos, optamos por una base de datos relacional robusta y utilizamos PDO para la conexión, lo que protege nuestra aplicación contra inyecciones SQL y garantiza la seguridad de los datos del usuario.

CSS3, en lugar de depender de librerías, diseñamos un sistema de estilos propio utilizando variables CSS, esto nos permitió establecer un sistema de diseño de colores, espaciados y altamente personalizable.

---
**3. Funcionalidad**
La aplicación se divide en dos entornos: el Entorno Cliente (Front) y el Entorno Gestión (Back).

Experiencia del Cliente, landing page e identidad, es decir, el index.php, aqui diseñamos un "Hero Section" muy visual que dirige al usuario a tres acciones claras, Ver Carta, Carrito o Contacto.

Catálogo, aquí resolvimos el problema de la navegación en menús extensos implementando una barra de navegación "sticky" por categorías que permite al usuario saltar entre "Tapas", "Cócteles" o "Postres" sin perderse. 
Los productos se cargan dinámicamente desde la base de datos, mostrando imágenes, descripciones y precios actualizados en tiempo real.

Carrito y Gestión de Sesiones, aqui el sistema permite modificar cantidades, recalcular subtotales y conseguimos mantener la persistencia de la información mediante variables de sesión `($_SESSION)`, todo esto asegura que si el cliente cierra el navegador por error, su pedido no se pierde.

Historial y Pedir la Cuenta, en este apartado, el cliente puede ver en tiempo real lo que su mesa ha consumido (sumando rondas anteriores) y solicitar la cuenta digitalmente, esto elimina la ansiedad de esperar al camarero para pedir la nota, enviando una alerta directa al panel de control.

Comandas a Cocina, aquí lo que hicimos fue hacer que los nuevos pedidos entren automáticamente en una lista de pendientes, y, con un solo clic, cocina marca el plato como "Entregado" y desaparece de la lista, limpiando el flujo de trabajo.

---
**4. Cierre y Conclusiones**
Bar Bara demuestra que somos capaces de construir una solución Full-Stack completa, desde la base de datos hasta la interfaz de usuario.
En resumen, creo que mi compañera y yo hemos conseguido crear una aplicación robusta, un backend seguro y bien estructurado, usabilidad, una interfaz pensada para móviles.

Para finalizar me gustaría añadir que este proyecto consolida nuestros conocimientos en desarrollo web, demostrando que no solo sabemos "picar código", sino crear productos digitales que resuelven problemas reales.