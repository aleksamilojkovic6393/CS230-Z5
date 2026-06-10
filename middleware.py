import socket

HOST = '127.0.0.1'
PORT = 5000

def timeout_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except socket.timeout:
            return "Vreme cekanja isteklo."
    return wrapper

@timeout_decorator
def prosledi_zahtev(zahtev):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.settimeout(2)

    client.connect((HOST, PORT))

    client.send(zahtev.encode())

    odgovor = client.recv(1024).decode()

    client.close()

    return odgovor