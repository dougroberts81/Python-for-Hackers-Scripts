#! /usr/bin/python3

import socket

tcp_ip="192.168.0.10"

tcp_port=44

buffer_size=100

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.bind((tcp_ip,tcp_port))

s.listen(1)

conn,addr= s.accept()
print('Connection address: ' ,addr)

while 1:

	data=conn.recv(buffer_size)
	if not data:break
	print('Received data: ' ,data)
	conn.send(data)

conn.close
