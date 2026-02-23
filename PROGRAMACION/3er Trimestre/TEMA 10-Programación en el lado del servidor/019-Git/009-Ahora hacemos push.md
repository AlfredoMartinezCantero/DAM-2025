git push origin main

/var/www/html/pruebadamgit2026$ git push origin main
Username for 'https://github.com': AlfredoMartinezCantero
Password for 'https://AlfredoMartinezCantero@github.com': 
remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Autenticación falló para 'https://github.com/AlfredoMartinezCantero/pruebadamgit2026/'

Vamos a crear un token de autenticacion

Primero creamos el token:

https://github.com/settings/tokens
creamos token clásico
Seleccionamos todos los permisos

Os dará un token que empezará por ghp_XXXXXXXXXXXXXXXXXX

Ahora lo introducimos en la terminal:
git config --global credential.helper store