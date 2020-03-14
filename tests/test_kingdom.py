"""Holds test cases for Kingdom class."""

import cryptography as crypto  # pylint: disable=import-error
import unittest

from config import config_data
from kingdom import Kingdom
from .test_config import test_config_data
from unittest.mock import patch


class TestKingdom(unittest.TestCase):
    """Test of Kingdom class."""

    def _setUp(self):
        self.kingdom_obj = Kingdom("KINGDOMONE")

    def test_if_kingdom_object_is_created_with_correct_properties(self):
        with patch.dict(config_data, test_config_data, clear=True):
            self._setUp()
            self.assertEqual(self.kingdom_obj.name, "KINGDOMONE")
            self.assertEqual(self.kingdom_obj.emblem, "EmblemOne")
            length_of_emblem = 9
            self.assertEqual(self.kingdom_obj.cipher_key, length_of_emblem)
            self.assertEqual(self.kingdom_obj.allies, [])

    def test_send_one_correct_msg_and_one_incorrect_msg_to_other_kingdoms(
            self):
        msg = [{"name": "KINGDOMTWO", "msg": "'NJVKUGGNVCRRFX'"},
               {"name": "KINGDOMTHREE", "msg": "ABCEFGHIEMBLEMIJK"}
               ]
        with patch.dict(config_data, test_config_data, clear=True):
            self._setUp()
            actual = self.kingdom_obj.send_secret_msg(msg)
            expected = ["KINGDOMTWO"]
            self.assertEqual(actual, expected)

    def test_send_two_correct_messages_to_other_kingdoms_returns_kingdom_names(
            self):
        msg = [{"name": "KINGDOMTWO", "msg": "NJVKUGGNVCRRFX"},
               {"name": "KINGDOMTHREE", "msg": "PLXMWIIPXESSCPP"}
               ]
        with patch.dict(config_data, test_config_data, clear=True):
            self._setUp()
            actual = self.kingdom_obj.send_secret_msg(msg)
            expected = ["KINGDOMTWO", "KINGDOMTHREE"]
            self.assertEqual(actual, expected)

    def test_no_correct_message_to_other_kingdoms_returns_empty_list(self):
        msg = [{"name": "KINGDOMTWO", "msg": "KINGDOMTWONOCIPHER"},
               {"name": "KINGDOMTHREE", "msg": "KINGDUMTHRI"}
               ]
        with patch.dict(config_data, test_config_data, clear=True):
            self._setUp()
            actual = self.kingdom_obj.send_secret_msg(msg)
            expected = []
            self.assertEqual(actual, expected)

    def test_receive_correct_message_from_a_kingdom_returns_True(self):
        with patch.dict(config_data, test_config_data, clear=True):
            self._setUp()
            result = self.kingdom_obj.receive_secret_msg('VNKUNVQQXWN')
            self.assertTrue(result)

    def test_receive_incorrect_message_from_a_kingdom_returns_False(self):
        with patch.dict(config_data, test_config_data, clear=True):
            self._setUp()
            result = self.kingdom_obj.receive_secret_msg('INKORRECT')
            self.assertFalse(result)

    def test_form_rule_with_sufficient_allies_returns_kingdom_with_allies(
            self):
        with patch.dict(config_data, test_config_data, clear=True):
            self._setUp()
            self.kingdom_obj.allies = ["KINGDOMTWO", "KINGDOMTHREE"]
            actual = ["KINGDOMONE", "KINGDOMTWO", "KINGDOMTHREE"]
            # Number of allies to win in test data is 2.
            expected = self.kingdom_obj.form_rule()
            self.assertEqual(actual, expected)

    def test_form_rule_with_insufficient_allies_returns_kingdom_with_allies(
            self):
        with patch.dict(config_data, test_config_data, clear=True):
            self._setUp()
            self.kingdom_obj.allies = ["KINGDOMTWO"]
            actual = ["NONE"]
            # Number of allies to win in test data is 2.
            expected = self.kingdom_obj.form_rule()
            self.assertEqual(actual, expected)
