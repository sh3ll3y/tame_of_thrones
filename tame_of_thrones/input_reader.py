"""Module to read and validate inputs."""


import re


class InputError(BaseException):
    pass


class InputFormatError(InputError):
    pass


def read_input(filename):
    """Reads the input of the file.

    Args:
        filename (string): Path of the file.

    Returns:
        list: List of rows read from file.

    """
    with open(filename, "r") as fp:
        data = fp.readlines()
    return [row.strip() for row in data]


def validate_format(regex, rows):
    """Validates each row against regex.

    Args:
        regex (string): Regular expression
        rows (list): List of strings

    Returns:
        list of dictionaries with kingdom as keys and secret message as values.

    """
    lines = []
    for row in rows:
        line = re.match(regex, row)
        if not line:
            raise InputFormatError("Input format error.")
        lines.append(line.groupdict())
    return lines
