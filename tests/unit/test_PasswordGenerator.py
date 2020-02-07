import string
import unittest
from random import randint

from ws.passgen.password_generator import PasswordGenerator


def is_in(list_a, list_b):
    """
    Check if every item of list a is in list b.

    :param list_a: list
    :param list_b: list
    :return: bool
    """
    intersection = [a for a in list_a if a in list_b]
    return intersection == list_a


class TestPasswordGenerator(unittest.TestCase):
    def setUp(self):
        self.length = randint(0, 10000)
        self.password_generator = PasswordGenerator(self.length)

    def test_default_chars(self):
        """
        Test the original allowed characters.

        :return: None
        """
        self.assertTrue(self.password_generator.allowed_chars == list(string.ascii_lowercase))

    def test_add_uppercase_characters(self):
        """
        Test that use_uppercase works as expected.

        :return: None
        """
        self.password_generator.use_uppercase(True)
        self.assertTrue(is_in(list(string.ascii_uppercase), self.password_generator.allowed_chars))

    def test_add_digits(self):
        """
        Test that use_digits works.

        :return:
        """
        self.password_generator.use_digits(True)
        self.assertTrue(is_in(list(string.digits), self.password_generator.allowed_chars))

    def test_add_special_characters(self):
        """
        Test that use_digits works.

        :return:
        """
        self.password_generator.use_special_characters(True)
        self.assertTrue(is_in(list(string.punctuation), self.password_generator.allowed_chars))

    def test_generate_1(self):
        """
        First case scenario.
        :return:
        """
        passw = self.password_generator.generate()
        self.assertTrue(len(passw) == self.length)
        self.assertTrue(is_in(list(passw), string.ascii_lowercase))

    def test_generate_2(self):
        """
        First case scenario.
        :return:
        """
        self.password_generator.use_special_characters()
        self.password_generator.use_digits()
        self.password_generator.use_uppercase()
        chars = list(string.ascii_letters + string.punctuation + string.digits)

        passw = self.password_generator.generate()
        self.assertTrue(len(passw) == self.length)
        self.assertTrue(is_in(list(passw), chars))


if __name__ == '__main__':
    unittest.main()
