"""Some functions to output message in the terminal faster."""
import click

ERROR_MESSAGE = "❌ Something went wrong: "


def info_msg(text):
    """Echo a blue message, signifying that it is a piece of information."""
    click.echo(click.style(text, fg='blue'))


def ok_msg(text):
    """Echo a green message, meaning success of an operation."""
    click.echo(click.style("✔ " + text, fg='green'))


def err_msg(text):
    """
    Echo a red message, meaning failure of an operation.

    :param text: either str or Exception, to print the error message
    :type text: str or Exception
    """
    if type(text) == str:
        click.echo(click.style(ERROR_MESSAGE + text, fg='red'))
    elif isinstance(text, Exception):
        click.echo(click.style(ERROR_MESSAGE + text.__str__(), fg='red'))
