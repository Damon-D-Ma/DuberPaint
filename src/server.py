from threading import Thread
import socket
import board
import user

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


def send(conn, message):
    """
    Sends a message to the client

    Args:
        conn (socket): the socket to use to send the message
        message (string): the string to send
    """
    conn.send(message.encode())


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
        for board in boards:
            if board.check_invite_code(data[2]):
                new_user = user.User(data[1], current_user_id)
                clients.append((new_user, conn, board))
                board.add_user(new_user)
                success = True
                # TODO: send board for the join code
        send(conn, f"<j>\n{current_user_id}") if success else send(conn, "<X>")
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
        new_user = user.User(data[1], current_user_id)
        # TODO: make this not a fixed value later
        boards.append(board.Board((720, 720), join_code, new_user))
        clients.append((new_user, conn, boards[-1]))
        send(conn, f"<c>\n{current_user_id}\n{join_code}")
        current_user_id += 1
    else:
        send(conn, "<X>")

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
                client[1].close()
                user_id = client[0].get_id()
                board = client[2]
                board_users = board.get_users()
                for user in board_users:
                    for message_target in clients:
                        if message_target[0] == user:
                            send(message_target[1], f"<dc>\n{user_id}")
                clients.remove(client) # not sure if this handles it nicely

command_map = {
    "<j>": join_room, 
    "<c>": create_room, 
    "<dc>": disconnect}


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
