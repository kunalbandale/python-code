def multiply_by_2(li):
  return li*2

def check_odd(item):
  return item % 2 != 0

print(list(filter(check_odd,[1,2,3,4,5])))