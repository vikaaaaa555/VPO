import unittest
from unittest.mock import patch

from Task_3.main import main


class MainCase(unittest.TestCase):
    @patch("builtins.input", lambda: "")
    def test_too_few_values(self):
        self.assertIsNone(main())

    @patch("builtins.input", lambda: "A B")
    def test_value_not_a_number(self):
        self.assertIsNone(main())

    @patch("builtins.input", lambda: "1e-1 -1")
    def test_invalid_values(self):
        self.assertIsNone(main())

    def test_with_correct_inputs(self):
        with patch("builtins.input", lambda: "0 -0"):
            self.assertEqual(main(), -0)

        with patch("builtins.input", lambda: "0 42"):
            self.assertEqual(main(), 0)

        with patch("builtins.input", lambda: "1e-10 1e10"):
            self.assertEqual(main(), 1)

        with patch("builtins.input", lambda: "20.15 30"):
            self.assertEqual(main(), 604.5)


if __name__ == "__main__":
    unittest.main()
