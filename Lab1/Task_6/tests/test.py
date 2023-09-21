import os
import unittest
from Task_6.main import save_document


class SaveDocumentCase(unittest.TestCase):
    def test_missing_url_schema(self):
        url: str = "/"
        path: str = "../../Task_3"

        self.assertEqual(save_document(url, path), False)

    def test_invalid_url_schema(self):
        url: str = "hppt://////"
        path: str = "../../Task_3"

        self.assertEqual(save_document(url, path), False)

    def test_invalid_url(self):
        url: str = "http://////"
        path: str = "../../Task_3"

        self.assertEqual(save_document(url, path), False)

    def test_empty_url(self):
        url: str = ""
        path: str = ""

        self.assertEqual(save_document(url, path), False)

    def test_file_not_found(self):
        url: str = "https://i.ytimg.com/vi/SFfVu9mqOoA/"
        path: str = ""

        self.assertEqual(save_document(url, path), False)

    def test_invalid_folder(self):
        url: str = "https://media.tenor.com/RtmcggFXF04AAAAd/cat-kitten.gif"
        path: str = "./non_existent_folder/"

        self.assertEqual(save_document(url, path), False)

    def test_success(self):
        url: str = "https://media.tenor.com/RtmcggFXF04AAAAd/cat-kitten.gif"
        path: str = ""

        os.remove("./cat-kitten.gif")

        self.assertEqual(save_document(url, path), True)

    def test_success_upper_folder(self):
        url: str = "https://media.tenor.com/RtmcggFXF04AAAAd/cat-kitten.gif"
        path: str = "../"

        self.assertEqual(save_document(url, path), True)

        os.remove("../cat-kitten.gif")


if __name__ == "__main__":
    unittest.main()
