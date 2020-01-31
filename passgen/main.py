#!/usr/bin/env python3
import random


def password_generator(length, characters):
    def select_char(list_characters):
        return list_characters[random.randrange(len(list_characters))]

    characters_list = list(characters)
    return "".join([select_char(characters_list) for i in range(length)])
