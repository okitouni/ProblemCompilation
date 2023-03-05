# utility to calculate the big O of a function
from timeit import Timer
from typing import Callable, Iterable


def time(func: Callable, runs=10, *args, **kwargs):
    """Calculate the big O of a function
    :param func: the function to calculate the big O of
    :param args: the arguments to pass to the function
    :param kwargs: the keyword arguments to pass to the function
    :return: the big O of the function
    """
    # create a timer object
    timer = Timer(lambda: func(*args, **kwargs))
    result = timer.timeit(number=runs) / runs
    # calculate the big O
    return result


def map_time(func: Callable, arg_sequence: Iterable, runs=10):
    """Calculate the big O of a function for a sequence of arguments
    :param func: the function to calculate the big O of
    :param arg_sequence: the sequence of arguments to pass to the function
    :return: a list of the big O of the function for each argument
    """
    return [time(func, runs, *args) for args in arg_sequence]
