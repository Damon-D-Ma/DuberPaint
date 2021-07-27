from threading import Thread
import pygame
import socket
import brushes

def server_interaction (ip, port):
    """
    Interacts with the server (listens and sends)

    Args:
        ip (string): The IP to connect to
        port (int): The port to connect to on that specific IP
    """
    sock = socket.create_connection((ip, port))
    while 1:
        data = input("send something: ")
        sock.send(data.encode())

def main():
    """
    The main function
    """
    ip = input("enter ip: ")
    port = int(input("enter port: "))
    thread = Thread(target=server_interaction, args=(ip, port))
    thread.start()

if __name__ == "__main__":
    main()