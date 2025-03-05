import socket

class TCPServer:
    def __init__(self, address_ip, port):
        self.address_ip = address_ip
        self.port = port

    def main(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.address_ip, self.port))
        server_socket.listen(1)

        while True:
            connection_socket, client_address = server_socket.accept()

            client_sentence = connection_socket.recv(1024).decode('utf-8').strip()

            print(f"Recebido: {client_sentence}")

            sending = "Seja bem vindo ao servidor TCP, " + client_sentence

            print(f"Enviado: {sending}\n")

            connection_socket.sendall(sending.encode('utf-8'))

            connection_socket.close()

            print(f"Conexão encerrada com {client_sentence}")

if __name__ == "__main__":
    server_tcp = TCPServer('localhost', 6789)
    server_tcp.main()