# "Therefore, in simple terms: A closure is an inner function that remembers and has access to variables
# in the local scope in which it was created even after the outer function has finished executing"

# closures are when a function remembers the environment it was created it, specifically the variables around it.
import logging
import os

os.chdir('/Tutorials/src/pythonic-code/py_tricks/closures_decorators_logging')
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):

    def log_func(*args):
        logging.info(f'Running "{func.__name__}" with arguments {args}')
        print(func(*args))

    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)


def outer_function(msg):

    def inner_function():
        print(msg)

    return inner_function


# si_func = outer_function('Siemka')
# bye_func = outer_function('Bajo')
#
# si_func()
# bye_func()
