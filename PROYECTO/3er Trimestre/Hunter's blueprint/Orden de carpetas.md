wilds-build-planner/
├── back/                       # Lógica de servidor y procesamiento
│   ├── python/                 # Scripts de Python (IA y API)
│   │   ├── api_fetcher.py      # Script para consumir la API de Monster Hunter
│   │   ├── ai_assistant.py     # Integración con Ollama (RAG)
│   │   └── requirements.txt    # Librerías necesarias (requests, ollama, mysql-connector)
│   └── php/                    # Procesamiento de formularios y sesiones
│       ├── auth_login.php      # Gestión de acceso de usuarios
│       ├── save_build.php      # Guardado de configuraciones en DB
│       └── admin_actions.php   # Lógica específica del panel CRUD
├── database/                   # Archivos relacionados con la persistencia
│   ├── schema.sql              # Estructura de tablas (Usuarios, Builds, Piezas)
│   └── seeds.sql               # Datos iniciales de prueba
├── front/                      # Todo lo que el usuario ve
│   ├── css/                    # Hojas de estilo (estilo.css)
│   ├── js/                     # Lógica de interfaz (interactividad de la build)
│   │   └── build-engine.js     # Calculador de stats en tiempo real
│   ├── img/                    # Activos visuales e iconos
│   └── index.php               # Página principal (Landing + Planner)
├── inc/                        # Componentes reutilizables (Estilo Alfredo)
│   ├── cabecera.php            # Header y navegación
│   ├── pie.php                 # Footer y scripts
│   ├── funciones.php           # Helpers comunes
│   └── db_connection.php       # Conexión PDO a MySQL/MariaDB
├── admin/                      # Panel de administración (Acceso restringido)
│   ├── dashboard.php           # Vista general
│   ├── gestionar_usuarios.php  # CRUD de usuarios
│   └── moderar_builds.php      # CRUD de builds públicas
└── .env                        # Variables de entorno (claves API, credenciales DB)