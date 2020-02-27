def decorate(f):
    def wrapper(*args, **kwargs):
        print('before')
        r = f(*args, **kwargs)
        print('after')
        return r
    return wrapper


@decorate
def sayHello(name):
    return 'Hello {}'.format(name)

print(sayHello('LUR'))

import time

def timeit(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        f(*args, **kwargs)
        print("Time: {}".format(time.time() - start))
    return wrapper

@timeit
def useless():
    time.sleep(10)


def checkTypes(*types):
    def decorator(f):
        def wrapper(*args, **kwargs):
            for arg, T in zip(args, types):
                assert type(arg) == T, "{} is not a {}".format(arg, T)
            return f(*args, **kwargs)
        return wrapper
    return decorator    

@checkTypes(int, int)
def somme(a, b):
    return a + b




print(somme(3, "4"))

