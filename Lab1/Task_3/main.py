from Task_3 import msgs


def main():
    # Trying to parse the data from stdin
    try:
        l, w = input().split()
    except ValueError:
        print(msgs.ERR_MSG_TOO_FEW_VALUES)
        return

    # Checking if entered values are float-convertible
    try:
        l, w = map(float, (l, w))
    except ValueError:
        print(msgs.ERR_MSG_VALUES_NOT_FLOAT)
        return

    # Checking if either value is negative (2D object dimensions cannot be negative)
    if l < 0 or w < 0:
        print(msgs.ERR_MSG_INVALID_VALUES)
        return

    # If all the checks are passed, printing the result
    print(l * w)

    return l * w


if __name__ == "__main__":
    main()
