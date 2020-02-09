"""
__main__ script, responsible for cli calls.

Distributes the call between the two click_commands.py from modules generator and store.
"""
import click

from generator import click_commands as generator_commands
from store import click_commands as group_store


@click.group()
def passutil():
    """Passutil, a basic password generator and password manager, using 🐍."""
    pass


passutil.add_command(group_store.store)
passutil.add_command(generator_commands.generate)

if __name__ == "__main__":
    passutil()
