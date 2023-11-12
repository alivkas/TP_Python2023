import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        result_time = end_time - start_time
        print(f"Время выполнения функции: {result_time} секунд")
        return result

    return wrapper


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


def validate_args(func):
    def wrapped_func(*args, **kwargs):
        args_count = len(args) + len(kwargs)

        if args_count < 1:
            return "Not enough arguments"
        if args_count > 1:
            return "Too many arguments"
        if not isinstance(args[0], int):
            return "Wrong types"
        if args[0] < 0:
            return "Negative argument"

        return func(*args, **kwargs)

    return wrapped_func


@validate_args
@timer
def fibonacci(a):
    if a < 2:
        return a
    else:
        return fibonacci(a - 1) + fibonacci(a - 2)


print(fibonacci(101))
