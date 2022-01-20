#File:
#1.ReadFile:
	#(1).Read all the file:
with open("lyrics.txt") as file_object:
	#"file_object" is an object which embeds the file "lyrics.txt"
	contents = file_object.read()
	#Calling function "read()" to read the whole file and copy it into a string "contents"
	print(contents.rstrip())
	#The last line is void string so we need to strip the right end.

	#(2).Read file line by line:
	with open("lyrics.txt") as file_object:
		for line in file_object:
			print(line.rstrip())
		#and you can use the statement below to copy each line into a list.
		lines = file_object.readline()

#2.WriteFile:
	#(1).To write into file, we should provide anothor argument 
			#"w(write)"/"r(read(default))"/"a(append)"/"r+(read and write)".
	#For example:
with open("void.txt","w") as file_object:
	file_object.write("I love Hoshino Hinata.\n")
	#Switch to a new line (Not provided automatically).
	file_object.write("I love Shirosaki Hana.")

#3.AppendFile:
	#Use "a" as the second argument to open file.
with open("void.txt","a") as file_object:
	file_object.write("\nI love Kamisato Ayaka.")
