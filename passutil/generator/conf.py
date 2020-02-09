#!/usr/bin/env python3
"""Script responsible for handling the conf fileDB."""

import configparser
import os
import sys


class Conf(object):
    """Util class that reads the conf fileDB."""

    def __init__(self):
        """
        Initialise the instance.

        This reads the conf fileDB and then store the defaults values in the instance.
        """
        self.use_uppercase = None
        self.use_spec_char = None
        self.use_digits = None
        self.length = None
        self.show_password = None
        self.copy_to_paper_clip = None

    def get_uppercase(self):
        """
        Get self.uppercase.

        :return:
        """
        return self.use_uppercase

    def get_spec_char(self):
        """
        Get self.use_spec_char.

        :return:
        """
        return self.use_spec_char

    def get_digits(self):
        """
        Get self.use_digits.

        :return:
        """
        return self.use_digits

    def get_length(self):
        """
        Get self.length.

        :return:
        """
        return self.length

    def get_show_password(self):
        """
        Get self.show_password.

        :return:
        """
        return self.show_password

    def get_paperclip(self):
        """
        Get self.copy_to_paper_clip.

        :return:
        """
        return self.copy_to_paper_clip

    def read_conf(self, filename):
        """
        Read conf fileDB and store the default values in a dictionary.

        :param filename: name of the conf fileDB
        :type filename: str
        :return: dict with the default values
        :rtype: dict
        """
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(sys.argv[0]), filename))
        defaults = config["PASSWORD_GENERATOR"]
        self.use_uppercase = defaults.getboolean("use_uppercase")
        self.use_spec_char = defaults.getboolean("use_special_chars")
        self.use_digits = defaults.getboolean("use_digits")
        self.length = defaults.get("length")
        self.show_password = defaults.getboolean("show_password")
        self.copy_to_paper_clip = defaults.getboolean("copy_to_paperclip")
