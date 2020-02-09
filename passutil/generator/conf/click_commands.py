"""CLI tool to modify the conf.ini file."""
import click

from passutil.click_utils import ok_msg
from passutil.generator.conf.conf import Conf

CONF_PATH = "./data/conf_passgen.ini"


@click.group(help="Manage the default configuration")
@click.pass_context
def conf(ctx):
    """Subgroup that modify the default configuration."""
    conf_ = Conf()
    conf_.read_conf(CONF_PATH)
    ctx.obj = conf_


@conf.command(help="Show the current default configuration")
@click.pass_context
def show(ctx):
    """Show the current default configuration."""
    print(ctx.obj)


@conf.group(help="Change the default configuration")
@click.pass_context
def modify(ctx):
    """Subgroup that modify the default configuration."""
    pass


@modify.command()
@click.pass_context
@click.argument('new_value', type=bool)
@click.confirmation_option(prompt="Are you sure you want to modify the default configuration ?")
def uppercase(ctx, new_value):
    """Change the default value of use_uppercase."""
    ctx.obj.use_uppercase = new_value
    ctx.obj.update_conf(CONF_PATH)
    ok_msg("Conf updated")


@modify.command()
@click.pass_context
@click.argument('new_value', type=bool)
@click.confirmation_option(prompt="Are you sure you want to modify the default configuration ?")
def spec_char(ctx, new_value):
    """Change the default value of use_special_chars."""
    ctx.obj.use_spec_char = new_value
    ctx.obj.update_conf(CONF_PATH)
    ok_msg("Conf updated")


@modify.command()
@click.pass_context
@click.argument('new_value', type=bool)
@click.confirmation_option(prompt="Are you sure you want to modify the default configuration ?")
def digits(ctx, new_value):
    """Change the default value of use_digits."""
    ctx.obj.use_digits = new_value
    ctx.obj.update_conf(CONF_PATH)
    ok_msg("Conf updated")


@modify.command()
@click.pass_context
@click.argument('new_value', type=int)
@click.confirmation_option(prompt="Are you sure you want to modify the default configuration ?")
def length(ctx, new_value):
    """Change the default value of length."""
    ctx.obj.length = new_value
    ctx.obj.update_conf(CONF_PATH)
    ok_msg("Conf updated")


@modify.command()
@click.pass_context
@click.argument('new_value', type=bool)
@click.confirmation_option(prompt="Are you sure you want to modify the default configuration ?")
def show_password(ctx, new_value):
    """Change the default value of show_password."""
    ctx.obj.show_password = new_value
    ctx.obj.update_conf(CONF_PATH)
    ok_msg("Conf updated")


@modify.command()
@click.pass_context
@click.argument('new_value', type=bool)
@click.confirmation_option(prompt="Are you sure you want to modify the default configuration ?")
def copy_to_paper_clip(ctx, new_value):
    """Change the default value of copy_to_paperclip."""
    ctx.obj.copy_to_paper_clip = new_value
    ctx.obj.update_conf(CONF_PATH)
    ok_msg("Conf updated")
