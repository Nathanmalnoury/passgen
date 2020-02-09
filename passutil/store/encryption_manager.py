"""Util class to deal with encryption."""
import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class EncryptionManager:
    """
    Help to deal with encryption.

    Only contains static methods, and it behaves like a collection of related and util functions.
    Contains function to :
    - generate key (from password or form password + salt)
    - encrypt and decrypt data
    """

    algorithm = hashes.SHA256
    length_kdf = 32
    iterations = 100000
    backend = default_backend()

    @staticmethod
    def _str_to_bytes(str_):
        return bytes(str_.encode("utf-8"))

    @staticmethod
    def _bytes_to_str(bytes_):
        return bytes_.decode(encoding='utf-8')

    @staticmethod
    def generate_new_key(password):
        """
        Generate a key from a given password.

        code from : https://cryptography.io/en/latest/fernet/#using-passwords-with-fernet

        :param password: password.py
        :type password: str
        :return: [key, salt]
        :rtype: list[bytes]
        """
        em = EncryptionManager
        bin_pass = em._str_to_bytes(password)
        salt = os.urandom(16)

        kdf = PBKDF2HMAC(
            algorithm=em.algorithm,
            length=em.length_kdf,
            salt=salt,
            iterations=em.iterations,
            backend=em.backend,
        )

        key = base64.urlsafe_b64encode(kdf.derive(bin_pass))
        return [key, salt]

    @staticmethod
    def generate_key(salt, password):
        """
        Generate a key, given a salt and password.

        :param salt: salt.
        :type salt: bytes
        :param password: password to use to generate key.
        :type password: str
        :return: key
        :rtype: bytes
        """
        em = EncryptionManager
        bin_pass = em._str_to_bytes(password)

        kdf = PBKDF2HMAC(
            algorithm=em.algorithm,
            length=em.length_kdf,
            salt=salt,
            iterations=em.iterations,
            backend=em.backend,
        )
        key = base64.urlsafe_b64encode(kdf.derive(bin_pass))

        return key

    @staticmethod
    def encrypt_data(key, data):
        """
        Encrypt data.

        :param key: key to encrypt the data
        :type key: bytes
        :param data: data to encrypt.
        :type data: str
        :return: bytes
        """
        fernet = Fernet(key)
        return fernet.encrypt(bytes(data, 'utf8'))

    @staticmethod
    def decrypt_data(key, data):
        """
        Decrypt data using a key.

        :raise cryptography.fernet.InvalidToken:
        :param key: key of encryption.
        :type key: bytes
        :param data: data to decrypt.
        :type data: bytes
        :return: decrypted data, decoded using utf-8
        :rtype: str
        """
        fernet = Fernet(key)
        return fernet.decrypt(data).decode('utf-8')
