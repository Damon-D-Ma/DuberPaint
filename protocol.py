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

        
        """

