def log_function_call(func):
    """
    Decorator that logs function calls with arguments and return values.

    Args:
        func: The function to be decorated.

    Returns:
        A wrapper function that logs the decorated function's call and return value.
    """

    def wrapper(*args, **kwargs):
        """
        Inner wrapper function that performs logging.

        Args:
            *args: Positional arguments passed to the decorated function.
            **kwargs: Keyword arguments passed to the decorated function.

        Returns:
            The result of calling the decorated function.
        """

        arg_str = ','.join(str(arg) for arg in args)  # Use comma (,) for positional arguments
        kwarg_str = '.'.join(f"{key}={value}" for key, value in kwargs.items())  # Use equal sign (=) for keyword arguments
        print(f"Calling {func.__name__}({arg_str}, {kwarg_str})")

        result = func(*args, **kwargs)

        print(f"{func.__name__} returned {result}")

        return result

    return wrapper

@log_function_call
def add_number(a, b):
    """
    Function that adds two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.
    """
    return a + b

add_1 = add_number(4, 9)
print(add_1)  # Output: 13
