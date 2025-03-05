import socket
import json

class UDPClient:
    def __init__(self, address_ip, port):
        self.address_ip = address_ip
        self.port = port

    def main(self):
        try:
            user_input = input("Digite seu nome: ")

            receive_data = self.send_message(user_input)

            json_data = json.loads(receive_data)

            print("\nFROM SERVER: " + json_data['message'])

            double = self.double_number(json_data['number'])

            print("\nO dobro é " + str(double))

            receive_data = self.send_message(str(double))

            print("\n" + receive_data)

        except Exception as e:
            print(f"Error: {e}")

    def send_message(self, message: str) -> str:

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        server_address = (self.address_ip, self.port)

        client_socket.sendto(message.encode('utf-8'), server_address)

        receive_data, _ = client_socket.recvfrom(1024)

        client_socket.close()

        return receive_data.decode('utf-8')


    def double_number(self, num: int) -> int:
        return num * 2

if __name__ == "__main__":
    udp_client = UDPClient('localhost', 1212)
    udp_client.main()
