sudo apt install nginx

pip3 install gunicorn --break-system-packages

Navegamos hasta la carpeta:
gunicorn --bind 127.0.0.1:8000 app:app