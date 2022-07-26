import socket

while True :
    host = input()

    socket.setdefaulttimeout(10)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((host,443))
        print("connected :)")
        sock.close()
    except Exception as ex:
        print(ex)