from Task_2 import msgs


def get_personal_data() -> tuple | None:
    """This function reads the data from stdin and
    returns tuple containing 3 values: first name, last name, and age
    of the person

    :return: first name, last name, age
    """
    # Trying to read the values from stdin and handling
    # possible reading errors.
    try:
        first_name, last_name, age = input(msgs.INPUT_MSG).split()
    except ValueError:
        print(msgs.ERR_MSG_TOO_FEW_VALUES)
        return

    # Trying to parse the age correctly #1.
    # Here, age is incorrect if it is not parseable to float.
    try:
        age = float(age)
    except ValueError:
        print(msgs.ERR_MSG_AGE_NOT_FLOAT)
        return

    # Trying to parse the age correctly #2.
    if age <= 0 or age > 2023:
        print(msgs.ERR_MSG_AGE_INVALID)
        return

    return first_name, last_name, age


def get_age_statistics(ages: list) -> tuple:
    if not len(ages):
        return ()

    return min(ages), max(ages), sum(ages) / len(ages)


def main():
    people = []
    ages = []

    print(msgs.FIRST_MSG)

    while True:
        try:
            data = get_personal_data()

            if not data:
                continue

            # If everything is correct, add person info to lists
            first_name, last_name, age = data

            people += [(first_name, last_name, str(age))]
            ages += [age]

        except KeyboardInterrupt:
            break

    # Formatting the data for the output
    people = [" ".join(person) for person in people]
    age_stats = get_age_statistics(ages)

    print()
    print("\n".join(people))
    print(" ".join(map(str, age_stats)))


if __name__ == "__main__":
    main()
