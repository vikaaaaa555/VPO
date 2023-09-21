import glob
import os

from Task_5 import msgs


def find_files(folder: str, extension: str) -> list | None:
    """This function returns a list of files with the specified
    file type (`extension`) in the `folder` and all its subfolders.

    :param folder: path to the folder where the files must be found
    :param extension: extension of the files to find
    :return: either a list of files, or None, if nothing found
    """
    folder = os.path.abspath(folder)
    search_path = os.path.join(folder, "**", f"*.{extension}")
    search_results = glob.glob(search_path, recursive=True)

    return search_results


def main():
    # Parsing the data isn't a problem here since both inputs are in separate lines.
    folder = input(msgs.FOLDER_INPUT)
    extension = input(msgs.EXTENSION_INPUT)

    # Verifying that path is valid.
    if not os.path.lexists(folder):
        print(msgs.INVALID_PATH)
        return

    results = find_files(folder, extension)

    if results:
        print("\n".join(results))
    else:
        print(msgs.NO_FILES_FOUND.format(ext=extension, folder=folder))


if __name__ == "__main__":
    main()
