# En el shell (terminal):
# echo 'export NOMBRE="Alfredo"' >> ~/.bashrc
# source ~/.bashrc
import os

print(os.environ.get("NOMBRE"))
