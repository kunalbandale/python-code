#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat('Tom',2)
cat2 = Cat('Spy',4)
cat3 = Cat('Jack',6)

def OldestCat():
   return max(cat1.age,cat2.age,cat3.age)

print(f"The oldest cat is {OldestCat()} years old")

