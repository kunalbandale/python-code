score = 55

if score >= 101:
	print("Invalid Score")
	exit()

if score >= 90:
	print("A")
elif score >= 80:
	print("B")
elif score >= 70:
	print("C")
elif score >= 60:
	print("D")
else:
	print("F")

print("Grade", score)