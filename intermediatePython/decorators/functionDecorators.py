import functools


def repeat(numTimes):
    def decoratorRepeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(numTimes):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decoratorRepeat


def startEndDecorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result

    return wrapper


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        argsRepr = [repr(a) for a in args]
        kwargsRepr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ', '.join(argsRepr + kwargsRepr)
        print(f'Calling {func.__name__}({signature})')
        result = func(*args, **kwargs)
        print(f'{func.__name__!r} returned {result!r}')
        return result

    return wrapper


@repeat(numTimes=3)
def greet(name):
    print(f'Hello {name}')


@debug
@startEndDecorator
def sayHello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting


# greet('Alex')
sayHello('Alex')
