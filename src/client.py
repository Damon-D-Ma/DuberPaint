from threading import Thread
import pygame
import socket
import user
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
brush_icon = None
eraser_icon = None
line_icon = None
rectangle_icon = None
ellipse_icon = None

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
export_button = None
join_code_area = None

board_elements = []
user_list = []
user_button_list = []
main_font = None

colour_selection_area = None
brush_selection_area = None
shape_selection_area = None
user_selection_area = None
kick_button = None

run = True
server_thread = None

brush_list = []
colour_list = []
shape_list = []


def send(message):
    """
    sends a message to the server

    Args:
        message (string): the message to be sent to the server
    """
    global sock
    sock.send(message.encode())
    # incomplete function

def export_drawing():
    """
    Exports a screenshot of the board that the users drew on
    """
    #TODO not complete

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
    """
    Disconnects the client from the server
    """
    global server_thread
    global sock
    message = f'<dc>\n{user_id}'
    send(message)
    del(server_thread)
    sock.close()


def kick_user(target_id):
    """
    Kicks a selected user if the current user is the owner of the room

    Args:
        target_id (string): the user id of the user to be kicked
    """

    if owner:
        message = f'<k>\n{target_id}'
        send(message)


def recv_successful(data):
    """
    What happens when the connection was successful

    Args:
        data (list): All the data that was send over
    """
    global userid
    global join_code
    userid = int(data[1])
    join_code = data[2]


def recv_login_failed(data):
    """
    Shows connection failed

    Args:
        data (list): In this case is just ["<X>"] and is here to follow convention
    """
    pass  # connection failed


def recv_draw(data):
    """
    Handles receiving a draw mark

    Args:
        data (list): the data sent over by the server
    """
    if len(data) == 4:
        # TODO: do stuff with the data
        coords = (int(data[1].split(" ")[0]), int(data[1].split(" ")[1]))
        width = int(data[2])
        colour = (int(data[3].split(" ")[0]), int(
            data[3].split(" ")[1]), int(data[3].split(" ")[2]))


def recv_rectangle(data):
    """
    Handles receiving a rectangle

    Args:
        data (list): the data sent over by the server
    """
    if len(data) == 5:
        top_left = (int(data[1].split(" ")[0]), int(data[1].split(" ")[1]))
        bottom_right = (int(data[2].split(" ")[0]), int(data[2].split(" ")[1]))
        colour = (int(data[3].split(" ")[0]), int(
            data[3].split(" ")[1]), int(data[3].split(" ")[2]))
        fill = (int(data[4].split(" ")[0]),
                int(data[4].split(" ")[1]),
                int(data[4].split(" ")[2]))
        # TODO: do stuff with the data


def recv_ellipse(data):
    """
    Handles receiving an ellipse

    Args:
        data (list): the data sent over by the server
    """
    if len(data) == 5:
        top_left = (int(data[1].split(" ")[0]), int(data[1].split(" ")[1]))
        bottom_right = (int(data[2].split(" ")[0]), int(data[2].split(" ")[1]))
        colour = (int(data[3].split(" ")[0]), int(
            data[3].split(" ")[1]), int(data[3].split(" ")[2]))
        fill = (int(data[4].split(" ")[0]),
                int(data[4].split(" ")[1]),
                int(data[4].split(" ")[2]))
        # TODO: do stuff with the data


def recv_line(data):
    """
    Handles receiving a line

    Args:
        data (list): the data sent over by the server
    """
    if len(data) == 5:
        top_left = (int(data[1].split(" ")[0]), int(data[1].split(" ")[1]))
        bottom_right = (int(data[2].split(" ")[0]), int(data[2].split(" ")[1]))
        colour = (int(data[3].split(" ")[0]), int(
            data[3].split(" ")[1]), int(data[3].split(" ")[2]))
        # TODO: do stuff with the data


def recv_disconnect(data):
    """
    Handles a user disconnecting

    Args:
        data (list): the data being sent over by the server
    """
    if len(data) == 2:
        user_id_of_user_to_remove = int(data[1])
        # TODO: remove the user


def recv_user_join(data):
    """
    Handles a user joining

    Args:
        data (list): stuff sent over from the server
    """
    if len(data) == 3:
        new_user_id = int(data[1])
        new_username = data[2]
        # TODO: uh do stuff with this data


def recv_board(data):
    """
    Handles receiving board data

    Args:
        data (list): all the data that got sent over
    """
    width, height = int(data[1].split(" ")[0]), int(data[1].split(" ")[1])
    canvas = []
    for i in range(width):
        row = []
        row_data = data[i + 2].split("|")
        for j in range(height):
            colour_data = row_data[j].split(",")
            colour = [int(colour_data[0]), int(
                colour_data[1]), int(colour_data[2])]
            row.append(colour)
        canvas.append(row)


