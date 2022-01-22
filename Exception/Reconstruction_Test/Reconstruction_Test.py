import json

def get_new_username(file_object):
	name = input("Hello, what's your name？ ")
	json.dump(name,file_object)
	return name

def get_username(file_object):
	name = json.load(file_object)
	return name

def greet_user(name):
	print(f"Welcome, {name}.")

try:
	with open("username.json","r") as username:
		name = get_username(username)

except FileNotFoundError:
	with open("username.json","w") as username:
		name = get_new_username(username)
		greet_user(name)
else:
	greet_user(name)