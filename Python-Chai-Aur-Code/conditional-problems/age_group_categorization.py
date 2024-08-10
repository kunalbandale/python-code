user_age = int(input("Enter Your Age:"))

if user_age < 13:
	print("Child")
elif user_age >= 13 and user_age <= 19:
	print("Teenager")
elif user_age >= 20 and user_age <= 59:
	print("Adult")
else:
	print("Senior")