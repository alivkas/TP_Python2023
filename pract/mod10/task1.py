import re


def is_valid(password: str) -> bool:
    """
    :param password:
    :return: Bool

    Tests:
    >>> is_valid("rtG3FG!Tr^e")
    True
    >>> is_valid("aA1!*!1Aa")
    True
    >>> is_valid("oF^a1D@y5e6")
    True
    >>> is_valid("enroi#$rkdeR#$092uWedchf34tguv394h")
    True
    >>> is_valid("пароль")
    False
    >>> is_valid("password")
    False
    >>> is_valid("qwerty")
    False
    >>> is_valid("lOngPa$$$W0Rd")
    False
    """
    symbols = re.fullmatch(r'[^a-zA-Z0-9^$%@#&*!?]', password)
    uppercase = re.findall(r'[A-Z]', password)
    digit = re.fullmatch(r'\d', password)
    special = re.findall(r'[^a-zA-Z0-9]', password)
    same = re.fullmatch(r'(.)\1\1', password)
    lenght = re.fullmatch(r'^.{6,}$', password)

    if not(symbols) and not(digit) and not(same) and not(lenght):
        return False
    elif len(uppercase) < 2:
        return False
    elif len(set(special)) < 2:
        return False

    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
