"""The Tame Of Thrones CLI."""

import input_reader as ir
import output as op
import sys

from config import config_data
from kingdom import Kingdom


def main():
    input_file = sys.argv[1]
    data = ir.read_input(input_file)
    messages = ir.validate_format(config_data.get("std_input_format"), data)
    home_kingdom = config_data.get("home_kingdom")
    home_kngdm_obj = Kingdom(home_kingdom)
    home_kngdm_obj.send_secret_msg(messages)
    allies = home_kngdm_obj.form_rule()
    output = op.Outputter(allies)
    output.print_standard_output()


if __name__ == "__main__":
    main()
