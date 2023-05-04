import random

def roll_dice():
    """Roll two dice and return their sum."""
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

def play_game():
    """Play one round of the game."""
    roll = roll_dice()
    if roll == 7 or roll == 11:
        print("You win!")
    elif roll == 2 or roll == 3 or roll == 12:
        print("You lose!")
    else:
        print("Your goal is", roll)
        while True:
            roll = roll_dice()
            if roll == 7:
                print("You lose!")
                break
            elif roll == goal:
                print("You win!")
                break

# Main program starts here

while True:
    input("Press Enter to roll the dice...")
    roll = roll_dice()
    if roll == 7 or roll == 11:
        print("You win!")
    elif roll == 2 or roll == 3 or roll == 12:
        print("You lose!")
    else:
        print("Your goal is", roll)
        goal = roll
        play_game()
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != "y":
        break
print("Thanks for playing!")