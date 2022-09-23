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

    print('func1')
    return a + b

@decorator_args
def sub(a, b):

    print('func2')
    return a - b

print('start')

c = add(1, 2)
d = sub(2, 1)
print('c = ', c, 'd = ', d)
