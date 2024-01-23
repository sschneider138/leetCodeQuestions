class CountCalls:
    def __init__(self, func):
        self.func = func
        self.numCalls = 0

    def __call__(self, *args, **kwargs):
        self.numCalls += 1
        print(self.numCalls)
        return self.func(*args, **kwargs)


@CountCalls
def sayHello():
    print('Hello')


sayHello()
sayHello()
sayHello()
