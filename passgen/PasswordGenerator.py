#! /usr/bin/env python3

import string
from random import randrange


class PasswordGenerator:
    def __init__(self, length):
        self.allowed_chars = list(string.ascii_lowercase)
        self.length = length

    def use_uppercase(self, use=True):
        if use:
            self.allowed_chars += list(string.ascii_uppercase)

    def use_digits(self, use=True):
        if use:
            self.allowed_chars += list(string.digits)

    def use_special_characters(self, use=True):
        if use:
            self.allowed_chars += list(string.punctuation)

    def _select_one_character(self):
        return self.allowed_chars[randrange(len(self.allowed_chars))]

    def generate(self):
        return "".join([self._select_one_character() for i in range(self.length)])
