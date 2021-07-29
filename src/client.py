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
    pygame.display.set_caption("Duber Paint")
    logo = pygame.image.load("./assets/duberpaint.png")
    pygame.display.set_icon(logo)

    window = pygame.display.set_mode((1080, 720))
    login_font = pygame.font.Font(None, 32)
    username_text = ''
    join_code_text = ''

    run = True

    while run:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    username_text = username_text[0:-1]
                else:
                    username_text += event.unicode

        #Booleans for multiple text boxes to choose which one to edit?
        #needs a join/connect button and a create button
        window.fill((0,0,0))
        textbox = login_font.render(username_text, True, (255,255,255))
        window.blit(textbox, (0,0))
        pygame.display.flip()
    
    """
    text-based login code to be scrapped later

    ip = input("enter ip: ")
    port = int(input("enter port: "))
    thread = Thread(target=server_interaction, args=(ip, port))
    thread.start()
    """
if __name__ == "__main__":
    main()