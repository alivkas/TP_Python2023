def recurs_pow(a, n):
    if n == 1:
        return a
    elif n == 0:
        return 1
    elif n % 2 == 0:
        return recurs_pow(a * a, n / 2)
    else:
        return a * recurs_pow(a, n - 1)