command_map = {
    "<c>": recv_successful,
    "<X>": recv_login_failed,
    "<d>": recv_draw,
    "<r>": recv_rectangle,
    "<e>": recv_ellipse,
    "<L>": recv_line,
    "<dc>": recv_disconnect,
    "<uj>": recv_user_join,
    "<b>": recv_board
}


def server_listener():
    """
    Listens to the server then calls a function to respond based on what the server sends
    """
    global sock
    global run
    while run:
        data = sock.recv(4096).decode("utf-8")
        print(data)
        command = data.splitlines()[0]
        command_map[command](data.splitlines())


def join_room():
    """
    Joins an existing room upon logging in

    Returns:
        boolean: True if successful, false otherwise
    """
    global sock
    global server_thread
    sock = socket.create_connection((ip, port))
    send(f"<j>\n{username}\n{join_code}")
    # unfinished method

    print(f"Joining room with: {username}, {ip}, {port}, {join_code}")

    # need condition to check if the login went through
    response = sock.recv(4096).decode("utf-8")
    if response == "<X>":
        return False
    elif len(response.splitlines()) == 3:
        user_id = int(response.splitlines[1])
        server_thread = Thread(target=server_listener).start()
        return True
    else:
        return False


def create_room():
    """
    Creates a new room upon logging in

    Returns:
        boolean: True if successful, False otherwise
    """
    global sock
    global owner
    global server_thread
    sock = socket.create_connection((ip, port))
    send(f"<c>\n{username}")
    print(f"Creating room with {username}, {ip}, {port}")

    owner = True

    # need condition to check if the login went through
    response = sock.recv(4096).decode("utf-8")
    if response == "<X>":
        return False
    elif len(response.splitlines()) == 3:
        user_id = int(response.splitlines()[1])
        join_code = response.splitlines()[2]
        server_thread = Thread(target=server_listener).start()
        return True
    else:
        return False


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
    global export_button
    global join_code_area
    global board_elements
    global user_list
    global user_button_list

    global colour_selection_area
    global brush_selection_area
    global shape_selection_area
    global user_selection_area
    global kick_button

    global brush_list
    global colour_list
    global shape_list

    global brush_icon
    global eraser_icon
    global line_icon
    global rectangle_icon
    global ellipse_icon

    global run

    pygame.init()
    pygame.display.set_caption("Duber Paint")

    #loading in assets
    logo = pygame.image.load("./assets/duberpaint.png")
    brush_icon = pygame.image.load("./assets/BrushIcon.png")
    eraser_icon = pygame.image.load("./assets/EraserIcon.png")
    line_icon = pygame.image.load("./assets/LineIcon.png")
    rectangle_icon = pygame.image.load("./assets/RectangleIcon.png")
    ellipse_icon = pygame.image.load("./assets/EllipseIcon.png")

    pygame.display.set_icon(logo)

    # screen size subject to change
    window_width = 1080
    window_length = 720
    window = pygame.display.set_mode((window_width, window_length))

    # uniform fonts the program
    login_font = pygame.font.Font(None, 32)
    main_font = pygame.font.Font(None, 32)

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
    


    # elements for main window
    colour_selection_area = dubercomponent.DuberComponent(
        240, 10, 160, 95, (128, 128, 128))
    brush_selection_area = dubercomponent.DuberComponent(
        420, 10, 136, 95, (128, 128, 128))
    shape_selection_area = dubercomponent.DuberComponent(
        576, 10, 265, 95, (128, 128, 128))
    user_selection_area = dubercomponent.DuberComponent(20,170,160,480, (128,128,128))
    join_code_area = dubercomponent.DuberTextBox(
            861, 10, 130, 55, (128, 128, 128), "Join Code:", main_font, (255, 255, 255))
    export_button = dubercomponent.DuberTextBox(
            861, 73, 130, 32, (128, 128, 128), "Export", main_font, (0, 128, 0))
    # kick user button
    kick_button = dubercomponent.DuberTextBox(
        20, 670, 160, 40, (255, 0, 0), "Kick User", main_font, (255, 0, 0))

    # booleans to operate program
    login_screen = True
    editing_username = False
    editing_ip = False
    editing_port = False
    editing_join_code = False

    using_brush = True
    drawing_rectangle = False
    drawing_ellipse = False
    drawing_line = False
    selected_user = user.User("", -1, False)

    # default colour for shapes that are drawn
    shape_colour = (0, 0, 0)

    # index of the brush selected
    brush_index = 0

    # Other values needed for the program
    current_brush = brushes.Brush((0, 0, 0), 10)

    # adding buttons to the list of colour buttons

    # row 1
    colour_list.append(dubercomponent.DuberColourButton(250, 18, (255, 0, 0)))
    colour_list.append(
        dubercomponent.DuberColourButton(
            280, 18, (255, 165, 0)))
    colour_list.append(
        dubercomponent.DuberColourButton(
            310, 18, (255, 255, 0)))
    colour_list.append(dubercomponent.DuberColourButton(340, 18, (0, 128, 0)))
    colour_list.append(dubercomponent.DuberColourButton(370, 18, (0, 0, 255)))

    # row 2
    colour_list.append(
        dubercomponent.DuberColourButton(
            250, 48, (128, 0, 128)))
    colour_list.append(dubercomponent.DuberColourButton(280, 48, (0, 0, 0)))
    colour_list.append(
        dubercomponent.DuberColourButton(
            310, 48, (255, 255, 255)))
    colour_list.append(
        dubercomponent.DuberColourButton(
            340, 48, (139, 69, 19)))
    colour_list.append(
        dubercomponent.DuberColourButton(
            370, 48, (128, 128, 128)))

    # row 3
    colour_list.append(
        dubercomponent.DuberColourButton(
            250, 78, (255, 255, 255)))
    colour_list.append(
        dubercomponent.DuberColourButton(
            280, 78, (255, 255, 255)))
    colour_list.append(
        dubercomponent.DuberColourButton(
            310, 78, (255, 255, 255)))
    colour_list.append(
        dubercomponent.DuberColourButton(
            340, 78, (255, 255, 255)))
    colour_list.append(
        dubercomponent.DuberColourButton(
            370, 78, (255, 255, 255)))

    # adding buttons to the list of brush buttons

    # row 1
    brush_list.append(
        dubercomponent.DuberBrushButton(
            430, 20, pygame.transform.scale(
                brush_icon, (32, 32)), brushes.Brush(
                (0, 0, 0), 10)))
    brush_list.append(
        dubercomponent.DuberBrushButton(
            472, 20, pygame.transform.scale(
                brush_icon, (32, 32)), brushes.Brush(
                (0, 0, 0), 10)))
    brush_list.append(
        dubercomponent.DuberBrushButton(
            514, 20, pygame.transform.scale(
                brush_icon, (32, 32)), brushes.Brush(
                (0, 0, 0), 10)))

    # row 2
    brush_list.append(
        dubercomponent.DuberBrushButton(
            430, 62, pygame.transform.scale(
                brush_icon, (32, 32)), brushes.Brush(
                (0, 0, 0), 10)))
    brush_list.append(
        dubercomponent.DuberBrushButton(
            472, 62, pygame.transform.scale(
                brush_icon, (32, 32)), brushes.Brush(
                (0, 0, 0), 10)))
    brush_list.append(
        dubercomponent.DuberBrushButton(
            514, 62, pygame.transform.scale(
                eraser_icon, (32, 32)), brushes.Eraser(10)))

    # adding buttons to the list of shape buttons
    shape_list.append(
        dubercomponent.DuberShapeButton(
            586, 20, pygame.transform.scale(
                rectangle_icon, (75, 75))))
    shape_list.append(
        dubercomponent.DuberShapeButton(
            671, 20, pygame.transform.scale(
                ellipse_icon, (75, 75))))
    shape_list.append(
        dubercomponent.DuberShapeButton(
            756, 20, pygame.transform.scale(
                line_icon, (75, 75))))
    

    # adding buttons to the list of user buttons
    user_button_list.append(dubercomponent.DuberUserButton(20,170, True, main_font, user.User("", -1, False) ))
    user_button_list.append(dubercomponent.DuberUserButton(20,210, True, main_font, user.User("", -1, False) ))
    user_button_list.append(dubercomponent.DuberUserButton(20,250, True, main_font, user.User("", -1, False) ))
    user_button_list.append(dubercomponent.DuberUserButton(20,290, True, main_font, user.User("", -1, False) ))
    user_button_list.append(dubercomponent.DuberUserButton(20,330, True, main_font, user.User("", -1, False) ))
    user_button_list.append(dubercomponent.DuberUserButton(20,370, True, main_font, user.User("", -1, False) ))
    user_button_list.append(dubercomponent.DuberUserButton(20,410, True, main_font, user.User("", -1, False) ))
    user_button_list.append(dubercomponent.DuberUserButton(20,450, True, main_font, user.User("", -1, False) ))
    user_button_list.append(dubercomponent.DuberUserButton(20,490, True, main_font, user.User("", -1, False) ))
    user_button_list.append(dubercomponent.DuberUserButton(20,530, True, main_font, user.User("", -1, False) ))
    user_button_list.append(dubercomponent.DuberUserButton(20,570, True, main_font, user.User("", -1, False) ))
    user_button_list.append(dubercomponent.DuberUserButton(20,610, True, main_font, user.User("", -1, False) ))
    #TODO: add the current users to the list of users
    
    while run:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if not login_screen:
                    disconnect()

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

                        login_screen = not join_room()
                    elif create_room_button.selected(pygame.mouse.get_pos()):

                        username = username_box.get_text()
                        ip = ip_box.get_text()
                        port = port_box.get_text()

                        login_screen = not create_room()

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
                    elif event.key == pygame.K_TAB:
                        if editing_username:
                            editing_username = False
                            editing_ip = True
                            editing_port = False
                            editing_join_code = False
                        elif editing_ip:
                            editing_username = False
                            editing_ip = False
                            editing_port = True
                            editing_join_code = False
                        elif editing_port:
                            editing_username = False
                            editing_ip = False
                            editing_port = False
                            editing_join_code = True
                        elif editing_join_code:
                            editing_username = True
                            editing_ip = False
                            editing_port = False
                            editing_join_code = False
                    # editing_username = True
                    #     editing_ip = False
                    #     editing_port = False
                    #     editing_join_code = False
                    elif (event.key == pygame.K_LCTRL) or (event.key == pygame.K_RCTRL):
                        pass  # TODO: handle ctrl being pressed
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
                        for colour_button in colour_list:
                            if colour_button.selected(pygame.mouse.get_pos()):
                                if drawing_rectangle or drawing_ellipse or drawing_line:
                                    shape_colour = colour_button.get_colour()
                                elif not isinstance(current_brush, brushes.Eraser) and using_brush:
                                    current_brush.set_colour(
                                        colour_button.get_colour())
                                    brush_list[brush_index].set_colour(
                                        colour_button.get_colour())
                                break

                    elif brush_selection_area.selected(pygame.mouse.get_pos()):
                        temp_brush_index = 0
                        for brush_button in brush_list:
                            temp_brush_index += 1
                            if brush_button.selected(pygame.mouse.get_pos()):
                                current_brush = brush_button.get_brush()
                                brush_index = temp_brush_index
                                using_brush = True
                                drawing_rectangle = False
                                drawing_ellipse = False
                                drawing_line = False
                                break

                    elif shape_selection_area.selected(pygame.mouse.get_pos()):
                        if shape_list[0].selected(pygame.mouse.get_pos()):
                            drawing_rectangle = True
                            using_brush = False
                            drawing_ellipse = False
                            drawing_line = False
                        elif shape_list[1].selected(pygame.mouse.get_pos()):
                            drawing_ellipse = True
                            using_brush = False
                            drawing_rectangle = False
                            drawing_line = False
                        elif shape_list[2].selected(pygame.mouse.get_pos()):
                            drawing_line = True
                            using_brush = False
                            drawing_rectangle = False
                            drawing_ellipse = False
                    elif user_selection_area.selected(pygame.mouse.get_pos()):
                        for user_button in user_button_list:
                            if user_button.selected(pygame.mouse.get_pos()):
                                selected_user = user_button.get_user()
                                break
                    elif kick_button.selected(pygame.mouse.get_pos()):
                         kick_user(selected_user)
                    elif export_button.selected(pygame.mouse.get_pos()):
                        export_drawing()
                    elif (200 >= pygame.mouse.get_pos()[0] <= 1080) and (115 >= pygame.mouse.get_pos()[1] <= 720):
                        if using_brush:
                            send_brush_mark(
                                current_brush.make_brush_stroke(
                                    pygame.mouse.get_pos()))
                        elif drawing_rectangle:
                            # send_rect()
                            print("Drawing Rectangle")
                        elif drawing_ellipse:
                            # send_ellipse
                            print("Drawing Ellipse")
                        elif drawing_line:
                            # send_line()
                            print("Drawing Line")

        # update the screen
        if login_screen:
            update_login_screen()
        else:
            update_main_screen()
    pygame.quit()


def update_main_screen():
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 255, 255), (0, 0, 1080,
                     115), True)  # top part of interface
    pygame.draw.rect(window, (255, 255, 255), (0, 0, 200, 720),
                     True)  # left part of interface
    pygame.draw.rect(window, (255, 255, 255),
                     (200, 115, 880, 605), False)  # canvas

    window.blit(pygame.transform.scale(logo, (166, 115)), (0, 0))

    colour_selection_area.draw(window)
    brush_selection_area.draw(window)
    shape_selection_area.draw(window)
    kick_button.draw(window)
    export_button.draw(window)        
    window.blit(main_font.render('Users:', True, (255, 255, 255)), (20, 130))
    window.blit(main_font.render(join_code, True, (255, 255, 255)), (866, 34))

    for colours in colour_list:
        colours.draw(window)

    for brushes in brush_list:
        brushes.draw(window)

    for shapes in shape_list:
        shapes.draw(window)

    for object in board_elements:
        object.draw(window)

    for user in user_button_list:
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
