#!/usr/bin/env python3

import pyperclip

from PasswordGenerator import PasswordGenerator


def handle_request(args):
    password_generator = PasswordGenerator(args.length)
    print("password of length {}".format(args.length))

    password_generator.use_uppercase(use=args.use_upper_case)
    password_generator.use_digits(use=args.use_digits)
    password_generator.use_special_characters(args.use_spec_chars)

    password = password_generator.generate()

    if args.copy_to_paperclip:
        pyperclip.copy(password)
        print("password copied in the paperclip")

    if args.show_password:
        print(password)
