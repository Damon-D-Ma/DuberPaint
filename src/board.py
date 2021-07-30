"""
Contains a board class
"""


class Board:
    """[summary]
    """

    def __init__(self, size, invite_code):
        """
        Constructor for the board class

        Args:
            size (tuple): in the format of (height, width) of the canvas
            invite_code (string): the invite code for the board
        """
        self.invite_code = invite_code
        self.canvas = []
        for i in range(size[0]):
            temp = []
            for j in range(size[1]):
                temp.append([255, 255, 255])
            self.canvas.append(temp)
