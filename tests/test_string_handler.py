"""Test casess for string handler methods."""

import string_handler as sh # pylint: disable=import-error
import unittest


class TestStringHandler(unittest.TestCase):
    """Tests of string handler functions"""

    def test_if_is_string_method_returns_True_when_input_is_of_type_string(self):
        input_string = "hello"
        result = sh.is_string(input_string)
        self.assertTrue(result)

    def test_is_string_method_returns_False_when_input_is_not_of_type_string(self):
        input_string = 123
        result = sh.is_string(input_string)
        self.assertFalse(result)

    def test_if_is_string_method_returns_True_when_input_is_list_of_strings(self):
        input_string = ["hello", "hi"]
        result = sh.is_string(input_string)
        self.assertTrue(result)

    def test_if_is_string_method_returns_False_when_input_list_has_a_non_string_value(self):
        input_string = ["hello", 1]
        result = sh.is_string(input_string)
        self.assertFalse(result)

    def test_if_correct_number_of_characters_of_a_word_are_returned(self):
        input_string = "geektrust"
        expected = {'g': 1, 'e': 2, 'k': 1, 't': 2, 'r': 1, 'u': 1, 's': 1}
        actual = sh.char_counter(input_string)
        self.assertDictEqual(expected, actual)

    def test_if_True_is_returned_if_a_main_str_contains_all_the_letters_of_the_sub_string_in_any_order(self):
        main_str = "geektrust"
        sub_str = "trust"
        result = sh.contains_sub_str_letters(main_str, sub_str)
        self.assertTrue(result)

    def test_if_False_is_returned_if_a_main_str_does_not_contain_all_the_letters_of_the_sub_string_in_any_order(self):
        main_str = "geektrust"
        sub_str = "trustx"
        result = sh.contains_sub_str_letters(main_str, sub_str)
        self.assertFalse(result)