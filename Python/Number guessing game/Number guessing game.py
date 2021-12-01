# ------------------------------
# Number guessing game
# This game has 2 game modes:
# 1. Two player mode
#   In this game mode, the first player inserts a number and the second player has to guess it.
#   Extra information will be given to guide the player to guess the right number within 3 tries.
#
# 2. Player Vs Computer
#   In this game mode, the computer chooses a number and the player has to guess it.
#   Extra information will be given to guide the player to guess the right number within 3 tries.
# ------------------------------

import random
from primePy import primes

def help():
    print("""
              Simply insert a number and see if was correct or not.
              for seeing that how many times more you're allowed to guess, type 'chances'.
              For seeing the inserted clues, type 'clue'
              To give up, type 'surrender'.
          """)

def chances():
    pass

def clue():
    print(f"""The number you're looking for has {len(num)} digits.\n
                  It is bigger that {num-5} and bigger than {num+5}.\n
                  And also this number is dividable by {divisiblity(num)}.\n
                  For the last tip, is {odd(num)}.\n
                  ...\n
                  ok, a bonus tip.\n
                  The number before the following series of numbers is the one you're looking for:{number_series(num)}.
                  Hope the tips helped! """)

gamemode = str(input("Enter the gamemode(pvsp, pvsc): "))

if gamemode == "pvsp":
    num = int(input("Enter the number: "))
    p_clue = str(input("Enter a clue to guide the second player: "))
elif gamemode == "pvsc":
    num = int(random.randrange(1,100))

def kind(num):
    if num // 2 == 0:
        return "Even"
    else:
        return "Odd"

def area(num):
    if num < 0:
        return "Negative"
    else:
        return "Positive"

def divisiblity(x):
    for i in range(1,10):
        if x % i == 0:
            return i
    else:
        return None

def odd(x):
    if primes.check(x) == True:
        return "an odd number"
    else:
        return "not an odd number"

def number_series(x):
    serie = list()
    y = x + 5
    while y != x:
        z = y + 15
        serie.append(z)
        y -= 1
    else:
        return serie
        
chance = 4

while chance > -1:
    if chance == 4:
        print(f"""---------------------------------------
                Welcome to the number guessing game!
                You have {chance-1} chances left. use them wisely.
                for seeing that how many times more you're allowed to guess, type 'chances'.
                For seeing the inserted clues, type 'clue'
                To give up, type 'surrender'.
                The number you have to guess is bigger than {num-10} and smaller than {num+10}
                It also is a {area(num)} number.
                Now, What number is it?
                """)
    else:
        continue
    
    if chance == 4:
        guess = input("What's your guess? ")
    else:
        guess = input("Give it another shot ")
    
    if guess == num:
        print("Congradulations! You guessed the correct number!")
        break
    
    elif guess != num:
        print(f"Sorry, but {guess} not the right number. Try again")
        chance -= 1
        del(guess)
        
    if type(guess) == str and guess == "surrender":
        print(f"Well, ok then. The number was {num}. \nBetter luck next time!")
        del(guess)
        chance == -1
    
    if chance == 1:
        print("Be careful, This is you last chnace!")
        
    
    if type(guess) == str and guess == "clue": 
        if input("Gwtting a clue costs you a chance, are you sure? (Y/N)") == "Y": 
            print(clue())  
            if clue != None: print(f"And here's the clue that player one wrote: {p_clue}")
            chance -= 1
        elif guess == "N":
            print("Ok then, back to the game!")
            continue
    
    if type(guess) == str and guess == "chances" and chance != 1:    
        print (f"You have {chance} chances left")
    else:
        print("You only have one chance left...")
    
    if chance == 0:
        print(f"Sorry but you lost! \nyou ran out of chances. \nThe number was {num}")
        del(guess)
        break  
else:
    print("The game has finished. \nThanks for playing! \nIf you want to play again, restart the app")

