#! /usr/bin/python3

# This will be our simple TCP server

import socket

'SERVER_IP = "127.0.0.1"

SERVER_PORT = 8080

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((SERVER_IP, SERVER_PORT))

server.listen(5)

print("[*] Server Listening on%s:%d" % (SERVER_IP, SERVER_PORT)

client,addr = server.accept()

print("[*] Accepted connection from: %s:%d % (addr[0], addr[1]))
