from threading import Thread
import socket
import board
import user
import time

boards = []  # stores all the boards
clients = []  # stores all clients (user, conn, board)

current_user_id = 0  # next ID to assign to a user
current_join_code = 0  # next join code to assign to a board


def parse_join_code(join_code):
    """
    takes the join code and makes sure it's at least 6 digits long

    Args:
        join_code (int): the number of join codes sent out so far

    Returns:
        string: the actual join code
    """
    if join_code < 10:
        return f"00000{join_code}"
    elif join_code < 100:
        return f"0000{join_code}"
    elif join_code < 1000:
        return f"000{join_code}"
    elif join_code < 10000:
        return f"00{join_code}"
    elif join_code < 100000:
        return f"0{join_code}"
    else:
        return f"{join_code}"

def parse_point_and_colour(point_or_colour_string):
    """
    Parses a point or colour to just space separated characters

    Args:
        point_string (string): The point in string format as "(x, y)" or colour as "[r, g, b]"

    Returns:
        string: the point parsed into "x y" or clour as "r g b"
    """
    point_or_colour_string = point_or_colour_string[1:-1]
    return " ".join(point_or_colour_string.split(", "))

def send(conn, message):
    """
    Sends a message to the client

    Args:
        conn (socket): the socket to use to send the message
        message (string): the string to send
    """
    conn.send(message.encode())


def send_to_board_members(board, message):
    """
    Sends a message all members using the board

    Args:
        board (board.Board): the board to broadcast the message to
        message (string): the message to boardcast
    """
    board_users = board.get_users()
    for user in board_users:
        for client in clients:
            if client[0] == user:
                send(client[1], message)


def send_canvas(conn, board):
    """
    Sends the board data over

    Args:
        conn (socket): [description]
        board (board.Board): [description]
    """
    canvas_data = f"{len(board.canvas)} {len(board.canvas[0])}\n"
    for row in board.canvas:
        for colour in row:
            canvas_data += f"{colour[0]},{colour[1]},{colour[2]}|"
        canvas_data += "\n"
    # send(conn, f"<b>\n{canvas_data}")


def join_room(conn, data):
    """
    Handles when a user joins a room

    Args:
        conn (socket): the socket the message was sent from and where messages should be sent to
        data (list): all the data that was sent over
    """
    global current_user_id
    if len(data) == 3:
        success = False
        right_board = None
        for board in boards:
            if board.check_invite_code(data[2]):
                new_user = user.User(data[1], current_user_id, False)
                clients.append((new_user, conn, board))
                board.add_user(new_user)
                right_board = board
                success = True
        if success:
            # send user in reply
            send(conn, f"<c>\n{current_user_id}\n{data[2]}")
            # send_canvas(conn, right_board)
            # send to board member that a new user joined
            for user_to_send in right_board.get_users():
                for client in clients:
                    if (client[0] == user_to_send) and (client[1] is not conn):
                        print(f"<uj>\n{user_to_send.get_username()}\n{user_to_send.get_id()}")
                        send(conn, f"<uj>\n{user_to_send.get_username()}\n{user_to_send.get_id()}")
                        time.sleep(0.2)
            send_to_board_members(
                right_board, f"<uj>\n{data[1]}\n{current_user_id}")
        else:
            send(conn, "<X>")
        current_user_id += 1
    else:
        send(conn, "<X>")


def create_room(conn, data):
    """
    Handles when user requests to create a room

    Args:
        conn (socket): the socket the message was sent from and where messages should be sent to
        data (list): all the data that was sent over
    """
    global current_join_code
    global current_user_id
    if len(data) == 2:
        join_code = parse_join_code(current_join_code)
        current_join_code += 1
        new_user = user.User(data[1], current_user_id, True)
        # TODO: make this not a fixed value later
        boards.append(board.Board((720, 1080), join_code, new_user))
        clients.append((new_user, conn, boards[-1]))
        boards[-1].add_user(new_user)
        send(conn, f"<c>\n{current_user_id}\n{join_code}")
        send(conn, f"<uj>\n{data[1]}\n{current_user_id}")
        current_user_id += 1
        # send_canvas(conn, boards[-1])
    else:
        send(conn, "<X>")


def draw(conn, data):
    """
    Handles when a user decides to draw on the board

    Args:
        conn (socket): the socket connection
        data (list): data being sent over
    """
    if len(data) == 5:
        for board in boards:
            if board.check_invite_code(data[1]):
                send_to_board_members(
                    board, f"<d>\n{parse_point_and_colour(data[2])}\n{data[3]}\n{parse_point_and_colour(data[4])}")


def draw_rectangle(conn, data):
    """
    Handles a rectangle being drawn

    Args:
        conn (socket): the socket the message came from
        data (list): the data the client sent
    """
    if len(data) == 6:
        for board in boards:
            if board.check_invite_code(data[1]):
                send_to_board_members(
                    board, f"<r>\n{parse_point_and_colour(data[2])}\n{parse_point_and_colour(data[3])}\n{parse_point_and_colour(data[4])}\n{data[5]}")


def draw_ellipse(conn, data):
    """
    Handles an ellipse being drawn

    Args:
        conn (socket): the connection the message was from
        data (list): the data that the client sent
    """
    if len(data) == 6:
        for board in boards:
            if board.check_invite_code(data[1]):
                send_to_board_members(
                    board, f"<e>\n{parse_point_and_colour(data[2])}\n{parse_point_and_colour(data[3])}\n{parse_point_and_colour(data[4])}\n{data[5]}")


def draw_line(conn, data):
    """
    Handles a line being drawn

    Args:
        conn (socket): the connection the message was from
        data (list): the data the client sent
    """
    if len(data) == 5:
        for board in boards:
            if board.check_invite_code(data[1]):
                send_to_board_members(
                    board, f"<L>\n{parse_point_and_colour(data[2])}\n{parse_point_and_colour(data[3])}\n{parse_point_and_colour(data[4])}")


def disconnect(conn, data):
    """
    Handles a user disconnect

    Args:
        conn (socket): the socket connection
        data (list): the data being sent over
    """
    if len(data) == 1:
        for client in clients:
            if client[1] == conn:
                send_to_board_members(client[2], f"<dc>\n{client[0].get_id()}")
                client[1].close()
                clients.remove(client)  # not sure if this handles it nicely


def kick(conn, data):
    """
    Handles kicking a user

    Args:
        conn (socket): the socket connection
        data (list): the data being sent over
    """
    if len(data) == 2:
        for client in clients:
            if client[0].get_id == int(data[1]):
                send_to_board_members(client[2], f"<dc>\n{data[1]}")
                client[1].close()
                clients.remove(client)


command_map = {
    "<j>": join_room,
    "<c>": create_room,
    "<dc>": disconnect,
    "<d>": draw,
    "<r>": draw_rectangle,
    "<e>": draw_ellipse,
    "<L>": draw_line,
    "<k>": kick
}


def client_listener(conn, addr):
    """
    Listens to a specific client

    Args:
        conn (socket.socket): socket to listen to
        addr (tuple): Where the connection is coming from
    """
    print(f"connection from {addr}")
    connected = True  # change to False on disconnect
    while connected:
        data = conn.recv(4096).decode("utf-8")
        print(data)
        command = data.splitlines()[0]
        print(command)
        if command in command_map.keys():
            command_map[command](conn, data.splitlines())


def main():
    """
    The main function
    """
    while 1:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(("127.0.0.1", 5000))
            sock.listen()
            conn, addr = sock.accept()
            Thread(target=client_listener, args=(conn, addr)).start()


if __name__ == "__main__":
    main()
