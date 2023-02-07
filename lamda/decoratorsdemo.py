def outer():
    print("hello from outer function")
    def inner():
        print("hello from inner function")
    return inner
d=outer()
d()
