#Square
my_list = [4,5,3]

new_list = list(map(lambda num:num**2,my_list))
print(my_list)


# list sorting
a = [(0,2),(4,2),(10,-1),(9,9)]
a.sort(key=lambda x: x[1])
print(a)