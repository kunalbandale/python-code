# decorator in python

def my_spaces(func):
    def wrap_func():
        print('--------------')
        func()
        print('--------------')
    return wrap_func

@my_spaces
def hello():
    print('hello')

hello()