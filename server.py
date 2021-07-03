from threading import Thread
import socket
        
threads = []

def client_listener(conn, addr):
    pass

def main():
    """
    The main function
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 5000))
        sock.listen()
        conn, addr = sock.accept()
        thread = Thread(target=client_listener, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()