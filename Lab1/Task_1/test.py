import unittest
import random


class ExclamationCase(unittest.TestCase):
    def test_zero_exclamations(self):
        n = random.randint(0, 0)
        self.assertEqual("!" * n, "!" * 0)

    def test_none_zero_exclamations(self):
        n = random.randint(15, 15)
        self.assertEqual("!" * n, "!" * 15)

    def test_float_exclamations(self):
        n = random.randint(10, 10)
        n += 0.12

        with self.assertRaises(TypeError):
            _ = "!" * n


if __name__ == "__main__":
    unittest.main()
