"""
Contains a User class
"""


class User:
    """
    Class for Users
    """

    def __init__(self, username, id, owner):
        """
        Constructor for the User class

        Args:
            username (string): the user's username
            id (int): the user's unique ID used to identify them
            owner (boolean): whether this user is the owner of the room or not
        """
        self.__username = username
        self.__id = id
        self.__owner = owner

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

    def get_owner(self):
        """
        Gets the user's ownership status

        Returns:
            boolean: whether the user is the owner of their current room or not
        """
        return self.__owner
