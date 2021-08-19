from threading import Thread
import pygame
import socket
import brushes as brushes
import dubercomponent

#-------------------------------GLOBALS-------------------------------#
sock = None  # socket

user_id = None
join_code = None
username = None
ip = None
port = None

owner = False

logo = None
window_width = None
window_length = None
window = None


login_font = None

username_box = None
ip_box = None
port_box = None
join_code_box = None
create_room_button = None
join_button = None

board_elements = []
user_list = []

main_font = None

colour_selection_area = None
brush_selection_area = None
shape_selection_area = None
leave_button = None

brush_list = [] #need some preset brushes here
colour_list = [] #need some preset colours here


def send(message):
    """
    sends a message to the server

    Args:
        message (string): the message to be sent to the server
    """
    global sock
    sock.send(message.encode())
    # incomplete function


def send_brush_mark(mark):
    """
    Sends a point drawn from the brush to the server

    Args:
        mark (BrushMark): the mark that the user drew on the canvas
    """
    message = f'<d>\n{join_code}\n{mark.get_coordinates()}\n{mark.get_width()}\n{mark.get_colour()}'
    send(message)


def send_rect(rect):
    """
    Sends a rectangle drawn by the user to the server

    Args:
        rect (Rectangle): the rectangle to be sent to the server
    """
    message = f'<r>\n{join_code}\n{rect.get_top_left()}\n{rect.get_bottom_right()}\n{rect.get_colour()}\n{rect.get_filled()}'
    send(message)


def send_ellipse(ellipse):
    """
    Sends an ellipse drawn by the user to the server

    Args:
        ellipse (Ellipse): the ellipse to be sent to the server
    """
    message = f'<e>\n{join_code}\n{ellipse.get_top_left()}\n{ellipse.get_bottom_right()}\n{ellipse.get_colour()}\n{ellipse.get_filles()}'
    send(message)


def send_line(line):
    """
    sends a line drawn by the user to the server

    Args:
        line (Line): the line to be sent to the server
    """
    message = f'<L>\n{join_code}\n{line.get_top_left}\n{line.get_bottom_right()}\n{line.get_colour()}'
    send(message)


def disconnect():
    message = f'<dc>\n{user_id}'
    send(message)


def kick_user(target_id):
    """
    Kicks a selected user if the current user is the owner of the room

    Args:
        target_id (string): the user id of the user to be kicked
    """

    if owner:
        message = f'<k>\n{target_id}'
        send(message)

def recv_draw(data):
    """
    Handles receiving a draw mark

    Args:
        data (list): the data sent over by the server
    """
    if len(data) == 4:
        #TODO: do stuff with the data
        coords = (int(data[1].split(" ")[0]), int(data[1].split(" ")[1]))
        width = int(data[2])
        colour = (int(data[3].split(" ")[0]), int(data[3].split(" ")[1]), int(data[3].split(" ")[2]))

def recv_rectangle(data):
    """
    Handles receiving a rectangle

    Args:
        data (list): the data sent over by the server
    """
    if len(data) == 5:
        top_left = (int(data[1].split(" ")[0]), int(data[1].split(" ")[1]))
        bottom_right = (int(data[2].split(" ")[0]), int(data[2].split(" ")[1]))
        colour = (int(data[3].split(" ")[0]), int(data[3].split(" ")[1]), int(data[3].split(" ")[2]))
        fill = (int(data[4].split(" ")[0]), int(data[4].split(" ")[1]), int(data[4].split(" ")[2]))
        #TODO: do stuff with the data

def recv_ellipse(data):
    """
    Handles receiving an ellipse

    Args:
        data (list): the data sent over by the server
    """
    if len(data) == 5:
        top_left = (int(data[1].split(" ")[0]), int(data[1].split(" ")[1]))
        bottom_right = (int(data[2].split(" ")[0]), int(data[2].split(" ")[1]))
        colour = (int(data[3].split(" ")[0]), int(data[3].split(" ")[1]), int(data[3].split(" ")[2]))
        fill = (int(data[4].split(" ")[0]), int(data[4].split(" ")[1]), int(data[4].split(" ")[2]))
        #TODO: do stuff with the data

