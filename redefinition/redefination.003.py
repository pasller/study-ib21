def check_password(password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if password:
                if password == input("Введите пароль"):
                    return func(*args, **kwargs)
                else:
                    print("Неверный пароль")
            else:
                print("не стоит хранить данные без пароля")
                return func(*args, **kwargs)

        return wrapper
    return decorator

@check_password("")
def make_burger(typeOfMeat, withOnion=False, withTomato=True):
    return (typeOfMeat, withOnion, withTomato)

print(make_burger("chicken", True, False))