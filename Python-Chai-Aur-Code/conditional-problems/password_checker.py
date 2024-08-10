pass = "123Password"
pass_length = len(pass)

if len(pass) < 6:
	strength = "Weak"
elif len(pass) <= 10:
	strength = "Medium"
else:
	strength = "Strong"

print("Password strength is:" , strength)
