import time

t0 = time.time()


def cached(func):
    cach = {}

    def wrapper(chislo):
        if chislo in cach:
            return cach[chislo]
        else:
            cach[chislo] = func(chislo)
            return cach[chislo]

    return wrapper


@cached
def fib(chislo):
    if chislo == 1 or chislo == 2:
        return 1
    else:
        return fib(chislo - 1) + fib(chislo - 2)


print(fib(500))
t1 = time.time()
print(t1 - t0)
