#передача функции в качестве параметра в другую функцию

def name():
    name = 'Вася'
    bar(name)

def bar(name):
    log(name)
def log(name):
    print(name)