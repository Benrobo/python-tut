from time import perf_counter
from math import floor


def Timer(func):
    
    def runtime_time(*args, **kwargs):
        start = perf_counter()
        value = func(*args, **kwargs)
        end = perf_counter()
        runtime = (end-start)
        # print(runtime)
        return f"Took {func.__name__} {runtime}"
    return runtime_time