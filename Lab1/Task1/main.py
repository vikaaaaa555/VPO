import random


def rand():
    return '!' * random.randint(5, 50)


def hello():
    return f"Hello, World!\nAndhiagain!\n{rand()}"


if __name__ == "__main__":
    print(hello())
