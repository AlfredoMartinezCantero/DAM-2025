En el cron, añado esta linea:

Terminal:
crontab -e

Añadimos esto en la última linea

* * * * * /usr/bin/python3 /var/www/html/"home/alfredo/Documentos/GitHub/DAM-2025/BASES DE DATOS/2º Trimestre/TEMA 8-Proyectos/006-Repaso mysql dump/"

Y luego:
Control + O = Guardar
Control + X = Salir