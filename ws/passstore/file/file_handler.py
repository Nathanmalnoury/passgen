import json

from ws.passstore.encryption_manager import EncryptionManager
from ws.passstore.fileDB.fileStorageHelper import FileStorageHelper
from ws.passstore.fileDB.password_file import PasswordFile
from ws.passstore.password.password import PasswordEntry


class FileHandler:
    def __init__(self, file_path, password, salt=None):

        self.file_path = file_path
        self.salt = salt
        self.key = EncryptionManager.generate_key(salt=salt, password=password)

    @staticmethod
    def create_file(file_path, password):
        fsh = FileStorageHelper()
        fsh.load_db()

        key, salt = EncryptionManager().generate_new_key(password=password)
        pass_file = PasswordFile(filepath=file_path, salt=salt)

        if not pass_file.is_complete():
            print("Something is wrong. Log to be detailed")
            return False

        if not fsh.add_file(pass_file):
            return False

        # initialize an empty file
        file_handler = FileHandler(file_path=file_path, password=password, salt=salt)
        file_handler.write_in_file(json.dumps([]))
        fsh.save_db()

        print("Password file Created")
        return file_handler

    def write_in_file(self, data):
        with open(self.file_path, mode='wb') as f:
            f.write(EncryptionManager().encrypt_data(self.key, data))

    def decode_file(self):
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
                raise IndexError("Name already in file")
        stored_entries.append(entry.to_json)
        self.write_in_file(json.dumps(stored_entries))

    def get_all_entries(self):
        entries = json.loads(self.decode_file())
        return [PasswordEntry.from_json(s) for s in entries]

    def get_entry(self, entry_name):
        entries = self.get_all_entries()
        for e in entries:
            if e.name == entry_name:
                return e
        IndexError("No such entry with this")

    def get_entry_starting_by(self, entry_name):
        entries = self.get_all_entries()
        results = []
        for e in entries:
            if e.name.startswith(entry_name):
                results.append(e)
        if not e:
            print("No corresponding name found")
        return results

    def update(self, entry):
        self.delete_entry(entry.name)
        self.add_entry(entry)

    def delete_entry(self, entry_name):
        entries = self.get_all_entries()
        for e in entries:
            if e.name == entry_name:
                entries.remove(e)
                self.write_in_file(json.dumps([pwd.to_json() for pwd in entries]))
                print("Deletion successful")
                return True
        IndexError("Deletion failed. No such entry")

    def delete_all_entries(self):
        self.write_in_file(json.dumps([]))


if __name__ == '__main__':
    file_path = "/home/nathan/test4.psw"
    password = "test123"
    fsh = FileStorageHelper()
    fsh.load_db()
    salt = fsh.get_file(file_path).salt
    # print(salt)

    file_handler = FileHandler(file_path=file_path, password=password, salt=salt)
    # print(file_handler.get_all_entries())

    # file_handler = FileHandler.create_file(file_path=file_path, password=password)

    passw = PasswordEntry(username="nathan", name="test856kk", password="password123")
    # file_handler.add_entry(passw)

    entries_ = file_handler.get_all_entries()
    [print(e) for e in entries_]
