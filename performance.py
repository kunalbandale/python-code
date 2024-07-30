from time import time

def performance(fn):
    def wrapper(*args , **kawrgs):
        t1 = time()
        result = fn(*args,**kawrgs)
        t2 = time()
        print(t2-t1)
        return result
    return wrapper


@performance
def long_time():
    for i in range(234343):
        i*5
long_time()