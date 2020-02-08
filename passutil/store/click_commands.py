import json
import pprint

import click
from cryptography.fernet import InvalidToken

from store.file.file_handler import FileHandler
from store.fileDB.fileStorageHelper import FileStorageHelper
from store.password.password import PasswordEntry

ERROR_MESSAGE = "❌ Something went wrong: "


def ok_msg(text):
    click.echo(click.style(text, fg='green'))


def err_msg(text):
    click.echo(click.style(ERROR_MESSAGE + text, fg='red'))


@click.group(help='Manage encrypted files and passwords in them.')
def store():
    pass


@store.group(help='Manage encrypted files')
@click.pass_context
@click.option('--path', help='Creates a new encoded file. Do not support "~"', prompt=True)
def file(ctx, path):
    ctx.obj = {'path': path}


@file.command(help='Create a new file')
@click.option('--master-password', help='Master Password', prompt=True, hide_input=True, confirmation_prompt=True)
@click.pass_context
def new(ctx, master_password):
    try:
        FileHandler.create_file(file_path=ctx.obj.get('path'), password=master_password)
        ok_msg("Password file Created 📝")

    except IsADirectoryError:
        err_msg('"{}" is a directory.'.format(ctx.obj.get('path')))
        exit()

    except FileExistsError:
        err_msg("file already exists.")
        exit()

    except Exception as e:
        err_msg(e.__str__())


@file.command('delete',  help='Delete a file')
@click.option('--master-password', help='Master Password', prompt=True, hide_input=True)
@click.pass_context
def delete_file(ctx, master_password):
    try:
        FileHandler.delete(file_path=ctx.obj.get('path'), password=master_password)
        ok_msg("File successfully deleted.")
    except FileNotFoundError:
        err_msg("No such file '{}'".format(ctx.obj.get('path')))
        exit()
    except InvalidToken:
        err_msg("Wrong password.")
        exit()


@store.command(help='List all files encrypted using this tool.')
def list_files():
    fsh = FileStorageHelper()
    fsh.load_db()
    pprint.pprint(fsh.get_all_files(), indent=4)


@store.group(help="Manage password inside an encrypted file")
@click.option('--path', help='file to read', prompt=True)
@click.option('--master-password', prompt=True, hide_input=True)
@click.pass_context
def password(ctx, path, master_password):
    """

    :type ctx: click.core.Context
    :param path:
    :param master_password:
    :return:
    """
    print(ctx, type(ctx))
    ctx.obj = {'path': path, 'master_password': master_password}


@password.command()
@click.pass_context
def get_all(ctx):
    path = ctx.obj.get("path")
    salt = FileStorageHelper.get_salt_from_path(path)
    try:
        fh = FileHandler(file_path=path, password=ctx.obj.get("master_password"), salt=salt)
        entries = fh.get_all_entries()
        [pprint.pprint(json.loads(pwd.to_json()), compact=False, indent=2) for pwd in entries]
    except InvalidToken:
        err_msg("Wrong password.")
    except FileNotFoundError:
        err_msg("File not found")
    except IndexError:
        err_msg("Path not found in the storage file.")


@password.command()
@click.pass_context
@click.option('--name', prompt=True, help='Fullname or the start of the name to find')
@click.option('--absolute', is_flag=True, default=False, help='Only returns the perfect match')
def get(ctx, name, absolute):
    path = ctx.obj.get("path")
    salt = FileStorageHelper.get_salt_from_path(path)
    fh = FileHandler(file_path=path, password=ctx.obj.get("master_password"), salt=salt)
    if absolute:
        entries = [fh.get_entry(name)]
    else:
        entries = fh.get_entry_starting_by(name)

    [pprint.pprint(json.loads(pwd.to_json()), compact=False, indent=2) for pwd in entries]


@password.command()
@click.pass_context
@click.option('--name', help='name to store', prompt=True)
@click.option('--username', help='username to store', prompt=True)
@click.option('--password', prompt=True)
def add(ctx, name, username, password):
    path = ctx.obj.get("path")
    salt = FileStorageHelper.get_salt_from_path(path)
    fh = FileHandler(file_path=path, password=ctx.obj.get("master_password"), salt=salt)
    fh.add_entry(PasswordEntry(username=username, password=password, name=name))


@password.command()
@click.option('--name', help='name of the entry to delete', prompt=True)
def delete(ctx, name):
    path = ctx.obj.get("path")
    salt = FileStorageHelper.get_salt_from_path(path)
    fh = FileHandler(file_path=path, password=ctx.obj.get("master_password"), salt=salt)
    fh.delete_entry(entry_name=name)
