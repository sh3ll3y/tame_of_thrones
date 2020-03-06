"""Holds test cases for cyptography classes."""

import cryptography as crypto  # pylint: disable=import-error
import unittest


class TestSeasar(unittest.TestCase):
    """Test of SeasarCypher."""

    def test_if_a_string_is_encrypted_correctly_based_on_cipher_key(self):
        input_string = "GEEKZ"
        crypto_obj = crypto.SeasarCipher(5)
        expected = "LJJPE"
        actual = crypto_obj.encrypt(input_string)
        self.assertEqual(expected, actual)
