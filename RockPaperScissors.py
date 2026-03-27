import random 
global score 


# 1. make score variable accessible in the roshambo function
# 2. 

weaponwheel = ("Rock","Paper", "Scissors")
score = 0
win_var = False

def tutorial():
    print("Hello, Welcome to rock, paper, scissors, shoot!")

def play():
    play_time = ""  # Initialize play_time variable
    while play_time.strip().capitalize() != "No":
        play_time = input("Let's play! Type 'No' to quit: ").strip().capitalize()
        if play_time == "No":
            print("Thanks for playing!")
            print(f"Your final score is: {score}")
            break

        print(f"Pick your weapon: {weaponwheel}")
        user_weapon = ""
        while user_weapon not in weaponwheel:
            user_weapon = input("Which weapon do you choose to wield: ").capitalize()

        opp_weapon = random.choice(weaponwheel)
        roshambo(user_weapon, opp_weapon) 

        

def roshambo(user_weapon, opp_weapon):
    #Basic game mechanics using non global attributes from the play mechanic
    print(f"You picked: {user_weapon}")
    print(f"Opponent picked: {opp_weapon}")

    if user_weapon == opp_weapon:
        print("It is a tie draw again!")
    elif user_weapon == "Rock" and opp_weapon =="Paper":
        print("YOU LOSE!")
    elif user_weapon == "Scissors" and opp_weapon =="Rock":
        print("YOU LOSE!")
    elif user_weapon == "Paper" and opp_weapon =="Scissors":
        print("YOU LOSE!")
    else:
        print("YOU WIN!")
        win_var = True
        return win_var 

print(win_var)

def score():
    score = 0
    if win_var == True:
        score += 1
        return score 


play()