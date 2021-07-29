from threading import Thread
import pygame
import socket
import brushes
import dubercomponent

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


    #screen size subject to change
    window = pygame.display.set_mode((1080, 720))
    
    
    #uniform font for the login screen
    login_font = pygame.font.Font(None, 32)
    
    #textboxes for login information
    username_box = DuberTextBox(450, 400, 300, 25, (255,255,255), '', login_font, (200, 200, 200))
    ip_box = ''
    port_box = ''
    join_code_box = ''


    #boolean to operate main program
    run = True
    login_screen = True
    editing_username = False
    editing_ip = False
    editing_port = False

    while run:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if login_screen:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if editing_username:
                            username = username[0:-1]
                        elif editing_ip:
                            ip = ip[0:-1]
                        elif editing_port:
                            port = port[0:-1]

                    else:
                        #username can't be more than 10 characters
                        if editing_username and len(username) <= 10:
                            username += event.unicode
                        elif editing_ip and len(ip) <= 15:
                            ip += event.unicode
                        elif editing_port and len(port) <= 4:
                            port += event.unicode
                        
            else:
                #there are supposed to be inputs here for the main screen but we haven't gotten to that part yet
                window.fill((0,0,0))

        if login_screen:
            window.fill((0,0,0))
            window.blit(logo, (330, 30))
            window.blit(login_font.render('Username:', True, (255,255,255)), (300, 400))
            window.blit(login_font.render('IP Address:', True, (255,255,255)), (300, 430))
            window.blit(login_font.render('Port:', True, (255,255,255)), (300, 460))
            textbox = login_font.render(username, True, (200,200,200))
            window.blit(textbox, (450, 400))
        else:
            #other stuff for the main window to be added here
            window.fill((0,0,0))
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