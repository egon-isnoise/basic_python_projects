import random
 
top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0 : 
        print("Please type a number larger than 0 next time....")
        quit()
else:
    print("Please type a number next time...")
    quit()


random_number = random.randint(0, top_of_range)
# print(random_number)

tries = 0

while True:
    tries +=1
    user_guess = input("Make a guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time...")
        continue
    
    if user_guess == random_number:
        print("\nWow!! You got it!")
        break
    elif user_guess < random_number:
        print("\nThe number is bigger!")
    else: print("\nThe number is smaller!")
        
print("It took you", tries,  "tries to guess the correct number")
        