def recv_line(data):
    """
    Handles receiving a line

    Args:
        data (list): the data sent over by the server
    """
    if len(data) == 5:
        top_left = (int(data[1].split(" ")[0]), int(data[1].split(" ")[1]))
        bottom_right = (int(data[2].split(" ")[0]), int(data[2].split(" ")[1]))
        colour = (int(data[3].split(" ")[0]), int(data[3].split(" ")[1]), int(data[3].split(" ")[2]))
        #TODO: do stuff with the data

def recv_disconnect(data):
    """
    Handles a user disconnecting

    Args:
        data (list): the data being sent over by the server
    """
    if len(data) == 2:
        user_id_of_user_to_remove = int(data[1])
        #TODO: remove the user

def recv_user_join(data):
    """
    Handles a user joining

    Args:
        data (list): stuff sent over from the server
    """
    if len(data) == 3:
        new_user_id = int(data[1])
        new_username = data[2]
        #TODO: uh do stuff with this data

command_map = {
    "<d>": recv_draw,
    "<r>": recv_rectangle,
    "<e>": recv_ellipse,
    "<L>": recv_line,
    "<dc>": recv_disconnect,
    "<uj>": recv_user_join
}

def server_listener():
    """
    Listens to the server then calls a function to respond based on what the server sends
    """
    global sock
    running = True
    while running:
        data = sock.recv(4096).decode("utf-8")
        print(data)
        command = data.splitlines()[0]
        command[command](data.splitlines())


def join_room():
    """
    Joins an existing room upon logging in

    """
    global sock
    sock = socket.create_connection((ip, port))
    send(f"<j>\n{username}\n{join_code}")
    # unfinished method

    print(f"Joining room with: {username}, {ip}, {port}, {join_code}")
    Thread(target=server_listener).start()

    # need condition to check if the login went through
    response = sock.recv(4096).decode("utf-8")
    if response == "<X>":
        return False
    elif len(response.splitlines()) == 2:
        user_id = int(response.splitlines[1])
        return True
    else:
        return False


def create_room():
    """
    Creates a new room upon logging in

    Args:
       username (string): the username selected by the user
       ip (string): the ip address of the server
       port (string): the server's port to connect to

    """
    global sock
    global owner
    sock = socket.create_connection((ip, port))
    send(f"<c>\n{username}")
    print(f"Creating room with {username}, {ip}, {port}")

    owner = True
    Thread(target=server_listener).start()

    # need condition to check if the login went through
    response = sock.recv(4096).decode("utf-8")
    if response == "<X>":
        return False
    elif len(response.splitlines()) == 3:
        user_id = int(response.splitlines()[1])
        join_code = response.splitlines()[2]


def main():
    """
    The main function
    """
    # Initialize pygame

    global logo
    global window_width
    global window_length
    global window

    global user_id
    global join_code
    global username
    global ip
    global port

    global login_font
    global main_font
    global username_box
    global ip_box
    global port_box
    global join_code_box
    global create_room_button
    global join_button

    global board_elements
    global user_list

    global colour_selection_area
    global brush_selection_area
    global shape_selection_area
    global leave_button

    global brush_list
    global colour_list

    pygame.init()
    pygame.display.set_caption("Duber Paint")
    logo = pygame.image.load("./assets/duberpaint.png")
    pygame.display.set_icon(logo)

    # screen size subject to change
    window_width = 1080
    window_length = 720
    window = pygame.display.set_mode((window_width, window_length))

    # uniform fonts the program
    login_font = pygame.font.Font(None, 32)
    main_font = pygame.font.Font(None,32)



    # textboxes for login information
    username_box = dubercomponent.DuberTextBox(
        450, 400, 300, 25, (255, 255, 255), '', login_font, (200, 200, 200))
    ip_box = dubercomponent.DuberTextBox(
        450, 430, 300, 25, (255, 255, 255), '', login_font, (200, 200, 200))
    port_box = dubercomponent.DuberTextBox(
        450, 460, 300, 25, (255, 255, 255), '', login_font, (200, 200, 200))
    join_code_box = dubercomponent.DuberTextBox(
        175, 550, 300, 25, (255, 255, 255), '', login_font, (200, 200, 200))
    create_room_button = dubercomponent.DuberTextBox(
        650, 550, 150, 25, (255, 255, 255), 'Create Room', login_font, (200, 200, 200))
    join_button = dubercomponent.DuberTextBox(
        275, 610, 55, 25, (255, 255, 255), 'Join', login_font, (200, 200, 200))
    

    #elements for main window
    colour_selection_area = dubercomponent.DuberTextBox(240, 10, 300, 95, (128,128,128), "Colours here", main_font, (255,255,255))
    brush_selection_area = dubercomponent.DuberTextBox(560, 10, 150, 95, (128,128,128), "Brushes here", main_font, (255,255,255))
    shape_selection_area = dubercomponent.DuberTextBox(730, 10, 200, 95, (128,128,128), "Shapes here", main_font, (255,255,255))
        
    #leave/disconnect button
    leave_button = dubercomponent.DuberTextBox(20, 670, 160, 40, (255,0,0), "LEAVE", main_font, (255,0,0))


    # booleans to operate program
    run = True
    login_screen = True
    editing_username = False
    editing_ip = False
    editing_port = False
    editing_join_code = False

    using_brush = False
    drawing_rectangle = False
    drawing_ellipse = False
    drawing_line = False



    #Other values needed for the program
    current_brush = None #may need a default brush here



