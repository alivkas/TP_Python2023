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
