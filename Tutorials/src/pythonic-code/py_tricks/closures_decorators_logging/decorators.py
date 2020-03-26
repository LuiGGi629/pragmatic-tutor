# Decorator is a function that takes another function as an argument, adds some kind of functionality, and then returns
# another function. All of this without altering the source code of the original function that you've passed in.
import logging
import os
import time
from functools import wraps

os.chdir('/Tutorials/src/pythonic-code/py_tricks/closures_decorators_logging')


def my_logger(orig_func):
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(f'Ran with args: {args} and kwargs: {kwargs}')
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t0 = time.time()
        result = orig_func(*args, **kwargs)
        t1 = time.time() - t0
        print(f'{orig_func.__name__} ran in: {t1:.2f} sec.')
        return result

    return wrapper


def decorator_function(original_function):

    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)

    return wrapper_function


class DecoratorClass(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f'call method executed this before {self.original_function.__name__}')
        return self.original_function(*args, **kwargs)


@DecoratorClass
def display():
    print('display function ran')


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print(f'display_info ran with arguments ({name}, {age})')


display_info('Stak', 37)
# display()
