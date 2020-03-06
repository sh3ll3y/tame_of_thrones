"""Module that holds the output class."""


class Outputter(object):
    """Class that print the output in different formats."""

    def __init__(self, home_kingdom, allies, num_of_allies_required=0):
        self.home_kingdom = home_kingdom
        self.allies = allies
        self.num_of_allies_required = num_of_allies_required

    def print_standard_output(self):
        """Prints the output in standard format."""

        if len(self.allies) < self.num_of_allies_required:
            print('NONE')
        else:
            print(self.home_kingdom, ' '.join(self.allies))
