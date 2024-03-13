

import socket
HOST_IP="127.0.0.1"
HOST_PORT=32000
MAX_DATA_SIZE=1024


s=socket.socket()
s.setsocket(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)


s.bind((HOST_IP, HOST_PORT))
s.listen()


print("Attente de connexion sur {HOST_IP}, port {HOST_PORT}...")
connection_socket, client_address = s.accept()
print(f"Connexion établie avec {client_address}")

texte_envoye= "Bonjour"
connection_socket.sendall(texte_envoye.encode())

data_recues= s.recv(MAX_DATA_SIZE)
print(data_recues.decode())



s.close()
connection_socket.close()