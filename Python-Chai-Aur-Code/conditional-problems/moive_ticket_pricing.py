user_age = int(input("Enter you age:"))
day = "wednesday"

price = 12 if user_age >= 18 else 8

if day == "wednesday":
	price = price - 2

print("Ticket price for you is $" , price)