from threading import Thread
import socket

threads = []  # idk why we need to keep track of all the threads
boards = []  # stores all the boards
users = [] # stores all users

current_user_id = 0 # next ID to assign to a user
current_join_code = 0 # next join code to assign to a board

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


if __name__ == "__main__":
    main()
