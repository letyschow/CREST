import socket

# create the socket object
sock = socket.socket()
# identify port
port = 1056
# bind to port
sock.bind(('', port))
# listen very very carefully
sock.listen(1)
print("i'm listening...")
# create a loop to accept connections
while True :
    # make a connection with client
    conn, addr = sock.accept()
    print("received a connection from ", addr)

    #say something back
    conn.send("hello there".encode())

    #obv closes the connection
    conn.close()