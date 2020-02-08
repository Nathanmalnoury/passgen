import os


class PasswordFile:
    def __init__(self, filepath, salt=None):
        self.filepath = filepath
        self.salt = salt

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return "filepath: {};\nsalt: {}".format(self.filepath, self.salt)

    def set_salt(self, salt):
        self.salt = salt
        return True

    def get_salt(self):
        return self.salt

    def is_complete(self):
        if os.path.isfile(self.filepath):
            raise FileExistsError("file already exists in your system.")
        if self.salt is None:
            raise TypeError("Salt is None")

        return True

    def to_json(self):
        return {
            "filepath": self.filepath,
            "salt": self.salt.decode('latin-1'),
        }

    @staticmethod
    def from_json(json_dict):
        """

        :param json_dict:
        :type json_dict: dict
        :return:
        """
        return PasswordFile(
            filepath=json_dict.get("filepath"),
            salt=bytes(json_dict.get("salt"), encoding='latin-1')
        )
