import click

from generator import click_commands as generator_commands
from store import click_commands as group_store


@click.group()
def passutil():
    pass


passutil.add_command(group_store.store)
passutil.add_command(generator_commands.generate)

if __name__ == "__main__":
    passutil()
