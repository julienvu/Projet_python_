

import socket
import time
HOST_IP="127.0.0.1"
HOST_PORT=32000
MAX_DATA_SIZE=1024
s=socket.socket()



print("Attente de connexion sur {HOST_IP}, port {HOST_PORT}...")
while True:
    try:
        s.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError:
        print("Error: Impossible de se connecter su serveur")
        time.sleep(4)
    else:
        print("Connecté au serveur")
        break
# .....

   
s.close()

