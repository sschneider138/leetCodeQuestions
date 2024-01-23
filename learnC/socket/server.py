import socket
import sys
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())

print(SERVER)