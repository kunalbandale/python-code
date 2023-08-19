class Employee:

    def __init__(self , name , salary):
        self.name = name
        self.salary = salary

    def getSal(self):
        return self.salary

r = Employee( "ram",24444)
print(r.salary)
print(r.name)

h = Employee("harry potter",200000)
print(h.name)
print(h.salary)


