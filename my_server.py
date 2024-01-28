import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5555))
    server_socket.listen(1)
    print("Server listening on port 5555")

    while True:
        connection, address = server_socket.accept()
        data = connection.recv(1024)
        connection.sendall(data)
        connection.close()

if __name__ == "__main__":
    start_server()
