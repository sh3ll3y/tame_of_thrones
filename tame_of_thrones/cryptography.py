""" Class to hold cryptograhic methods. """


class SeasarCipher(object):
    """Implements Seasar Cipher."""

    NUM_OF_ENGLISH_LETTERS = 26
    MIN_ORDINAL = ord('A')
    MAX_ORDINAL = ord('Z')


    def __init__(self, cipher_key):
        self.cipher_key = cipher_key

    def decrypt(self):
        pass

    def encrypt(self, message):
        """Encryps the message.

        Args:
            message(str): input message

        Returns:
            string: encrypted message in string format.

        """
        encrypted_msg = ""
        for char in message:
            ordinal = ord(char)
            num_of_shifts = self.cipher_key % self.NUM_OF_ENGLISH_LETTERS
            new_ordinal = ordinal + num_of_shifts
            if new_ordinal > self.MAX_ORDINAL:
                new_ordinal = (self.MIN_ORDINAL - 1) + \
                    (new_ordinal - self.MAX_ORDINAL)
            encrypted_msg += chr(new_ordinal)

        return encrypted_msg
