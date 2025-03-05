import socket
import random

class UDPServer:
    def __init__(self, address_ip, port):
        self.address_ip = address_ip
        self.port = port

    def main(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind((self.address_ip, self.port))

        print("Servidor ligado")

        while True:
            receive_data, client_address = server_socket.recvfrom(1024)

            sentence = receive_data.decode('utf-8')

            number = self.get_number()

            message = f"Olá, {sentence}. Me der o dobro de {number}"

            print(f"\nO cliente {sentence} se conectou ao servidor e o número sorteado foi {number}")

            message_json = f'{{"message": "{message}", "number": {number}}}'

            server_socket.sendto(message_json.encode('utf-8'), client_address)

            while True:
                receive_data, client_address = server_socket.recvfrom(1024)

                sentence_new = receive_data.decode('utf-8')

                response = None

                if int(sentence_new) == number*2:
                    response = f"Você acertou. O dobro de {number} é {sentence_new}"
                else:
                   response = f"Você errou. O dobro de {number} é {number*2} e não {sentence_new}"

                send_data_response = response.encode('utf-8')

                print(response)

                server_socket.sendto(send_data_response, client_address)

                break

    def get_number(self) -> int:
        return int(random.randint(1, 10))

if __name__ == "__main__":
    udp_server = UDPServer('localhost', 1212)
    udp_server.main()
