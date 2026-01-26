# En el shell (terminal):
# echo 'export CONTRASENA_CEAC="Ceac123$"' >> ~/.bashrc
# source ~/.bashrc
import os

print(os.environ.get("CONTRASENA_CEAC"))
