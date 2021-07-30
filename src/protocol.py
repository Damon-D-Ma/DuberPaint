"""
Contains all needed protocol for the drawing program
"""


class Protocol:
    """
    class for general protocol between the server and client programs
    """

    def __init__(self):
        """
        Constructor for the class
        """

    def encode(self, message):
        """
        Encodes a received message

        Args:
            message (String): The original message that needs to be encoded before being sent
        """

    def decode(self, message):
        """
        Decodes a received message

        Args:
            message (string): The received message that needs to be decoded
        """

    def send(self):
        """
        Sends a message
        """

    def recv(self):
        """
        Receives a message
        """


class ColourProtocol(Protocol):
    """
    protocol for storing the colour of a pixel
    """

    def __init__(self, x, y, r, g, b):
        """
        Constructor, assigns values

        Args:
            x (int): x position
            y (int): y position
            r (int): red value
            g (int): green value
            b (int): blue value
        """
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b


class ConnectToBoardProtocol(Protocol):
    """
    protocol sent for sending a request for connecting to a board
    """

    def __init__(self, invite_code):
        """
        Constructor

        Args:
            invite_code (string): the sent invite code to connect to board
        """
        self.invite_code = invite_code
