import random
mn = random.randint(1, 100)
score = 0

while True:
	score += 1 #guess = guess + 1
	guess = int(input("Guess a number from 1 to 100: "))
	if guess == mn:
		print("Good job, you guessed it!")
		break
	elif guess > mn:
		print("Too high, try again.")
	else:
		print("Too low, try again.")

print("You tried "+ str(score) + " times.")