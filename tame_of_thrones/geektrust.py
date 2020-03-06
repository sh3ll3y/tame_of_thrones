""" The Tame Of Thrones CLI. """


import cryptography as crypto
import input_reader as ir
import output as op
import string_handler as sh
import sys

from config import config_data


def print_output(home_kingdom_name, ally_kingdoms, num_of_allies_required):
    output = op.Outputter(
        home_kingdom_name,
        ally_kingdoms,
        num_of_allies_required)
    output.print_standard_output()


def main():
    input_file = sys.argv[1]
    home_kingdom = config_data.get("home_kingdom")
    home_kingdom_name = home_kingdom.get("name")
    num_of_allies_required = home_kingdom.get("num_of_kingdoms_to_win")
    ally_kingdoms = []
    emblems = config_data.get("emblems")
    messages = ir.read_input(input_file)

    if ir.validate_format(config_data.get("std_input_format"), messages):
        if len(messages) < num_of_allies_required:
            print_output(
                home_kingdom_name,
                ally_kingdoms,
                num_of_allies_required)
        for msg in messages:
            kingdom, secret_msg = msg.split(" ", 1)
            emblem_name = emblems.get(kingdom)
            cipher_key = len(emblem_name)
            crypto_obj = crypto.SeasarCipher(cipher_key)
            # We are encrypting the emblem name and comparing
            # it with already encrypted msg instead of decrypting
            # the longer secret msg and comparing it with emblem name.
            encrypted_str = crypto_obj.encrypt(emblem_name.upper())
            secret_msg = secret_msg.replace(" ", "")
            correct_msg = sh.contains_sub_str_letters(
                secret_msg, encrypted_str)
            if correct_msg:
                ally_kingdoms.append(kingdom)
        print_output(home_kingdom_name, ally_kingdoms, num_of_allies_required)


if __name__ == "__main__":
    main()
