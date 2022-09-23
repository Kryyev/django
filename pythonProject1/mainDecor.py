#простой декоратор

def decorator(func):
    print('оболочка начало')
    def wrapper():
        print('что-то до wrapper', func.__name__)
        func()
        print('что-то после wrapper', func.__name__)
    return wrapper()

@decorator
def function():
    print('основная функция')
a = 2
b = 1
c = a-b
print(c)
function()

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
def add(a,b):
    print('func1')
    return a + b

@decorator_args
def sub(a, b):
    print('func2')
    return a - b

print('start')

c = add(1, 2)
v = sub(2, 1)
print('c = ', c)
print('v = ', v)