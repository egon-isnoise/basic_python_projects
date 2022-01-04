name = input("Type your name: ")
print("Welcome, "+name+ ", to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. \nWhich way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross. \nType 'walk' or 'swim'.").lower()
    if answer == "swim":
        print("You swam accross and got eaten by an alligator! \nYou lost!")       
    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game!")   
    else:
        print("Not a valid option, you lose.")
           
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, to you want to cross it or walk back? \nType 'cross' or 'back'.").lower()
    if answer == "back":
        print("You go back to the main road and lose 'cause you are a wussy!")

    elif answer == "cross":
        answer = input("You meet a stranger, do you wanna talk to them? Type 'Yes' or 'No'.").lower()
        if answer == "yes":
            print("Great! You make a new friend! You win!!")
        elif answer == "no":
            print("So rude! You lose!")
        else:
            print("Not a valid option, you lose.")  
    else:
        print("Not a valid option, you lose.")      
else:
    print("Not a valid option, you lose.")
    
print("Thank you for trying, "+name+", till next time!")
quit()
