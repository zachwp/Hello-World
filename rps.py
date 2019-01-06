import random
def rps():
    inpt = input(": ")
    rps = ["rock" , "paper", "scissors" ]
    comp = random.choices(rps)
    while True:
        if inpt == "rock":
            comp = random.choices(rps)
            print(inpt)
            print(comp)
            inpt = input(': ')
        if inpt == "scissors":
            comp = random.choices(rps)
            print(inpt)
            print(comp)
            inpt = input(': ')
        if inpt == "paper":
            comp = random.choices(rps)
            print(inpt)
            print(comp)
            inpt = input(': ')
        else:
            print("enter rock, paper, or scissors.")
            inpt = input(': ')

rps()


        
    
        
        
