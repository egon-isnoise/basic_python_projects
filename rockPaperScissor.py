import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("\nType Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
        
    if user_input not in ["rock", "paper", "scissors"]:
        continue
    
    random_number = random.randint(0,2)
    # rock 0, paper 1, scissors 2
    
    computer_pick = options[random_number]
    print("Computer picked " + computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissors":
        print("\nYou won!")
        user_wins +=1
    
    elif user_input == "paper" and computer_pick == "rock":
        print("\nYou won!")
        user_wins +=1
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("\nYou won!")
        user_wins +=1
        
    elif user_input == computer_pick:
        print("\nIt's a tie!")
        
    else:
        print("\nYou lost!")
        computer_wins +=1
    
print("\nYou won " +str(user_wins)+ " times and the computer won " +str(computer_wins)+ " times.")    

if user_wins > computer_wins:
    print("\nYOU are the winner!!")
elif user_wins < computer_wins:
    print("\nComputer is the winner!!")
else:
    print("\nIt's a TIE!!")
    
print("\nGoodbye!!")
