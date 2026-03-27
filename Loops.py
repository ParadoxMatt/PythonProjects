import random 

#while Loops will run as a condition remains true/false 
name = input("Enter your name: ")
while name == "":
    print("Please enter your name")
    name = input("Enter your name: ")


#game 
play = input("Guess the Number!\nPress Y to play and N to stop: ")
score = 0 
guesscount = 1
while play.lower() != "n":
    #Scoring system
    Num= random.randint(1,100)
    userGuess = input("guess the number: ")
    if userGuess.lower() == "n":
        break
    elif userGuess == "":
        print("Please use a valid input!")
    else:
        userGuess = int(userGuess)
        while userGuess != Num:
    #check where num is between 1 and 50
            guesscount +=1
            if userGuess == "":
                print("Please use a valid input!")
            elif userGuess < Num:
              print("Your number is LESS than my number!\n   Try Again!  ")
            elif userGuess > Num:
             print("Your number is MORE than my number!\n   Try Again!  ")
            userGuess = input("guess the number: ")
            userGuess = int(userGuess)
        print("Congratulations! You got it right")
        score += 1
        print(f"Hello {name} your score is {score} \n The number of guesses taken is {guesscount}")
        play = input("Guess the Number!\nPress Y to play and N to stop: ")
        guesscount = 0

if type(userGuess) == str:
   print("Please use a valid ")