from random import randrange

print("Welcome to the Random Number Guessing Game!"
      "I will think of a number between 0 and 100, and you have to guess it. ")

gues_this_number = randrange(0, 100)
print(f"Please select the difficulty level: " 
    "1. Easy (10 chances)" 
    "2. Medium (5 chances)" 
    "3. Hard (3 chances )")

setdifficulty = int(input("Choose your difficulty level: "))

if setdifficulty == 1:
    difficulty = 10
elif setdifficulty == 2:
    difficulty = 5
elif setdifficulty == 3:
    difficulty = 3
else:
    print("Invalid difficulty")

for i in range(difficulty):
    guess = int(input("Guess a number between 0 and 100: "))
    if guess > gues_this_number:
        print(f"The number is lower than {guess}")
    elif guess < gues_this_number:
        print(f"The number is higher than {guess}")
    elif guess == gues_this_number:
        print(f"You guessed the correct number wich was: {gues_this_number}.")
        break
    else:
        print(f"Wrong guess, the number was : {gues_this_number}")