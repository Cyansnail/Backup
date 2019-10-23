# Name:Isaac 
# Period 4
# Dice Rolling Simulator
import random

rollChoices = [1,2,3,4,5,6]
nDice = int(input("How many dice would you like to roll? "))
dNum = 0
roll1 = 0
roll2 = 0
roll3 = 0
roll4 = 0
roll5 = 0
roll6 = 0
def rollDice():
	print("Dice " + str(dNum) + " rolled a " + str(roll))

for i in range(nDice):
	roll = random.choice(rollChoices)
	dNum = dNum + 1
	rollDice()
	if roll == 1:
		roll1 = roll1 + 1
	elif roll == 2:
		roll2 = roll2 + 1
	elif roll == 3:
		roll3 = roll3 + 1
	elif roll == 4:
		roll4 = roll4 + 1
	elif roll == 5:
		roll5 = roll5 + 1
	else:
		roll6 = roll6 + 1

proll1 = str((roll1 / nDice)*100)
proll2 = str((roll2 / nDice)*100)
proll3 = str((roll3 / nDice)*100)
proll4 = str((roll4 / nDice)*100)
proll5 = str((roll5 / nDice)*100)
proll6 = str((roll6 / nDice)*100)
nDice = str(nDice)
roll1 = str(roll1)
roll2 = str(roll2)
roll3 = str(roll3)
roll4 = str(roll4)
roll5 = str(roll5)
roll6 = str(roll6)
print("\n""The dice was rolled " + nDice + " times")
print("1 was rolled " + roll1 + " times.")
print("2 was rolled " + roll2 + " times.")
print("3 was rolled " + roll3 + " times.")
print("4 was rolled " + roll4 + " times.")
print("5 was rolled " + roll5 + " times.")
print("6 was rolled " + roll6 + " times.")
print("Percent of 1s: " + proll1)
print("Percent of 2s: " + proll2)
print("Percent of 3s: " + proll3)
print("Percent of 4s: " + proll4)
print("Percent of 5s: " + proll5)
print("Percent of 6s: " + proll6)