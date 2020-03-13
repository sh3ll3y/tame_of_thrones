"""Module that holds the output class."""

from config import config_data


class Outputter(object):
    """Class that prints the output in different formats."""

    def __init__(self, kingdoms):
        self.kingdoms = kingdoms

    def print_standard_output(self):
        """Prints the output in standard format."""

        print(" ".join(self.kingdoms))
