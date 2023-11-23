import re


def is_valid(color: str) -> bool:
    """
    :param color:
    :return Bool:

    Tests:
    >>> is_valid("#21f48D")
    True
    >>> is_valid("#888")
    True
    >>> is_valid("rgb(255, 255,255)")
    True
    >>> is_valid("rgb(10%, 20%, 0%)")
    True
    >>> is_valid("hsl(200,100%,50%)")
    True
    >>> is_valid("hsl(0, 0%, 0%)")
    True
    >>> is_valid("#2345")
    False
    >>> is_valid("ffffff")
    False
    >>> is_valid("rgb(257, 50, 10)")
    False
    >>> is_valid("hsl(20, 10, 0.5)")
    False
    >>> is_valid("hsl(34%, 20%, 50%)")
    False
    """


    hex_regex = r'^#([0-9a-fA-F]{3}){1,2}$'
    hex = re.fullmatch(hex_regex, color)
    rgb_regex = r'^rgb\((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5]|0%|100%) ?, ?(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5]|0%|100%) ?, ?(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5]|0%|100%)\)$'
    rgb = re.fullmatch(rgb_regex, color)
    hsl_regex = r'^hsl\((\d{1,2}|[1-2]\d{2}|3[0-5]\d) ?, ?(100%|\d{1,2}%) ?, ?(100%|\d{1,2}%)\)$'
    hsl = re.fullmatch(hsl_regex, color)
    percent_regex = r"rgb\(\s*((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)%\s*,\s*){2}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)%\s*\)"
    percent = re.fullmatch(percent_regex, color)

    if not(hex) and not(rgb) and not(hsl) and not(percent):
        return False

    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
