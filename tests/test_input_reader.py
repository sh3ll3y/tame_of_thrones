"""Test cases to read inputs from text files."""

import input_reader as ir  # pylint: disable=import-error
import os
import unittest

from .test_config import test_config_data

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


class TestInputReader(unittest.TestCase):
    """Tests of input reader functions."""

    def test_if_correct_number_of_rows_are_returned_from_input_file(self):
        input_file = os.path.join(
            CURRENT_DIR, "test_input_files/test_input.txt")
        expected = 3
        actual = len(ir.read_input(input_file))
        self.assertEqual(expected, actual)

    def test_if_correct_strings_are_returned_with_secret_message_striped_for_white_spaces_at_ends(
            self):
        input_file = os.path.join(
            CURRENT_DIR, "test_input_files/test_input.txt")
        expected = ["KINGDOMONE SECRETMESSAGEONE",
                    "KINGDOMTWO SECRET MESSAGE TWO",
                    "KINGDOMTHREE SECRET MESSAGETHREE"
                    ]
        actual = ir.read_input(input_file)
        self.assertEqual(expected, actual)

    def test_if_True_is_returned_if_input_format_is_correct(self):
        input_file = os.path.join(
            CURRENT_DIR, "test_input_files/test_input.txt")
        lines = ir.read_input(input_file)
        regex = test_config_data.get("std_input_format")
        result = ir.validate_format(regex, lines)
        self.assertTrue(result)

    def test_if_False_is_returned_if_input_format_is_not_correct(self):
        input_file = os.path.join(
            CURRENT_DIR, "test_input_files/bad_test_input.txt")
        lines = ir.read_input(input_file)
        regex = test_config_data.get("std_input_format")
        with self.assertRaises(ir.InputFormatError):
            ir.validate_format(regex, lines)
