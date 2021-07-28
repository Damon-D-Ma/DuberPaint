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

    #Initialize pygame
    pygame.init()

    window = pygame.display.set_mode((1080, 720))

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
    
   
    
    """
    text-based login code to be scrapped later

    ip = input("enter ip: ")
    port = int(input("enter port: "))
    thread = Thread(target=server_interaction, args=(ip, port))
    thread.start()
    """
if __name__ == "__main__":
    main()