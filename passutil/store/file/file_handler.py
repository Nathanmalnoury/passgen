"""Class responsible for handling a Password File (not the Storage File)."""
import json
import os

from click_utils import info_msg, ok_msg
from store.encryption_manager import EncryptionManager
from store.fileDB.fileStorageHelper import FileStorageHelper
from store.fileDB.password_file import PasswordFile
from store.password.password import PasswordEntry


class FileHandler:
    """
    Help managing a Password File.

    Includes commands as:

    - Create / delete a Password File
    - CRUD on passwords in a Password File
    """

    def __init__(self, file_path, password, salt):
        """
        Init function to instantiate a FileHandler.

        :param file_path: the path of the Password File we want to Manage.
        :type file_path: str
        :param password: the password of the Password File. Will not be saved (The key will be instead).
        :type password: str
        :param salt: the salt of the Password file. Will be saved.
        :type salt: bytes
        :return: None
        """
        # TODO: should take a PasswordFile instead?
        self.file_path = file_path
        self.salt = salt
        self.key = EncryptionManager.generate_key(salt=salt, password=password)

    @staticmethod
    def create_file(file_path, password):
        """
        Create a new file, static method.

        Uses the FileStorage Helper to coordinate the creation of the file with its addition to the Storage File.

        :param file_path: Path of the Password File to create.
        :type file_path: str
        :param password: Password to assign to the Password File to create.
        :type password: str
        :return: False if the operation failed, the FileHandler object created otherwise.
        :rtype: Union(bool, FileHandler)
        """
        fsh = FileStorageHelper()
        fsh.load_db()

        key, salt = EncryptionManager().generate_new_key(password=password)
        pass_file = PasswordFile(file_path=file_path, salt=salt)

        if not pass_file.is_complete():
            info_msg("Something is wrong. Log to be detailed")
            return False

        if not fsh.add_file(pass_file):
            return False

        # initialize an empty file
        file_handler = FileHandler(file_path=file_path, password=password, salt=salt)
        file_handler.write_in_file(json.dumps([]))
        fsh.save_db()
        return file_handler

    def delete(self):
        """
        Delete a file.

        :return: None
        """
        fsh = FileStorageHelper()
        fsh.load_db()

        self.get_all_entries()  # check the master password
        self.delete_all_entries()  # make it empty

        fsh.delete_file(
            PasswordFile(file_path=self.file_path, salt=self.salt)  # removes the entry from the storage file
        )

        fsh.save_db()  # then save the db again.
        os.remove(self.file_path)  # removes file from the OS.

    def write_in_file(self, data):
        """
        Write data in file.

        :param data: data to write as a string
        :type data: string
        :return: None
        """
        with open(self.file_path, mode='wb') as f:
            f.write(EncryptionManager().encrypt_data(self.key, data))

    def decode_file(self):
        """
        Decode an encrypted password file.

        :return: the data contained in the file.
        :rtype: str
        """
        with open(self.file_path, mode='rb') as f:
            decrypted = EncryptionManager.decrypt_data(data=f.read(), key=self.key)
        return decrypted

    def add_entry(self, entry):
        """
        Add password entry to a file.

        :param entry: PasswordEntry
        :return: bool, signifying the success or not of the operation
        """
        stored_entries = json.loads(self.decode_file())
        decoded_stored_entries = [PasswordEntry.from_json(passw) for passw in stored_entries]

        for password in decoded_stored_entries:
            if password.name == entry.name:
                raise IndexError("Name already in the PasswordFile")
        stored_entries.append(entry.to_json())
        self.write_in_file(json.dumps(stored_entries))

    def get_all_entries(self):
        """
        Get all PasswordEntry from a PasswordFile.

        :return: list(PasswordEntry)
        """
        entries = json.loads(self.decode_file())
        return [PasswordEntry.from_json(s) for s in entries]

    def get_entry(self, entry_name):
        """
        Get one PasswordEntry from a PasswordFile.

        :param entry_name: exact name of the entry to look for.
        :return: PasswordEntry
        :raise IndexError:
        """
        entries = self.get_all_entries()
        for e in entries:
            if e.name == entry_name:
                return e
        IndexError("No such entry with this")

    def get_entry_starting_by(self, entry_name):
        """
        Get all entry starting with a given string.

        :param entry_name: str to search elements with.
        :return: list of corresponding PasswordEntry, might be empty.
        :rtype: list[PasswordEntry]
        """
        entries = self.get_all_entries()
        results = []
        for e in entries:
            if e.name.startswith(entry_name):
                results.append(e)

        if not results:
            info_msg("No corresponding name found 😕")
        return results

    def update(self, entry):
        """
        Update an entry.

        :param entry: The updated entry.
        :type entry: PasswordEntry
        :return: None
        """
        self.delete_entry(entry.name)
        self.add_entry(entry)

    def delete_entry(self, entry_name):
        """
        Delete an entry given its name.

        Side note: entry name is an Index and is unique to each PasswordEntry.

        :param entry_name: name of the entry to delete.
        :type entry_name: str
        :return: None
        :rtype: None
        :raise IndexError:
        """
        entries = self.get_all_entries()
        for e in entries:
            if e.name == entry_name:
                entries.remove(e)
                self.write_in_file(json.dumps([pwd.to_json() for pwd in entries]))
                ok_msg("Deletion successful")
                return True
        IndexError("Deletion failed. No such entry")

    def delete_all_entries(self):
        """
        Delete all PasswordEntry in a PasswordFile.

        :return: None
        :rtype: None
        """
        self.write_in_file(json.dumps([]))
