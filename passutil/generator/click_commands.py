#! /usr/bin/env python3
"""Parses the flags used when the module was called."""
import sys

import click
import pyperclip

from generator.conf import Conf
from generator.password_generator import PasswordGenerator

conf = Conf()
print(sys.argv[0])
conf.read_conf("./conf.ini")


@click.command()
@click.option('--length', '-l', default=conf.get_length(), type=int,
              help='set up the length of the password')
@click.option('--special-chars', is_flag=True, default=conf.get_spec_char(),
              help='use this to use special characters')
@click.option("--no-upper", is_flag=True, default=conf.get_uppercase(),
              help="use this flag to prevent from using uppercase letter")
@click.option("--no-digit", is_flag=True, default=conf.get_digits(),
              help="use this flag to prevent from using digits")
@click.option("--show-password", is_flag=True, default=conf.get_show_password(),
              help="show the generated password in the command line")
@click.option("--copy-to-paperclip", is_flag=True, default=conf.get_paperclip(),
              help="use this flag to copy the password to the paperclip")
def generate(length, special_chars, no_upper, no_digit, show_password, copy_to_paperclip):
    print("🔒 Password Generator 🔒")
    pwg = PasswordGenerator(length=length)
    pwg.use_digits(no_digit)
    pwg.use_uppercase(no_upper)
    pwg.use_special_characters(special_chars)
    password = pwg.generate()
    if show_password:
        print(password)
    if copy_to_paperclip:
        pyperclip.copy(password)
        print("📎 copied to paperclip")
