# Isaac Lynn
# Period 4
import random
import time
import os 
#variables
wList = ["awkward"]#,"bagpipes","banjo","bungler","croquet","crypt","fishhook","fjord","gazebo","gypsy","haiku","haphazard","hyphen","ivory","jazzy","jiffy","jinx","jukebox","kayak","kiosk","klutz","rhythmic","rogue","sphinx","squawk","swivel","toady","twelfth","unzip","waxy","wildebeest","yacht","zealous","zigzag","zippy","zombie"]
pdifficulty = 0
difficulty = input("Select a difficulty level(Number of failed guesses allowed)(5,10,15): ")
cList = []
mList = []
pgame = ['''





















 
                                                                          _
                                                                         / \\
                                                                         | |
                                                                         |_|
                                                                          |
                                                                        | # |
                                                                        |###|
                                                                       =======''','''




















                                                                          _
                                                                         / \\
                                                                         | |
                                                                         |_|
                                                                          |
                                                                          #
                                                                          #
                                                                        | ##|
                                                                        |###|
                                                                       =======''','''


















                                                                          _
                                                                         / \\
                                                                         | |
                                                                         |_|
                                                                          |
                                                                          #
                                                                          #
                                                                          #
                                                                          ##
                                                                        |###|
                                                                        |###|
                                                                       =======''','''
















                                                                          _
                                                                         / \\
                                                                         | |
                                                                         |_|
                                                                          |
                                                                          #
                                                                          #
                                                                          #
                                                                          #
                                                                          #
                                                                          ##
                                                                        |###|
                                                                        |###|
                                                                       =======''','''









                                                                               
                                                                        '    '
                                                                    \\   '    .'    / 
                                                                 '     "\\  .'" ,    '
                                                              ' . \\  " \\ / / .:'     .
                                                              ' .  :' \\ '! |'./,  '
                                                             ---  --  - ~>o<:- - - _' - 
                                                                 '   " %.'^ \\, \\' ; .
                                                                    /  ' / \\ \\' , .  
                                                                '       /  #  ' "  _ \\
                                                                    /     |      \\ 
                                                                               '
                                                                          #
                     
                                                                          #
                                                                          #
                                                                          #
                                                                          ##
                                                                        |###|
                                                                        |###|
                                                                       =======''','''









                                                                               
                                                                        '    '
                                                                    \\   '    .'    / 
                                                                 '     "\\  .'" ,    '
                                                              ' . \\  " \\ / / .:'     .
                                                              ' .  :' \\ '! |'./,  '
                                                             ---  --  - ~>o<:- - - _' - 
                                                                 '   " %.'^ \\, \\' ; .
                                                                    /  ' / \\ \\' , .  
                                                                '       /  #  ' "  _ \\
                                                                    /     |      \\ 
                                                                               '
                                                                          #
                     
                                                                          #
                                                                          #
                                                                          #
                                                                          ##
                                                                        |###|
                                                                        |###|
                                                                       =======''']
gameover = '''














  ________        __      __        __  ________         _________               _________   ______
 /               /  \\     | \\      / |  |               /         \\  \\        /  |          |      \\
/               /    \\    |  \\    /  |  |               |         |   \\      /   |          |______/
|        ___   /______\\   |   \\  /   |  |___            |         |    \\    /    |___       |   \\
\\          |  /        \\  |    \\/    |  |               |         |     \\  /     |          |    \\
 \\_________| /          \\ |          |  |_______        \\_________/      \\/      |________  |     \\




















'''
hangman = '''
 +---+
 0   |
/|\\  |
/ \\  | 
==========='''

if difficulty == "5":
  pdifficulty = 5
elif difficulty == "10":
  pdifficulty = 10
elif difficulty == "15":
  pdifficulty = 15  
else:
  print("That is not a valid choice.")
  pdifficulty = 0

mWord = random.choice(wList)
mWordList = list(mWord)
for length in mWordList:
  cList.append("_")

while pdifficulty >= 0:
  letterPlace = 0
  print(hangman)
  print(cList)
  print("Misses:" + str(mList))
  print("Tries remaining: " + str(pdifficulty))
  if cList == mWordList:
    if len(mList) == 0:
      print("You played a perfect game, congradulations.")
      for i in range(3):
        for frame in pgame:
          os.system("cls")
          print(frame)
          time.sleep(0.2)
    else:
      print("You guessed it! The word was " + mWord + "." )
    break
  elif pdifficulty == 0:
    os.system("cls")
    print(gameover)
    print("GAME OVER")
    break
  else:  
    guess = input("Guess a letter (lowercase): ")
    if guess in mWord:
      print("Correct")
      for place in mWord:
        letterPlace = letterPlace + 1 
        if guess == place:
          cList[letterPlace - 1] = guess
    else:
      print("Try Again")
      pdifficulty = pdifficulty - 1
      mList.append(guess)

