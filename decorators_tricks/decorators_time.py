from functools import wraps
from time import sleep, time, perf_counter


def time_count(func):
    """times any function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        time_start = perf_counter()
        func(*args, **kwargs)
        time_end = perf_counter()
        total_time = round(time_end - time_start, 2)
        print('Time', total_time, 'seconds')

    return wrapper


@time_count
def do_something(param: str):
    """Does something important"""
    sleep(2)
    print(param)


if __name__ == '__main__':
    do_something('Hey everyone!')
    print(do_something.__name__)  # без @wraps будет отображаться не корректно
    print(do_something.__doc__)  # без @wraps будет отображаться не корректно
