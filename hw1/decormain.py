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
