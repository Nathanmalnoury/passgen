"""Data Model of PasswordFile."""
import json
import os


class PasswordFile:
    """
    Define the structure of a PasswordFile object.

    includes function to:

    - check equality between to PasswordFile,
    - get/set the attributes of PasswordFile
    - check that an Entry is complete and ready to be saved.
    - serialize/deserialize a PasswordFile
    """

    def __init__(self, file_path, salt=None):
        """
        Initialize a new PasswordFile object.

        :param file_path: path of the PasswordFile
        :type file_path: str
        :param salt: salt of the PasswordFile
        :type salt: bytes or None
        """
        self.file_path = file_path
        self.salt = salt

    def __eq__(self, other):
        """
        Define equality between two PasswordFile instances.

        Based on the fact that path are unique in any filesystem.

        :param other: Other PasswordFile
        :type other: PasswordFile
        :return: True or False
        :rtype: bool
        """
        return self.__dict__ == other.__dict__

    def __str__(self):
        """Change the way PasswordFile objects are printed."""
        return "file path: {};\nsalt: {}".format(self.file_path, self.salt)

    def set_salt(self, salt):
        """
        Set salt.

        :param salt: salt
        :type salt: bytes
        :return: True
        """
        self.salt = salt
        return True

    def get_salt(self):
        """
        Get salt.

        :return: salt
        :rtype: bytes
        """
        return self.salt

    def is_complete(self):
        """
        Check if a PasswordFile object is ready to be saved in the storage file, and that a new file can be created.

        :return: True
        :raise FileExistsError, TypeError:
        """
        if os.path.isfile(self.file_path):
            raise FileExistsError("file already exists in your system.")
        if self.salt is None:
            raise TypeError("Salt is None")

        return True

    def to_json(self):
        """
        Make PasswordFile serializable.

        :return: dict with the attributes of PasswordFile instance.
        :rtype: dict
        """
        return json.dumps({"file_path": self.file_path, "salt": self.salt.decode('latin-1')})

    @staticmethod
    def from_json(json_data):
        """
        Create a PasswordFile object from a dictionary.

        :param json_data: JSON formatted str containing the attributes of PasswordFile to create.
        :type json_data: str
        :return: PasswordFile
        :rtype: PasswordFile
        """
        data = json.loads(json_data)
        return PasswordFile(file_path=data.get("file_path"), salt=bytes(data.get("salt"), encoding='latin-1'))
