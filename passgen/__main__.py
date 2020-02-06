#! /usr/bin/env python3
"""Parses the flags used when the module was called."""
import argparse

from Conf import Conf
from request_handler import handle_request

conf = Conf()

parser = argparse.ArgumentParser(
    description="simple password generator. You can use the file `conf.ini` to change the default behaviour")

parser.add_argument("-l", action="store", dest="length", default=conf.get_length(), type=int,
                    help="set up the length of the password")

parser.add_argument("--use-special-chars", action="store_true", dest="use_spec_chars",
                    help="use this to use special characters", default=conf.get_spec_char())

parser.add_argument("--no-upper", action="store_false", dest="use_upper_case",
                    help="use this flag to prevent from using uppercase letter", default=conf.get_uppercase())

parser.add_argument("--no-digit", action="store_false", dest="use_digits",
                    help="use this flag to prevent from using digits", default=conf.get_digits())

parser.add_argument("--show-password", action="store_true", dest="show_password",
                    help="use this flag to show the password", default=conf.get_show_password())

parser.add_argument("--copy-to-paperclip", action="store_true", dest="copy_to_paperclip",
                    help="use this flag to copy the password to the paperclip", default=conf.get_paperclip())

args = parser.parse_args()

handle_request(args)

exit()
