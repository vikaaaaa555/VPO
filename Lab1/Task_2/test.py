import unittest
from unittest.mock import patch

from Task_2.main import get_personal_data, get_age_statistics


class PersonalDataCase(unittest.TestCase):
    @patch("builtins.input", lambda x: "")
    def test_too_few_values(self):
        self.assertIsNone(get_personal_data())

    @patch("builtins.input", lambda x: "First Last ABC")
    def test_age_not_a_number(self):
        self.assertIsNone(get_personal_data())

    def test_invalid_age(self):
        with patch("builtins.input", lambda x: "First Last 2024"):
            self.assertIsNone(get_personal_data())

        with patch("builtins.input", lambda x: "First Last 0"):
            self.assertIsNone(get_personal_data())

        with patch("builtins.input", lambda x: "First Last -1"):
            self.assertIsNone(get_personal_data())

    def test_with_correct_inputs(self):
        with patch("builtins.input", lambda x: "First Last 10"):
            self.assertEqual(get_personal_data(), ("First", "Last", 10))

        with patch("builtins.input", lambda x: "First Last 0.00000000001"):
            self.assertEqual(get_personal_data(), ("First", "Last", 0.00000000001))

        with patch("builtins.input", lambda x: "First Last 1e-10"):
            self.assertEqual(get_personal_data(), ("First", "Last", 1e-10))


class AgeStatisticsCase(unittest.TestCase):
    def test_zero_len(self):
        self.assertEqual(get_age_statistics([]), ())

    def test_single_age_given(self):
        self.assertEqual(get_age_statistics([3]), (3,) * 3)

    def test_different_ages(self):
        self.assertEqual(get_age_statistics([3, 5, 7]), (3, 7, 5))
        self.assertEqual(get_age_statistics([729, 0, 1e-90]), (0, 729, 243))


if __name__ == "__main__":
    unittest.main()
