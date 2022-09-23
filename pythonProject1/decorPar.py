#декоратор для функций с параметрами

def decorator_args(func):
    print('декоратор с параметрами')
    def decorated(a, b):
        print('до вызова func', func.__name__)
        funct = func(a, b)
        print('после вызова функции', func.__name__)
        return funct
        return decorated()

@decorator_args
def add(a, b):
    a = 2
    b = 3
    print('func1')
    return add(a + b)

@decorator_args
def sub(a, b):
    a = 3
    b = 2
    print('func2')
    return sub(a - b)

print('sub = ', sub)
print('add = ', add)
