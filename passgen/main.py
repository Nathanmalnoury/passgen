#!/usr/bin/env python3

import random
import string

import pyperclip


def password_generator(length, characters):
    def select_char(list_characters):
        return list_characters[random.randrange(len(list_characters))]

    characters_list = list(characters)
    return "".join([select_char(characters_list) for i in range(length)])


def handle_request(args):
    chars = string.ascii_lowercase

    if args.use_upper_case is True:
        chars += string.ascii_uppercase

    if args.use_digits is True:
        chars += string.digits

    if args.use_spec_chars is True:
        chars += string.punctuation

    password = password_generator(args.length, chars)
    print("password of length {}".format(args.length))

    if args.copy_to_paperclip:
        pyperclip.copy(password)
        print("password copied in the paperclip")

    if args.show_password:
        print(password)
