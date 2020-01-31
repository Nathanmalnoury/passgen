#! /usr/bin/env python3

import argparse
import configparser
import string
import pyperclip
import sys
import os
from main import password_generator

config = configparser.ConfigParser()
config.read(os.path.join(sys.argv[0], "../conf.ini"))
defaults = config["DEFAULT"]

def_length = defaults["length"]
def_upper = defaults["use_uppercase"]
def_spec_chars = defaults["use_special_chars"]
def_digits = defaults["use_digits"]


parser = argparse.ArgumentParser(description="simple password generator")
parser.add_argument("-l", action="store", dest="length", default=def_length, type=int,
                    help="set up the length of the password")

parser.add_argument("--use-special-chars", action="store_true", dest="use_spec_chars",
                    help="use this to use special characters", default=def_spec_chars)

parser.add_argument("--no-upper", action="store_false", dest="use_upper_case",
                    help="use this flag to prevent from using uppercase letter", default=def_upper)

parser.add_argument("--no-digit", action="store_false", dest="use_digits",
                    help="use this flag to prevent from using digits", default=def_digits)
# lower and upper
# unicode

args = parser.parse_args()

chars = string.ascii_lowercase
if args.use_upper_case:
    chars += string.ascii_uppercase
if args.use_digits:
    chars += string.digits
if args.use_spec_chars:
    chars += string.punctuation

passw = password_generator(args.length, chars)
pyperclip.copy(passw)
print("password of length {}".format(args.length))
print("password copied in the paperclip")
exit()