<<<<<<< Updated upstream

=======
    #row 1
    colour_list.append(dubercomponent.DuberColourButton(250,18, (255,0,0)))
    colour_list.append(dubercomponent.DuberColourButton(280,18, (255,165,0)))
    colour_list.append(dubercomponent.DuberColourButton(310,18, (255,255,0)))
    colour_list.append(dubercomponent.DuberColourButton(340,18, (0,128,0)))
    colour_list.append(dubercomponent.DuberColourButton(370,18, (0,0,255)))

    #row 2
    colour_list.append(dubercomponent.DuberColourButton(250,48, (128,0,128)))
    colour_list.append(dubercomponent.DuberColourButton(280,48, (0,0,0)))
    colour_list.append(dubercomponent.DuberColourButton(310,48, (255,255,255)))
    colour_list.append(dubercomponent.DuberColourButton(340,48, (139,69,19)))
    colour_list.append(dubercomponent.DuberColourButton(370,48, (128,128,128)))

    #row 3
    colour_list.append(dubercomponent.DuberColourButton(250,78, (255,255,255)))
    colour_list.append(dubercomponent.DuberColourButton(280,78, (255,255,255)))
    colour_list.append(dubercomponent.DuberColourButton(310,78, (255,255,255)))
    colour_list.append(dubercomponent.DuberColourButton(340,78, (255,255,255)))
    colour_list.append(dubercomponent.DuberColourButton(370,78, (255,255,255)))


    #adding buttons to the list of brush buttons

    #row 1
    brush_list.append(dubercomponent.DuberBrushButton(430,20, pygame.transform.scale(brush_icon, (32,32)), brushes.Brush((0,0,0), 10, 10) ))
    brush_list.append(dubercomponent.DuberBrushButton(472,20, pygame.transform.scale(brush_icon, (32,32)), brushes.Brush((0,0,0), 10, 10) ))
    brush_list.append(dubercomponent.DuberBrushButton(514,20, pygame.transform.scale(brush_icon, (32,32)), brushes.Brush((0,0,0), 10, 10) ))
    
    #row 2
    brush_list.append(dubercomponent.DuberBrushButton(430,62, pygame.transform.scale(brush_icon, (32,32)), brushes.Brush((0,0,0), 10, 10) ))
    brush_list.append(dubercomponent.DuberBrushButton(472,62, pygame.transform.scale(brush_icon, (32,32)), brushes.Brush((0,0,0), 10, 10) ))
    brush_list.append(dubercomponent.DuberBrushButton(514,62, pygame.transform.scale(brush_icon, (32,32)), brushes.Brush((0,0,0), 10, 10) ))
   
    #adding buttons to the list of shape buttons
    shape_list.append(dubercomponent.DuberShapeButton(586,20, rectangle_icon))
    shape_list.append(dubercomponent.DuberShapeButton(671, 20, ellipse_icon))
    shape_list.append(dubercomponent.DuberShapeButton(756,20, line_icon))
