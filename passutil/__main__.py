"""
__main__ script, responsible for cli calls.

Distributes the call between the two click_commands.py from modules generator and store.
"""
import click

from passutil.generator import click_commands as generator_commands
from passutil.generator.conf import click_commands as group_conf
from passutil.store import click_commands as group_store

HELP_STR = """
passutil, a password generator / password manager built using Python3.7.

tree structure of the commands :

passutil
    |
    | - info : shows this message
    |
    | - generate   Generate a password. Use the 'conf_passgen.ini' as default.
    |
    | - conf       Manage the default configuration
    |   |
    |   | - show :   show the current state of the file.
    |   |
    |   | - modify : modify the conf
    |   |   |
    |   |   | - copy-to-paper-clip  Change the default value of copy_to_paperclip.
    |   |   | - digits              Change the default value of use_digits.
    |   |   | - length              Change the default value of length.
    |   |   | - show-password       Change the default value of show_password.
    |   |   | - spec-char           Change the default value of use_special_chars.
    |   |   | - uppercase           Change the default value of use_uppercase.
    |
    | - store   Manage encrypted files and passwords in them.
    |   |
    |   |- list-files  List all files encrypted using this tool.
    |   |
    |   |- file        Manage encrypted files
    |   |   |
    |   |   |- delete  Delete a file
    |   |   |- new     Create a new file
    |   |
    |   |- password    Manage password inside an encrypted file
    |   |   |
    |   |   |-add      Get add a new password in an encrypted file.
    |   |   |-delete   Get delete a password in an encrypted file.
    |   |   |-get      Get one or several passwords in an encrypted file.
    |   |   |-get-all  Get all password in an encrypted file.

Developed by Nathan Malnoury, n.malnoury@gmail.com
"""


@click.group()
def passutil():
    """Passutil, a basic password generator and password manager, using 🐍."""
    pass


@passutil.command(help="more inforation about this tool.")
def info():
    """Display more information about passutil."""
    click.echo(HELP_STR)


passutil.add_command(group_store.store)
passutil.add_command(generator_commands.generate)
passutil.add_command(group_conf.conf)

if __name__ == "__main__":
    passutil()
