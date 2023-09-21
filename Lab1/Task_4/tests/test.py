import os
import re
import unittest

from Task_4.main import generate_html_table, main


class TableGeneratorCase(unittest.TestCase):
    def test_html_tags(self):
        table = generate_html_table(10)

        self.assertIn("<body", table)
        self.assertIn("<table", table)
        self.assertIn("<tr", table)
        self.assertIn("<td>", table)

        self.assertIn("</body>", table)
        self.assertIn("</table>", table)
        self.assertIn("</tr>", table)
        self.assertIn("</td>", table)

    def test_zero_rows(self):
        table = generate_html_table(0)

        self.assertNotIn("<tr", table)
        self.assertNotIn("<td>", table)

    def test_non_zero_rows(self):
        table = generate_html_table(300)

        self.assertCountEqual(["<tr"] * 300, re.findall("<tr", table))
        self.assertCountEqual(["<td"] * 300, re.findall("<td", table))


class MainCase(unittest.TestCase):
    @staticmethod
    def file_exists(directory, filename):
        file_path = os.path.join(directory, filename)

        return os.path.exists(file_path)

    def test_file_existence(self):
        main()
        self.assertTrue(self.file_exists(".", "gradient_table.html"))
        os.remove("gradient_table.html")


if __name__ == "__main__":
    unittest.main()
