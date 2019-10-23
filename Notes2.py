# Conditional
print("Welcome to the Movie Bot")
age = input("How old are you? : ")
age = int(age)
if age > 17:
	print("You can see an R rated movie")
else:
	print("You can not see an R rated movie")

print("Have a great day")


myNum = 4 
choice = int(input("Pick a number between 1 an 10 : "))
if myNum == choice :
	print("You geussed it!")
elif choice < myNum :
	print("Too low")
else:
	print("Too high")
# == (equal to), <, >, <=, >=, !=(not equal to)

bDay= input("Is today your birthday?(y/n)")
if bDay == "yes" or bDay == "Yes":
	print("Happy Birthday!")
elif bDay == "no":
	print("That's too bad, have a nice day anyway.")
else:
	print("Learn how to read directions")