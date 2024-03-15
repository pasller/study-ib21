def logged(func):
    def decorated_func(n, password):
        if password == "qwerty":
            return func(n, password)
        else:
            print("В доступе отказано")
            return None
    return decorated_func


@logged
def fib(n, password):
    if n <= 2:
        return 1
    else:
        return fib(n - 1, password) + fib(n - 2, password)


print(fib(20, "qwerty"))