>>>>>>> Stashed changes




    while run:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # only detects user input for these objects if they are in the
            # login screen
            if login_screen:

                # detects if a user clicked on a text box to enter information
                if (event.type == pygame.MOUSEBUTTONDOWN) and (
                        event.button == 1):
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

                        username = username_box.get_text()
                        ip = ip_box.get_text()
                        port = port_box.get_text()
                        join_code = join_code_box.get_text()

                        login_screen = join_room()
                    elif create_room_button.selected(pygame.mouse.get_pos()):

                        username = username_box.get_text()
                        ip = ip_box.get_text()
                        port = port_box.get_text()

                        login_screen = create_room()

                # lets the user remove information for logging in
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if editing_username:
                            username_box.set_text(
                                username_box.get_text()[0:-1])
                        elif editing_ip:
                            ip_box.set_text(ip_box.get_text()[0:-1])
                        elif editing_port:
                            port_box.set_text(port_box.get_text()[0:-1])
                        elif editing_join_code:
                            join_code_box.set_text(
                                join_code_box.get_text()[0:-1])

                    # lets the user enter in information for logging in
                    else:
                        if editing_username and len(
                                username_box.get_text()) < 10:
                            username_box.set_text(
                                username_box.get_text() + event.unicode)
                        elif editing_ip and len(ip_box.get_text()) < 15:
                            ip_box.set_text(ip_box.get_text() + event.unicode)
                        elif editing_port and len(port_box.get_text()) < 4:
                            port_box.set_text(
                                port_box.get_text() + event.unicode)
                        elif editing_join_code and len(join_code_box.get_text()) < 6:
                            join_code_box.set_text(
                                join_code_box.get_text() + event.unicode)

            # user interactions for the main program after logging in
            # (UNFINISHED)
            else:
                if((event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1)):
                    if colour_selection_area.selected(pygame.mouse.get_pos()):
                        print("Colour area clicked")
                    elif brush_selection_area.selected(pygame.mouse.get_pos()):
                        print("brush area clicked")
                    elif shape_selection_area.selected(pygame.mouse.get_pos()):
                        print("shape tool area selected")
                    elif leave_button.selected(pygame.mouse.get_pos()):
                        print("Leave button selected")
                    elif (200 >= pygame.mouse.get_pos()[0] <= 1080) and (115 >= pygame.mouse.get_pos()[1] <= 720):
                        print("drawing on the canvas")
                # we haven't gotten to that part yet

        # update the screen
        if login_screen:
            update_login_screen()
        else:
            update_main_screen()


def update_main_screen():
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255,255,255), (0,0, 1080, 115), True) #top part of interface
    pygame.draw.rect(window, (255,255,255), (0,0, 200, 720), True) #left part of interface
    pygame.draw.rect(window, (255,255,255), (200,115, 880,605), False) #canvas

    window.blit(pygame.transform.scale(logo, (166,115)), (0,0))
    
    colour_selection_area.draw(window)
    brush_selection_area.draw(window)
    shape_selection_area.draw(window)
    leave_button.draw(window)

    for object in board_elements:
        object.draw(window)

    for user in user_list:
        user.draw(window)

    pygame.display.flip()


def update_login_screen():
    """
    Updates the login window when it is being used
    """

    window.fill((0, 0, 0))
    window.blit(logo, (330, 30))
    window.blit(
        login_font.render(
            'Username:', True, (255, 255, 255)), (300, 400))
    window.blit(
        login_font.render(
            'IP Address:', True, (255, 255, 255)), (300, 430))
    window.blit(
        login_font.render(
            'Port:', True, (255, 255, 255)), (300, 460))
    window.blit(
        login_font.render(
            'Join Code:', True, (255, 255, 255)), (25, 550))
    window.blit(
        login_font.render(
            'Or', True, (255, 255, 255)), (530, 550))
    username_box.draw(window)
    ip_box.draw(window)
    port_box.draw(window)
    join_code_box.draw(window)
    create_room_button.draw(window)
    join_button.draw(window)

    pygame.display.flip()


if __name__ == "__main__":
    main()
