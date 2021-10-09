def val_checker(test):
    def _val_checker(func):
        def wrapper(*args):
            for i in args:
                if test(i):
                    return func(i)
                else:
                    raise ValueError
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(-3))
