import requests
from urllib3.exceptions import NameResolutionError
from requests.exceptions import (
    MissingSchema,
    InvalidSchema,
    InvalidURL,
)
import argparse
import os

from Task_6 import msgs


def save_document(url: str, folder: str) -> bool:
    """This function takes a `URL` and a `folder` as inputs
    and saves the downloaded from the `URL` file to the `folder`.

    :param url: string that contains URL of the file
    :param folder: where to save the file
    :return: True, if success, False otherwise
    """

    # Trying to get the file from the URL. Aborting if the URL has invalid schema.ß
    try:
        response = requests.get(url)
    except (MissingSchema, InvalidSchema, InvalidURL, NameResolutionError):
        print(msgs.MISSING_OR_INVALID_SCHEMA_URL.format(url=url))
        return False

    # Aborting if there is no file, or URL is broken.
    if response.status_code != 200:
        print(msgs.BROKEN_URL)
        return False

    filename = url.split("/")[-1]
    folder = os.path.abspath(folder)
    filepath = os.path.join(folder, filename)

    # Verifying the existence of saving path
    if not os.path.lexists(folder):
        print(msgs.INVALID_PATH)
        return False

    with open(filepath, "wb+") as f:
        f.write(response.content)
        print(msgs.SUCCESS.format(filepath=filepath))

    return True


def main():
    argparser = argparse.ArgumentParser()

    argparser.add_argument("url")
    argparser.add_argument("path")

    args = argparser.parse_args()

    save_document(args.url, args.path)


if __name__ == "__main__":
    main()
