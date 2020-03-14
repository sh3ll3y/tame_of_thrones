"""Test cases to print output."""

import output as op  # pylint: disable=import-error
import unittest

from io import StringIO
from unittest.mock import patch


class TestOutput(unittest.TestCase):
    """Tests for output class."""

    def setUp(self):
        self.kingdoms = ["HOMIE", "ALLYONE", "ALLYTWO", "ALLYTHREE"]

    def test_if_names_of_the_kingdoms_are_printed_in_standard_format(self):
        output = op.Outputter(self.kingdoms)
        expected = "HOMIE ALLYONE ALLYTWO ALLYTHREE"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            output.print_standard_output()
            self.assertEqual(
                fakeOutput.getvalue().strip(),
                expected)
