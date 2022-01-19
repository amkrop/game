from math import e
import random

randomOption = ["rock","paper","scissors"]
computerOption =  random.choice(randomOption)
playerOption = None
quitingTheGame = None


    
while True :
    quitingTheGame = input("type 'Y' if you want to continue: ").strip().upper()
    if quitingTheGame == "":
        print('please write rock paper or scissors')
    elif quitingTheGame != "Y":
        break
    elif quitingTheGame == "Y":
        print("it's wo")
        playerOption = input("choose rock, paper or scissors: ").lower().strip()
        if playerOption == computerOption:
                print("tie!!!!!")
                print("player__",playerOption) 
                print("computer__",computerOption)
                continue 
        elif playerOption == "rock":
            if computerOption == "paper":
                print("you lose")
                print("player__",playerOption) 
                print("computer__",computerOption)
                continue
            else:
                print("you win")
                print("player__",playerOption) 
                print("computer__",computerOption)
                continue
        elif playerOption == "paper":
            if computerOption == "scissors":
                print("you lose")
                print("player__",playerOption) 
                print("computer__",computerOption)
                continue
            else:
                print("you win")
                print("player__",playerOption) 
                print("computer__",computerOption)
                continue
        elif playerOption == "scissors":
            if computerOption == "rock":
                print("you lose")
                print("player__",playerOption) 
                print("computer__",computerOption)
                continue
            else:
                print("you win")
                print("player__",playerOption) 
                print("computer__",computerOption)
                continue    
       
    