# Input: Three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Finding the smallest and largest numbers
smallest = num1
largest = num1

if num2 < smallest:
    smallest = num2
elif num2 > largest:
    largest = num2

if num3 < smallest:
    smallest = num3
elif num3 > largest:
    largest = num3

# Displaying the results
print(f"The smallest number is: {smallest}")
print(f"The largest number is: {largest}")
