import cryptography as crypto

from config import config_data
import string_handler as sh


class Kingdom(object):

    def __init__(self, name):
        self.name = name
        self.emblem = config_data["emblems"][name.upper()]
        self.cipher_key = len(self.emblem)
        self.allies = []

    def send_secret_msg(self, messages):
        """ Sends the secret message to the respective kingdom.
        
        Args:
            message(list): list of dictionaries with kingdom as keys and secret message as values.

        Returns:
            list of allies.
        
        """
        for msg in messages:
            kingdom = msg.get("name")
            secret_msg = msg.get("msg")
            kngdm = Kingdom(kingdom)
            ally = kngdm.receive_secret_msg(secret_msg)
            if ally:
                if kingdom not in self.allies:
                    self.allies.append(kingdom)
        return self.allies

    def receive_secret_msg(self, msg):
        """ Receives the secret message from other kindgoms.

        Args:
            msg(str): encrypted secret message.

        Returns:
            bool: True if secret message contains all the letters of the emblem, else False.

        """
        crypto_obj = crypto.SeasarCipher(self.cipher_key)
        encrypted_emblem = crypto_obj.encrypt(self.emblem.upper())
        secret_msg = msg.replace(" ", "")
        return sh.contains_sub_str_letters(secret_msg, encrypted_emblem)

    def form_rule(self):
        """ Tries to form rule with the allies.

        Returns:
            list: home kingdom followed by sufficient allies in a list, else ["NONE"].

        """
                
        if len(self.allies) >= config_data["num_of_allies_to_win"]:
            return [self.name] + self.allies
        return ["NONE"]
