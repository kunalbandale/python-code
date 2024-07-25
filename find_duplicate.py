some_value = ['a','b','c','d','a','b']
duplicate = []

for value in some_value:
    if some_value.count(value) > 1:
        if value not in duplicate:
         duplicate.append(value)
print(duplicate)