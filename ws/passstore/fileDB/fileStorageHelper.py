import json
import os
import sys
from builtins import print

from ws.passstore.fileDB.password_file import PasswordFile


class FileStorageHelper:
    def __init__(self):
        self.filename = os.path.join(os.path.dirname(sys.argv[0]), "./../../pass_files.json")
        self.content = []  # list of PasswordFile

    def load_db(self):
        with open(file=self.filename, mode='r') as f:
            self.content = json.load(f)
        assert type(self.content) == list
        self.content = [PasswordFile.from_json(d) for d in self.content]

    def _is_filepath_taken(self, filepath):
        for file_ in self.content:
            if file_.filepath == filepath:
                return True
        return False

    def add_file(self, file):
        """

        :param file:
        :type file: PasswordFile
        :return: bool, indicating the success of the adding
        """
        if not file.is_complete():
            print("something doesn't work with this entry")
            return False

        if not self._is_filepath_taken(file.filepath):
            self.content.append(file)
            return True

        else:
            print("File already exists. Please choose another one")
            raise ValueError("Entry exists in database")

    def delete_file(self, file):
        """

        :param file:
        :type file: PasswordFile
        :return:
        """
        for f in self.content:
            if f == file:
                self.content.remove(f)
                print("delete succeed")
                return True

        print("no such file in database")
        return False

    def get_file(self, filepath):
        """

        :param filepath: str
        :return:
         :rtype: PasswordFile
        """
        for file_ in self.content:
            if file_.filepath == filepath:
                return file_

        raise ValueError("no such file in database")

    def get_all_files(self):
        return [f.filepath for f in self.content]

    def save_db(self):
        to_save = [f.to_json for f in self.content]
        with open(self.filename, 'w') as f:
            json.dump(to_save, f, indent=4)

    @staticmethod
    def get_salt_from_path(path):
        fsh = FileStorageHelper()
        fsh.load_db()
        return fsh.get_file(path).salt
