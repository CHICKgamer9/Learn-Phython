# Asks for the name of the user and stores it as a variable
name = input("Hi, What is your name?")
#Prints the name while adding "Hello world"
print("Well hello,",name)
#Uses the name in a sentance to ask for the age
age = int(input(f"So, {name}, how old are you?"))
#Changes what is printed based on how old the user is
if age > 17:
	print("your an adult")
else:
	print("Your not an adult")
