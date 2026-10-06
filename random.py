# Rock paper scissors

Moves = ["Rock", "Paper", "Scissors"]
import time
import random

print("Hello!")
time.sleep(0.5)
print("Let's play ROCK PAPER SCISSORS!")
time.sleep(0.5)
print("Lets go!")
time.sleep(0.5)
PlayerMove = input("State your move! (only use Rock, Paper, or Scissors): ")

if PlayerMove == "Rock":
    print("registered")
elif PlayerMove == "Paper":
    print("registered")
elif PlayerMove == "Scissors" or "Scissor":
    print("registered")
else:
    