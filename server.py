import socket
import time

HOST = '127.0.0.1'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server je pokrenut")

while True:
    conn, addr = server.accept()

    zahtev = conn.recv(1024).decode()

    time.sleep(1)

    conn.send(f"Odgovor servera: {zahtev}".encode())

    conn.close()