list_of_numbers = input("Enter a list of numbers: ").split(",")

negative = []
positive = []

for i in list_of_numbers:
	if int(i) > 0:
		positive.append(i)
	elif int(i) < 0:
		negative.append(i)
	else:
		continue

print(positive)
print(negative)