# TCP and UDP Connection Example

This project demonstrates how to establish and use both TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) connections in Python. It was created as an activity for a computer networks course.

## Features
- Establishes a TCP server and client connection for reliable communication.
- Sets up a UDP server and client connection for fast, connectionless communication.
- Offers sample messages between clients and servers.

## Requirements
- Python 3.x

You can install Python [here](https://www.python.org/downloads/), if it's not already installed.

## Usage
1. **Run the TCP Server:**
   ```bash
   python tcp_server.py
   ```

2. **Run the TCP Client:**
   ```bash
   python tcp_client.py
   ```

   You can send messages from the TCP client to the server and receive a response.

3. **Run the UDP Server:**
   ```bash
   python udp_server.py
   ```

4. **Run the UDP Client:**
   ```bash
   python udp_client.py
   ```

   Similarly, send messages using UDP and observe the communication.

## File Structure
- `server_tcp.py`: The TCP server implementation.
- `client_tcp.py`: The TCP client implementation.
- `server_udp.py`: The UDP server implementation.
- `client_udp.py`: The UDP client implementation.
