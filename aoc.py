import itertools
import time


def timer(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, *kwargs)
        print(f"Time: {time.time() - start}s")
        return result

    return wrapper


def take(iterable, n):
    return tuple(itertools.islice(iterable, 0, n))
