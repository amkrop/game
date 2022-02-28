import random

randomOption = ["rock","paper","scissors"]
computerOption =  random.choice(randomOption)
playerOption = None
quitingTheGame = None


    
while True :
    quitingTheGame = input("type 'Y' if you want to continue and enything else to quit: ").strip().upper()
    if quitingTheGame == "":
        print('please write rock paper or scissors')
    elif quitingTheGame != "Y":
        break 
    elif quitingTheGame == "Y":
        print("it's wo")
        playerOption = input("choose rock, paper or scissors: ").lower().strip()
        if playerOption == computerOption:
                print("tie!!!!!")
        elif playerOption == "rock":
            print("you win") if computerOption == "scissor" else print("you lose") 
        elif playerOption == "paper":
            print("you win") if computerOption == "rock" else print("you lose") 
        elif playerOption == "scissors":
             print("you win") if computerOption == "paper" else print("you lose") 
    else:
        print("please check your commands!!")
       
    