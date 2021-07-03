import pygame
import socket

def main():
    """
    The main function
    """
    ip = input("enter ip")
    port = int(input("enter port: "))
    socket.create_connection((ip, port))

if __name__ == "__main__":
    main()