import unittest
from main import hello, rand


class TestHello(unittest.TestCase):

    def test_hello_format(self):
        result = hello()
        self.assertTrue(result.startswith("Hello"))
        self.assertTrue(result.endswith("!"))


class TestRand(unittest.TestCase):

    def test_rand_cnt(self):
        result = rand()
        self.assertTrue(len(result) >= 5 and len(result) <= 50)

    def test_rand_exclamation(self):
        result = rand()
        self.assertEqual(result, "!" * len(result))


if __name__ == '__main__':
    unittest.main()
