import random

#List of tools to use during the game
tool_list = ["rock","paper", "scissors",]
userInput = input("Press N to quit, press Y to play: ")

if userInput == "y":
    print("Pick a tool to use! or press 'Q' to quit")
    usertool = input("1. Rock \n2. Paper \n3. Scissors\n ")

    while usertool.upper() != "Q":
        pctool = random.choice(tool_list)
        print(pctool)
        if usertool == "1":
            print("You picked rock")
            if pctool == "rock":
                print("You have drawn")
            elif pctool == "paper":
                print("Youve lost")
            else:
                print("WiN")
            break

        if usertool == "2":
            print("You picked paper")
            if pctool == "paper":
                print("You have drawn")
            elif pctool == "scissors":
                print("Youve lost")
            else:
                print("WiN")
            break

        if usertool == "3":
            print("You picked scissors")
            if pctool == "scissors":
                print("You have drawn")
            elif pctool == "rock":
                print("Youve lost")
            else:
                print("WiN")
            break

    print("Pick a tool to use! or press 'Q' to quit")
    usertool = input("1. Rock \n2. Paper \n3. Scissors\n ")

    userInput = input("Press N to quit, press Y to play: ")

elif userInput != "n":
     print("Please enter a valid letter")
else:
    print("Thanks for playing!")
