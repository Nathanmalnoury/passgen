#!/usr/bin/env python3

import configparser
import os
import sys


class Conf(object):

    def __init__(self):
        conf = Conf.read_conf()
        self.use_uppercase = conf.get("upper")
        self.use_spec_char = conf.get("spec_chars")
        self.use_digits = conf.get("digits")
        self.length = conf.get("length")
        self.show_password = conf.get("show_pass")
        self.copy_to_paper_clip = conf.get("paperclip")

    def get_uppercase(self):
        return self.use_uppercase

    def get_spec_char(self):
        return self.use_spec_char

    def get_digits(self):
        return self.use_digits

    def get_length(self):
        return self.length

    def get_show_password(self):
        return self.show_password

    def get_paperclip(self):
        return self.copy_to_paper_clip

    @staticmethod
    def read_conf():
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
