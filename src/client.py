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


def join_room(username, ip, port, code):
    """
    Joins an existing room upon logging in

    Args:
        username (string): the username selected by the user
        ip (string): the ip address of the server
        port (string): the server's port to connect to
        code (string): the join code of the existing room

    """


    #unfinished method

    print('Joining room with: ' + username + ', ' + ip + ', ' + port + ', ' + code)

    #need condition to check if the login went through
    return False

def create_room(username, ip, port):

    """
    Creates a new room upon logging in

    Args:
       username (string): the username selected by the user
       ip (string): the ip address of the server
       port (string): the server's port to connect to

    """
    print('Creating room with ' + username + ', ' + ip + ', ' + port)

    #need condition to check if the login went through
    return False

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
    window_width = 1080
    window_length = 720
    window = pygame.display.set_mode((window_width, window_length))
    
    
    #uniform font for the login screen
    login_font = pygame.font.Font(None, 32)
    
    #textboxes for login information
    username_box = dubercomponent.DuberTextBox(450, 400, 300, 25, (255,255,255), '', login_font, (200, 200, 200))
    ip_box = dubercomponent.DuberTextBox(450,430, 300, 25, (255,255,255), '', login_font, (200,200,200))
    port_box = dubercomponent.DuberTextBox(450,460, 300, 25, (255,255,255), '', login_font, (200,200,200))
    join_code_box = dubercomponent.DuberTextBox(175, 550, 300, 25, (255,255,255), '', login_font, (200,200,200))
    create_room_button = dubercomponent.DuberTextBox(650, 550, 150, 25, (255,255,255), 'Create Room', login_font, (200,200,200))
    join_button = dubercomponent.DuberTextBox(275, 610, 55, 25, (255,255,255), 'Join', login_font, (200,200,200))
    #boolean to operate main program
    run = True
    login_screen = True
    editing_username = False
    editing_ip = False
    editing_port = False
    editing_join_code = False

    while run:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #only detects user input for these objects if they are in the login screen
            if login_screen:

                #detects if a user clicked on a text box to enter information
                if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                    if username_box.selected(pygame.mouse.get_pos()):
                        editing_username = True
                        editing_ip = False
                        editing_port = False
                        editing_join_code = False
                    elif ip_box.selected(pygame.mouse.get_pos()):
                        editing_username = False
                        editing_ip = True
                        editing_port = False
                        editing_join_code = False
                    elif port_box.selected(pygame.mouse.get_pos()):
                        editing_username = False
                        editing_ip = False
                        editing_port = True
                        editing_join_code = False
                    elif join_code_box.selected(pygame.mouse.get_pos()):
                        editing_username = False
                        editing_ip = False
                        editing_port = False
                        editing_join_code = True
                    elif join_button.selected(pygame.mouse.get_pos()):
                        login_screen = join_room(username_box.get_text(), ip_box.get_text(), port_box.get_text(), join_code_box.get_text())
                    elif create_room_button.selected(pygame.mouse.get_pos()):
                        login_screen = create_room(username_box.get_text(), ip_box.get_text(), port_box.get_text())

                #lets the user remove information for logging in
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if editing_username:
                            username_box.set_text(username_box.get_text()[0:-1])
                        elif editing_ip:
                            ip_box.set_text(ip_box.get_text()[0:-1])
                        elif editing_port:
                            port_box.set_text(port_box.get_text()[0:-1])
                        elif editing_join_code:
                            join_code_box.set_text(join_code_box.get_text()[0:-1])


                    #lets the user enter in information for logging in
                    else:
                        if editing_username and len(username_box.get_text()) < 10:
                            username_box.set_text(username_box.get_text() + event.unicode)
                        elif editing_ip and len(ip_box.get_text()) < 15:
                            ip_box.set_text(ip_box.get_text() + event.unicode)
                        elif editing_port and len(port_box.get_text()) < 4:
                            port_box.set_text(port_box.get_text() + event.unicode)
                        elif editing_join_code and len(join_code_box.get_text()) < 6:
                            join_code_box.set_text(join_code_box.get_text() + event.unicode)

            #user interactions for the main program after loggin in (UNFINISHED)        
            else:
                #there are supposed to be inputs here for the main screen but we haven't gotten to that part yet
                window.fill((0,0,0))

        
        #draws components of the login screen
        if login_screen:
            window.fill((0,0,0))
            window.blit(logo, (330, 30))
            window.blit(login_font.render('Username:', True, (255,255,255)), (300, 400))
            window.blit(login_font.render('IP Address:', True, (255,255,255)), (300, 430))
            window.blit(login_font.render('Port:', True, (255,255,255)), (300, 460))
            window.blit(login_font.render('Join Code:', True, (255,255,255)), (25, 550))
            window.blit(login_font.render('Or', True, (255,255,255)), (530,550))
            username_box.draw(window)
            ip_box.draw(window)
            port_box.draw(window)
            join_code_box.draw(window)
            create_room_button.draw(window)
            join_button.draw(window)
        else:
            #other stuff for the main window to be added here
            window.blit(pygame.transform.scale(logo, (105,73)), (0,0))

        #update entire screen
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