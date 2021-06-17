import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))

s.listen(5)
testClient = None

def run():
    while True:
        clientSocket, address = s.accept()
        print(f"connection from {address} has been established! ")

        msg = "Welcome to the server!"
        msg = f"{len(msg):<{HEADERSIZE}}" + msg

        clientSocket.send(bytes(msg, "utf-8"))
        testClient = clientSocket