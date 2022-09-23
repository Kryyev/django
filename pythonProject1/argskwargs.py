def func1(*args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)
func1('hello world', 'hi', first = 'hello', second = 2, last = 'goodbye®')