import random

#List of tools to use during the game
tool_list = ["rock","paper", "scissors",]
comp_tool = random.choice(tool_list)

comp_tool = comp_tool.capitalize
userInput = input(f"Press N to quit, press Y to play: ")

while userInput.lower() == "n":
        print("Please enter Y or N")
        userInput = input("Press N to quit, press Y to play: ")

print(" 1. Rock \n 2. Paper \n 3.Scissors")
user_tool = input("Choose your weapon: ")
while user_tool == "n":
    print("Thanks for playing")
    break
#Rock ending       
if user_tool == 1:
                print("You picked Rock")
                print("I picked "+ comp_tool)
                if comp_tool.lower == "rock":
                    print("It's a Draw!")
                elif comp_tool.lower == "paper":
                    print("You Lose!")
                else:
                    print("You Win!")

#Paper ending
if user_tool == 2:
                print("You picked Paper")
                print("I picked "+ comp_tool)
                if comp_tool.lower == "paper":
                    print("It's a Draw!")
                elif comp_tool.lower == "scissors":
                    print("You Lose")
                else:
                    print("You Win")

#Scissors ending
if user_tool == 3:
                print("You picked Paper")
                print("I picked "+ comp_tool)
                if comp_tool.lower == "scissors":
                    print("It's a Draw!")
                elif comp_tool.lower == "rock":
                    print("You Lose")
                else:
                    print("You Win")
                

