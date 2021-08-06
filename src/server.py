from threading import Thread
import socket
import board
import user

threads = []  # idk why we need to keep track of all the threads
boards = []  # stores all the boards
users = []  # stores all users

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
        data (string): all the data that was sent over
    """
    global current_user_id
    if len(data) == 3:
        users.append(user.User(data[1], current_user_id))
        success = False
        for board in boards:
            if board.get_invite_code() == data[2]:
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
        data (string): all the data that was sent over
    """
    global current_join_code
    global current_user_id
    if len(data) == 2:
        join_code = parse_join_code(current_join_code)
        current_join_code += 1
        users.append(user.User(data[1], current_user_id))
        # TODO: make this not a fixed value later
        boards.append(board.Board((720, 720), join_code, users[-1]))
        send(conn, f"<c>\n{current_user_id}\n{join_code}")
        current_user_id += 1
    else:
        send(conn, "<X>")

command_map = {"<j>": join_room, "<c>": create_room}

def disconnect(conn, data):
    if len(data) == 1:
        # TODO: loopthroug threads and figure out which one it is or have an identifier for the thread and users
        pass

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
            thread = Thread(target=client_listener, args=(conn, addr))
            thread.start()
            threads.append(thread)


if __name__ == "__main__":
    main()
