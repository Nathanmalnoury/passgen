#!/usr/bin/env python3
"""Script responsible for handling the conf file."""

import configparser
import os
import sys


class Conf(object):
    """Util class that reads the conf file."""

    def __init__(self):
        """
        Initialise the instance.

        This reads the conf file and then store the defaults values in the instance.
        """
        conf = Conf.read_conf()
        self.use_uppercase = conf.get("upper")
        self.use_spec_char = conf.get("spec_chars")
        self.use_digits = conf.get("digits")
        self.length = conf.get("length")
        self.show_password = conf.get("show_pass")
        self.copy_to_paper_clip = conf.get("paperclip")

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

    @staticmethod
    def read_conf():
        """
        Read conf file and store the default values in a dictionary.

        :return: dict with the default values
        :rtype: dict
        """
        config = configparser.ConfigParser()
        config.read(os.path.join(sys.argv[0], "../conf.ini"))
        defaults = config["DEFAULT"]

        return {
            "length": defaults.get("length"),
            "upper": defaults.getboolean("use_uppercase"),
            "spec_chars": defaults.getboolean("use_special_chars"),
            "digits": defaults.getboolean("use_digits"),
            "show_pass": defaults.getboolean("show_password"),
            "paperclip": defaults.getboolean("copy_to_paperclip")
        }
