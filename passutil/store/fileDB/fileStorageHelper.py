"""Util class to access the Storage file, which keeps track of the PasswordFile in the OS."""
import json
import os
import sys

from store.click_commands import ok_msg, err_msg
from store.fileDB.password_file import PasswordFile


class FileStorageHelper:
    """
    Help with the FileStorage (pass_files.json).

    Includes methods to:

    - load / save the file
    - CRUD on the entry in the file
    """

    file_name = os.path.join(os.path.dirname(sys.argv[0]), "./pass_files.json")

    def __init__(self):
        """Init a FileStorageInstance."""
        self.content = []  # list of PasswordFile

    def load_db(self):
        """
        Load the file into content attribute.

        :return: None
        :raise AssertionError:
        """
        with open(file=FileStorageHelper.file_name, mode='r') as f:
            self.content = json.load(f)
        assert type(self.content) == list
        self.content = [PasswordFile.from_json(d) for d in self.content]

    def _is_file_path_taken(self, file_path):
        for file_ in self.content:
            if file_.file_path == file_path:
                return True
        return False

    def add_file(self, file):
        """
        Add a new entry in the storage file, corresponding to a new PasswordFile.

        :param file: PasswordFile to add to the content.
        :type file: PasswordFile
        :return: bool, indicating the success of the adding
        :raise ValueError:
        """
        if not file.is_complete():
            print("something doesn't work with this entry")
            return False

        if not self._is_file_path_taken(file.file_path):
            self.content.append(file)
            return True

        else:
            print("File already exists. Please choose another one")
            raise ValueError("Entry exists in database")

    def delete_file(self, file):
        """
        Delete an PasswordFile entry from the storage file.

        :param file: PasswordFile to delete
        :type file: PasswordFile
        :return: True in case of success, False otherwise.
        :rtype: bool
        """
        for f in self.content:
            if f == file:
                self.content.remove(f)
                ok_msg("delete succeed")
                return True

        err_msg("no such file in database")
        return False

    def get_file(self, file_path):
        """
        Get a PasswordFile from storage file given its path.

        :param file_path: path to the PasswordFile in the OS.
        :type file_path: str
        :return: PasswordFile
        :rtype: PasswordFile
        :raise ValueError:
        """
        for file_ in self.content:
            if file_.file_path == file_path:
                return file_

        raise ValueError("no such file in database")

    def get_all_files(self):
        """
        Return all the path of PasswordFile contained in the storage file.

        Does not output the salt of those files.

        :return: list of each PasswordFile's path
        :rtype: list of str
        """
        return [f.file_path for f in self.content]

    def save_db(self):
        """
        Save the updated content of PasswordFile into the storage file.

        :return: None
        :rtype: None
        """
        to_save = [f.to_json() for f in self.content]
        with open(FileStorageHelper.file_name, 'w') as f:
            json.dump(to_save, f, indent=4)

    @staticmethod
    def get_salt_from_path(file_path):
        """
        Get salt for a PasswordFile given it's name.

        :param file_path: path of the PasswordFile.
        :type file_path: str
        :return: salt
        :rtype; bytes
        """
        fsh = FileStorageHelper()
        fsh.load_db()
        return fsh.get_file(file_path).salt
