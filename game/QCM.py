from ast import Break
import datetime
from time import time


questoins = {
    "A":"what's the first pres of the us",
    "B":"How many states in the us ",
    "C":"what's the capital of the us ",
    "D":  "what's the official language in the us "
}

options = [
    ["A.Gearge Washington","B.3.F.K","C.Obama","D.Lincon"],
    ["A.50","B.55","C.35","D.53"],
    ["A.California","B.Las Vegas","C.Washington DC"],
    ["A.Spanish","B.Arabic","C.French","D.English"]
]

def test():    
    
    guesses = []
    count = 0
    # def time_limit():
    #     now =datetime.datetime.now()
    #     timee = datetime.timedelta(seconds= +5)
    #     deadline = now+timee
    #     print(f'you started at {now} and you will finish at {deadline}')
    #     while True:
    #         if  datetime.datetime.now()> deadline   :
                
    #             break

    def check_answers():
        if guesses[0] != "A":
            print("the question number 1 is false!")  
        elif guesses[0] == "A":
            print("the question number 1 is correct !")
        
        if guesses[1] != "A":
            print ("the question number 2 is false!") 
        elif guesses[1] == "A":
            print("the question number 2 is correct !")
        
        if guesses[2] != "C":
            print ("the question number 3 is false!") 
        elif guesses[2] == "C":
            print("the question number 3 is correct !")
        
        if guesses[3] != "D":
            print("the question number 4 is false!") 
        elif guesses[3] == "D":
            print("the question number 4 is correct !")
    
    def record_score():
        
        grade = 0

        if guesses[0] == "A":
            grade += 1
        if guesses[1] == "A":
            grade += 1
        if guesses[2] == "C":
            grade += 1
        if guesses[3] == "D":
            grade += 1
        print(f"your grade is {grade}/4")
    
    for q in questoins.items():
        print(f"{q[0]} _ {q[1]}")
        
        for item in options[count]:
            print(f"{item}")        
        count += 1
        answers = input("what's the answer (A,B,C OR D) : ").upper()
        guesses += answers
    
    print(len(guesses))
    # time_limit()
    check_answers()
    record_score()
    print("_____________________________________________________")
    
    
test()           
















        
        

