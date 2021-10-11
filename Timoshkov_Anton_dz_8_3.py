from functools import wraps


def type_logger(func):

    @wraps(func)
    def wrapper(*args):
        for i in args:
            print(f"{i}: {type(i)}")
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


calc_cube(5, 6)
print(calc_cube.__name__)
