# Input: Three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Finding the smallest and largest numbers
smallest = min(num1, num2, num3)
largest = max(num1, num2, num3)

# Displaying the results
print(f"The smallest number is: {smallest}")
print(f"The largest number is: {largest}")
