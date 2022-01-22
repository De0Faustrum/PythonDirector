#Exception:
#1.Traceback: When encountering syntax error, python creates a abnormal object reports Traceback.

#2.Use try-except-else statement to enhance your program, for example:
try:
	answer = 5/0
except ZeroDivisionError:
	print("You cannot divide by 0!")
else:
	print(f"The answer is {answer}.")
	#"ZeroDivisionError" is an abnormal object which is created when 0 acts as divisor.
	#If "try" statement runs, python ignores "except" statement and jump to "else".
	#If "try" statement reports error, python will search and run corresponding "except" module and ignore "else".

#3.Managing File error:
try:
	with open("lyrics.txt") as lrcs:
		lyrics = lrcs.read()
except FileNotFoundError:
	print("'lyrics.txt' not found.'")
else:
	print(lyrics)
	
#4.Error silence:
	#"pass" in "exception" statement. If error exists, nothing will happen.
try:
	with open("lyrics.txt") as lrcs:
		print("Hello")
except FileNotFoundError:
	pass

#5.Data Memory:
	#use format ".json" to store information:
import json
try:
	with open("username.json","r") as username:
		name = json.load(username)
except FileNotFoundError:
	with open("username.json","w") as username:
		name = input("Hello, what's your name？ ")
		print(f"Welcome, {name}.")
		json.dump(name,username)
else:

		print(f"Welcome back, {name}.")