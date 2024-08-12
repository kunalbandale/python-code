# timing function
import time

def timer(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args,**kwargs)
		end = time.time()
		print(end-start)
		return result
	return wrapper

@timer
def example_function(n):
	time.sleep(n)

example_function(4)