import functools
import time


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.numCalls = 0

    def __call__(self, *args, **kwargs):
        self.numCalls += 1
        print(self.numCalls)
        return self.func(*args, **kwargs)


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        startTime = time.time()
        result = func(*args, **kwargs)
        endTime = time.time()
        diffTime = endTime - startTime
        print(f'Elapsed time: {diffTime}')
        return result

    return wrapper


@CountCalls
def fibRecursive(n):
    if n == 0:
        return 0
    if n == (1 or 2):
        return 1
    return fibRecursive(n - 1) + fibRecursive(n - 2)


@timer
def fibDynamic(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        tmp = fib[0] + fib[1]
        fib[0] = fib[1]
        fib[1] = tmp
    return fib[1]


print(fibRecursive(30))
print(fibDynamic(36))
