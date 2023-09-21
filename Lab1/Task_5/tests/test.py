import os
import unittest

from Task_5.main import find_files


class FindFilesCase(unittest.TestCase):
    def test_invalid_path(self):
        self.assertEqual([], find_files("randomfoldername", "jpg"))

    def test_no_files_present(self):
        self.assertEqual([], find_files(".", "cpp"))

    def test_one_file_present(self):
        fpath = "/Users/mishashkarubski/PycharmProjects/TestLabs/Task_5/tests/tests.txt"

        self.assertEqual(
            [fpath],
            find_files(
                "/Users/mishashkarubski/PycharmProjects/TestLabs/Task_5/tests", "txt"
            ),
        )

    def test_many_files_present(self):
        with open(
            "/Users/mishashkarubski/PycharmProjects/TestLabs/Task_5/tests/a.tex", "w+"
        ) as f1, open(
            "/Users/mishashkarubski/PycharmProjects/TestLabs/Task_5/tests/b.tex", "w+"
        ) as f2:
            f1.write("123")
            f2.write("123")

        fpaths = [
            "/Users/mishashkarubski/PycharmProjects/TestLabs/Task_5/tests/a.tex",
            "/Users/mishashkarubski/PycharmProjects/TestLabs/Task_5/tests/b.tex",
        ]

        self.assertEqual(
            fpaths,
            sorted(
                find_files(
                    "/Users/mishashkarubski/PycharmProjects/TestLabs/Task_5/tests",
                    "tex",
                )
            ),
        )

        os.remove("/Users/mishashkarubski/PycharmProjects/TestLabs/Task_5/tests/a.tex")
        os.remove("/Users/mishashkarubski/PycharmProjects/TestLabs/Task_5/tests/b.tex")


if __name__ == "__main__":
    unittest.main()
