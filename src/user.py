"""
Contains a User class
"""


class User:
    """
    Class for Users
    """

    def __init__(self, username, id):
        """
        Constructor for the User class

        Args:
            username (string): the user's username
            id (int): the user's unique ID used to identify them
        """
        self.__username = username
        self.__id = id

    def get_username(self):
        """
        Gets the user's username

        Returns:
            string: the user's username
        """
        return self.__username

    def get_id(self):
        """
        Gets the user's ID

        Returns:
            int: the user's ID
        """
        return self.__id
