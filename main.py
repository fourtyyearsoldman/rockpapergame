#THIS IS MY ROCK PAPER SCISSORS GAME
import random
value_order = ["rock", "paper", "scissors"]
userinput = input("Enter rock, paper, or scissors: ").lower()
if userinput not in value_order:
    print("Invalid input. Please enter rock, paper, or scissors.")
    exit()
computer_choice = random.choice(value_order)
print(f"Computer chose: {computer_choice}")
if userinput == computer_choice:
    print("It's a tie!")
elif (userinput == "rock" and computer_choice == "scissors") or \
     (userinput == "paper" and computer_choice == "rock") or \
     (userinput == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("Computer wins!")
