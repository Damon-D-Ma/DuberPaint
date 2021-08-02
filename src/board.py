"""
Contains a board class
"""


class Board:
    """[summary]
    """

    def __init__(self, size, invite_code, owner):
        """
        Constructor for the board class

        Args:
            size (tuple): in the format of (height, width) of the canvas
            invite_code (string): the invite code for the board
            owner (string): the user id of the board's owner
        """
        self._invite_code = invite_code
        self._owner = owner
        self._board_elements = []
        self._user_list = []

        
        self._canvas = []

        for i in range(size[0]):
            temp = []
            for j in range(size[1]):
                temp.append([255, 255, 255])
            self.canvas.append(temp)

    def get_invite_code(self):
        """
        Gets the invite code

        Returns:
            string: the invite code
        """
        return self.__invite_code
