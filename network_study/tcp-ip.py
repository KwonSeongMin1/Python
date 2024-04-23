import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(('',12345))

server_socket.listen()

while True:
    client_socket, addr=server_socket.accept()
    print('Connected by',addr)
    while True:
        data=client_socket.recv(1024)
        if not data:
            break
        print('Received from',addr,data.decode())
        client_socket.sendall(data)
    client_socket.close()