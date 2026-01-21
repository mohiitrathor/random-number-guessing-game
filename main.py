import random

def Game_logic():
    count = 0
    number = random.randint(1, 10)
    guess = None
    print("You only have 3 chances")
    while guess != number and count < 3:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        count += 1
        if guess < number:
            print("Your guess is smaller than the number")
        elif guess > number:
            print("Your guess is greater than the number")
        else:
            print("Congratulations! You guessed it!")
        print(f"You have {3 - count} chances left")
    if guess != number:
        print("You ran out of chances :(")
        print(f"The number was {number}")

    print("Play again?")
    res=str(input("Y/N: "))
    if res=="Y" or res=="y":
        Game_logic()
    elif res=="N" or res=="n":
        print("Thanks for playing")
    else:
        print("Invalid input")

print("Play random number guessing game?")
response=str(input("Y/N: "))
if response=="Y" or response=="y":
    Game_logic()
elif response=="N" or response=="n":
    print("Player left")
else:
    print("Invalid input")