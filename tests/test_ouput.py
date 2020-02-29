"""Test cases to print output."""

import output as op # pylint: disable=import-error
import unittest

from io import StringIO
from unittest.mock import patch



class TestOutput(unittest.TestCase):
    """Tests for output class."""

    def setUp(self):
        self.home_kingdom = "HOMIE"
        self.ally_kingdoms = ["ALLYONE", "ALLYTWO", "ALLYTHREE"]

    def test_if_NONE_is_printed_if_number_of_allies_is_not_sufficient(self):
        num_of_allies_required = 5
        output = op.Outputter(self.home_kingdom, self.ally_kingdoms, num_of_allies_required)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
                output.print_standard_output()
                self.assertEqual(
                    fakeOutput.getvalue().strip(),
                    "NONE")

    def test_if_kingdom_names_are_printed_in_std_format_separated_by_spaces_if_number_of_allies_is_sufficient(self):
        num_of_allies_required = 3
        output = op.Outputter(self.home_kingdom, self.ally_kingdoms, num_of_allies_required)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
                output.print_standard_output()
                self.assertEqual(
                    fakeOutput.getvalue().strip(),
                    "HOMIE ALLYONE ALLYTWO ALLYTHREE")