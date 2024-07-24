import random

def rockPaperScissors(user_input, comp):
    rock = "rock"
    paper = "paper"
    scissors = "scissors"

    if((user_input == rock) & (comp == paper)):
        print()
        print("You: ", user_input)
        print("Computer: ", comp)

        print()
        print(paper, "beats ", rock,", computer wins!")
    elif((user_input == paper) & (comp == rock)):
        print()
        print("You: ", user_input)
        print("Computer: ", comp)
        
        print()
        print(paper, "beats ", rock,", you win!")

    elif((user_input == rock) & (comp == scissors)):
        print()
        print("You: ", user_input)
        print("Computer: ", comp)
        
        print()
        print(rock, "beats ", scissors,", you win!")
    elif((user_input == scissors) & (comp == rock)):
        print()
        print("You: ", user_input)
        print("Computer: ", comp)
        
        print()
        print(rock, "beats ", scissors,", computer wins!")

    elif((user_input == paper) & (comp == scissors)):
        print()
        print("You: ", user_input)
        print("Computer: ", comp)
        
        print()
        print(scissors, "beats ", paper,", computer wins!")
    elif((user_input == scissors) & (comp == paper)):
        print()
        print("You: ", user_input)
        print("Computer: ", comp)
        
        print()
        print(scissors, "beats ", paper,", you win!")

    elif((user_input == rock) & (comp == rock)):
        print()
        print("You: ", user_input)
        print("Computer: ", comp)
        
        print()
        print(rock, "draws with ", rock)
    elif((user_input == paper) & (comp == paper)):
        print()
        print("You: ", user_input)
        print("Computer: ", comp)
        
        print()
        print(paper, "draws with ", paper)
    elif((user_input == scissors) & (comp == scissors)):
        print()
        print("You: ", user_input)
        print("Computer: ", comp)
        
        print()
        print(scissors, "draws with ", scissors)

list = ["rock","paper","scissors"]
comp = random.choice(list)
index = 0

#-------------PART 2-------------PART 2-------------PART 2-------------PART 2-------------PART 2-------------PART 2-------------PART 2-------------PART 2
#========================================================================================================================================================
print()
response = input("Would you like to play a game or Rock, Paper, Scissors?: 'Y' for yes, 'N' for no:   " ).upper()
while(response != "Y"  and response != "N" and index != 2):
    print()
    response = input("Would you like to play a game or Rock, Paper, Scissors?: 'Y' for yes, 'N' for no:     " ).upper()
    index += 1
    if index == 2:
        break

while response == "Y":
    print()
    user = input("Rock, Paper, Scissors, Shoot! :  ").lower()
    rockPaperScissors(user, comp)
    print()
    response = input("Would you like to play another game or Rock, Paper, Scissors?: 'Y' for yes, 'N' for no:   " ).upper()
else:
    print()
    print("See you next time!")
