#import random
#number = random.randint(1,0) #random integer
#random.random() - random float from 0 to <1
#random.random() * 10 #andom float within the supplied range
#random_heads_or_tails = random.randint(0,1) #Gives either 0 or 1 randomly.
#if random_heads_or_tails == 0:
    #print("heads")
#else:
    #print("tails")

import random

print("Welcome to the Rock, Paper, Scissor Game")
choices = ["Rock", "Paper", "Scissor"]

user_choice = (input("What do you chose? ")).capitalize()

computer_choice = random.randint(0,2)
computer_choice = choices[computer_choice]

print("You chose: ", user_choice)
print("Computer chose: ", computer_choice)

if user_choice == computer_choice:
    print("It's a draw")

elif user_choice == "Rock" and computer_choice == "Scissor":
    print("User wins")

elif user_choice == "Paper" and computer_choice == "Scissor":
    print("Computer Wins")

elif user_choice == "Scissor" and computer_choice == "Paper":
    print("User Wins")

elif user_choice == "Rock" and computer_choice == "Paper":
    print("Computer Wins")

elif user_choice == "Paper" and computer_choice == "Rock":
    print("User wins")

elif user_choice == "Scissor" and computer_choice == "Rock":
    print("Computer wins")
else:
    print("Computer Wins")