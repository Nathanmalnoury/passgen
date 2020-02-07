import json

import click
import pathlib
import pprint

from ws.passstore.password.password import PasswordEntry
from ws.passstore.fileDB.fileStorageHelper import FileStorageHelper
from ws.passstore.file.file_handler import FileHandler


@click.group()
def cli():
    pass

@cli.group()
def file():
    pass

@file.command()
@click.option('--path', help='Creates a new encoded file. Do not support `~/` ', prompt=True)
@click.option('--master-password', prompt=True, hide_input=True, confirmation_prompt=True)
def new(path, master_password):
    FileHandler.create_file(path, master_password)


@file.command()
def list():
    fsh = FileStorageHelper()
    fsh.load_db()
    pprint.pprint(fsh.get_all_files(), indent=4)

@cli.group()
def password():
    pass


@password.command()
@click.option('--path', help='file to read', prompt=True)
@click.option('--master-password', prompt=True, hide_input=True)
def get_all(path, master_password):
    salt = FileStorageHelper.get_salt_from_path(path)
    fh = FileHandler(file_path=path, password=master_password, salt=salt)
    entries = fh.get_all_entries()
    [pprint.pprint(json.loads(pwd.to_json()), compact=False, indent=2) for pwd in entries]


@password.command()
@click.option('--path', help='file to read', prompt=True)
@click.option('--master-password', prompt=True, hide_input=True)
@click.option('--name', prompt=True, help='Fullname or the start of the name to find')
@click.option('--absolute', is_flag=True, default=False, help='Only returns the perfect match')
def get(path, master_password, name, absolute):
    salt = FileStorageHelper.get_salt_from_path(path)
    fh = FileHandler(file_path=path, password=master_password, salt=salt)
    if absolute:
        entries = [fh.get_entry(name)]
    else:
        entries = fh.get_entry_starting_by(name)

    [pprint.pprint(json.loads(pwd.to_json()), compact=False, indent=2) for pwd in entries]


@password.command()
@click.option('--path', help='path to the password file.', prompt=True)
@click.option('--master-password', prompt=True, hide_input=True)
@click.option('--name', help='name to store', prompt=True)
@click.option('--username', help='username to store', prompt=True)
@click.option('--password', prompt=True)
def add(path, master_password, name, username, password):
    salt = FileStorageHelper.get_salt_from_path(path)
    fh = FileHandler(file_path=path, password=master_password, salt=salt)
    fh.add_entry(PasswordEntry(username=username, password=password, name=name))


@password.command()
@click.option('--path', help='path to the password file.', prompt=True)
@click.option('--master-password', prompt=True, hide_input=True)
@click.option('--name', help='name of the entry to delete', prompt=True)
def delete(path, master_password, name):
    salt = FileStorageHelper.get_salt_from_path(path)
    fh = FileHandler(file_path=path, password=master_password, salt=salt)
    fh.delete_entry(entry_name=name)


if __name__ == '__main__':
    cli()
