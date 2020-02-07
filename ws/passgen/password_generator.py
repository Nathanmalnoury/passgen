#! /usr/bin/env python3
"""Core class, used to generate passwords."""
import string
from random import randrange


class PasswordGenerator:
    """Class responsible for creating passwords."""

    def __init__(self, length):
        """
        Initialise an instance of PasswordGenerator.

        :param length: length of the wanted password.py
        :type length: int
        """
        self.allowed_chars = list(string.ascii_lowercase)
        self.length = length

    def use_uppercase(self, use=True):
        """
        Set whether or not to use uppercase characters in password.py.

        :type use: bool
        :return: None
        """
        if use:
            self.allowed_chars += list(string.ascii_uppercase)

    def use_digits(self, use=True):
        """
        Set whether or not to use digits in password.py.

        :type use: bool
        :return: None
        """
        if use:
            self.allowed_chars += list(string.digits)

    def use_special_characters(self, use=True):
        """
        Set whether or not to use special characters in password.py.

        :type use: bool
        :return: None
        """
        if use:
            self.allowed_chars += list(string.punctuation)

    def _select_one_character(self):
        """
        Private function, select one character randomly in the allowed characters.

        :return: one character
        :rtype: str
        """
        return self.allowed_chars[randrange(len(self.allowed_chars))]

    def generate(self):
        """
        Generate password.py with the allowed characters.

        :return: str of length self.length
        :rtype: str
        """
        return "".join([self._select_one_character() for i in range(self.length)])
