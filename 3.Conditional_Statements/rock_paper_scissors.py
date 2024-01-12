"""
Rock Paper Scissors

User guess = rock/paper/scissors
Computer_guess = rock/paper/scissors


If user wins -> You won
if user lose = You lost, computer guessed rock

You tied
"""
import random

options = ["rock", "paper", "scissors"]
computer_guess = random.choice(options)
user_guess = input("Enter rock/paper/scissors = ")

# IF elif elif......
if (
    (user_guess == "rock" and computer_guess == "scissors")
    or (user_guess == "paper" and computer_guess == "rock")
    or (user_guess == "scissors" and computer_guess == "paper")
):
    print("You won")
elif user_guess == computer_guess:
    print("Tie")
else:
    print(f"You lost, computer guess was {computer_guess}")
