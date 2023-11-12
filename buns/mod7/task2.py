def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        arg = args[0]

        if arg in cache.keys():
            return cache[arg]
        else:
            cache[arg] = func(*args, **kwargs)

        return func(*args, **kwargs)

    return wrapper


@memoize
def fibonacci(a):
    if a < 2:
        return a
    else:
        return fibonacci(a - 1) + fibonacci(a - 2)

