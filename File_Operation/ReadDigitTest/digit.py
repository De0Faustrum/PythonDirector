with open("pi_digit.txt") as file_object:
	lines = file_object.readline()
	pi_digits=""
	for line in lines:
		pi_digits += line.strip()
	print(pi_digits)

btd = input("Enter your birthday and we'll tell you if your birthday is in the fisrt 10000 digits of pi: ")
if btd in pi_digits:
	print(f"Your birthday {btd} is in pi.")
else:
	print(f"Your birthday {btd} is not in pi.")