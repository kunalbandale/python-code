def generator_function(num):
  for i in range(num):
      yield i*2

g = generator_function(100)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
