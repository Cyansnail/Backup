# Isaac Lynn
# Period 4

# Variable declaration and assignment
# Examples
myNum = 12 # Integer type
myString = "12" # string type
myNum + 3 # works
#myString + 3 # doesn't work
myString + "3" # works but output is: 123

# make a variable and assign it a value of your favorite movie
myMovie = "Endgame"
# print "my favorite movie is " followed by the variable
print("My favorite movie is " +  myMovie + ".")

# while loops
# example - print from 1 - 10
x = 1
while x <= 10:
	print(x)
	x = x + 1

# count down from 100
y = 100
while y >= 0:
	print(y)
	y = y - 1

# string concatenation
# means putting two strings together
# example
myName = "Isaac"
print("Hello " + myName)

# input
# example
yourName = input("What is your name? ")
print("Hello " + yourName + ", have a nice day.")

# ask for two numbers, add them and print the sum
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
numt = num1 + num2
num1 = str(num1)
num2 = str(num2)
numt = str(numt)
print(num1 + " + " + num2 + " = " + numt)

# if/else statements
# example
num = int(input("Enter a number: "))
if num > 100:
	print("Your number is more than 100")
elif num == 100:
	prin("Your number is equal to 100")
else:
	print("Your number is less than or 100")

# ask if it is your birthday, if so wish them a happy birthday
birth = input("Is today your birthday? (Y/N) ")
if birth == "Y":
	print("Happy Bithday!")
elif birth == "N":
	print("Have a nice day anyway.")
else:
	print("This was a yes or no question.")