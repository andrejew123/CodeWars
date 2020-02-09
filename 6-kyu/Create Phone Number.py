def create_phone_number1(n):
    new = "("
    for i, y in enumerate(n):
        new += str(y)
        if i == 2:
            new += ") "
        elif i ==5:
            new += "-"
    return print(new)


def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}".format(*n)


create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
