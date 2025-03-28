import time
import random

name = input("WHAT IS YOUR NAME? ")
print(f"HELLO {name}, Time to play Rock, Paper, Scissors!")
time.sleep(1)
print("YOU HAVE 3 CHANCES TO PLAY")
time.sleep(0.5)
choices = ['rock', 'paper', 'scissors']
turns = 3

while turns > 0:
    print("\nROCK, PAPER, SCISSORS...")
    time.sleep(0.5)
    choice = input("ENTER YOUR CHOICE: ").lower()
    computer_choice = random.choice(choices)

    print(f"Computer chose: {computer_choice}")

    if choice == computer_choice:
        print("It's a tie!")
    elif (choice == 'rock' and computer_choice == 'scissors') or \
         (choice == 'scissors' and computer_choice == 'paper') or \
         (choice == 'paper' and computer_choice == 'rock'):
        print("Congratulations, you won!")
    elif choice not in choices:
        print("Invalid choice! Choose rock, paper, or scissors.")
        continue
    else:
        print("Oops, you lost this round!")

    turns -= 1
    print(f"Turns left: {turns}")

    if turns == 0:
        print("\nGame Over! Better luck next time.")
