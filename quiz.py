print("Welcome to my first Python game!")

playing = input("\nDo you wanna play? ")

if playing.lower() != "yes":
    print("Ok.....bye :((")
    quit()
    
print("Okay! Let's play then :)")
score = 0

answer1 = input("\nWhat does CPU stand for? ")
if answer1.lower()  == "central processing unit":
    print("\nCorrect!")
    score +=1
else:
    print("\n___Wrooooooong___")
    


answer2 = input("\nWhat does GPU stand for? ")
if answer2.lower()  == "graphics processing unit":
    print("\nCorrect!")
    score +=1
else:
    print("\n___Wrooooooong___")
    
    
    
answer3 = input("\nWhat does RAM stand for? ")
if answer3.lower()  == "random access memory":
    print("\nCorrect!")
    score +=1
else:
    print("\n___Wrooooooong___")
    
    
    
answer4 = input("\nWhat does PSU stand for? ")
if answer4.lower()  == "power supply":
    print("\nCorrect!")
    score +=1
else:
    print("\n___Wrooooooong___")
    
    

print("\nYou got " + str(score) + " questions correct! That means " + str(int((score/4) *100)) + "%!")

if score == 4:
    print("\nCongrats!")
    
else:
    print("\nYou can always try again....\n")