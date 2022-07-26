import socket

#create socket
sock = socket.socket()

sock.connect(('127.0.0.1', 1056))
print("established connection")

print (sock.recv(1024).decode())
sock.close() 