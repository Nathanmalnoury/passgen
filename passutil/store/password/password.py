"""Define a PasswordEntry."""
import json


class PasswordEntry:
    """
    Define a PasswordEntry.

    Include some basic functions to:

    - Print a PasswordEntry
    - Serialize, deserialize a PasswordEntry
    """

    def __init__(self, username, password, name):
        """
        Create new PasswordEntry instance.

        :param username: username for this PasswordEntry
        :type username: str
        :param password: password for this PasswordEntry
        :type password: str
        :param name: Name of this PasswordEntry. Considered as the index of the Entry.
        :type name: str
        :raise TypeError:
        """
        if name is None:
            raise TypeError("'name' cannot be None")
        self.username = username
        self.password = password
        self.name = name

    def __str__(self):
        """Change the way a PasswordEntry instance is printed."""
        return "name:{}\nusername: {}\nPassword: {}".format(self.name, self.username, self.password)

    def to_dict(self):
        """
        Make a dict from a PasswordEntry object.

        :return: dict with the PasswordEntry attributes
        :rtype: dict
        """
        return {'name': self.name, 'username': self.username, 'password': self.password}

    def to_json(self):
        """
        Make a PasswordEntry object serializable.

        :return: str
        """
        return json.dumps(self.to_dict(), indent=4)

    @staticmethod
    def from_json(json_data):
        """
        Create a PasswordEntry with a Json object.

        :param json_data: str, JSON Formatted
        :type json_data: str
        :return: PasswordEntry
        :rtype: PasswordEntry
        """
        return PasswordEntry(**json.loads(json_data))
