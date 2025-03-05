import socket

class TCPClient:
    def __init__(self, address_ip, port):
        self.address_ip = address_ip
        self.port = port

    def main(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            user_input_sentence = input("Digite seu nome: ")

            client_socket.connect((self.address_ip, self.port))

            client_socket.sendall(user_input_sentence.encode('utf-8'))

            modified_sentence = client_socket.recv(1024).decode('utf-8').strip()

            print(f"o servidor TCP respondeu com: {modified_sentence}")

        except ConnectionRefusedError:
            print("Erro: Não foi possível conectar ao servidor. Verifique se ele está ativo.")

        except socket.error as e:
            print(f"Erro no socket: {e}")

        finally:
            if 'client_socket' in locals():
                client_socket.close()
                print("Socket fechado.")

if __name__ == "__main__":
    client_tcp = TCPClient('localhost', 6789)
    client_tcp.main()