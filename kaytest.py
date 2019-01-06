import time
import datetime
import random

def kay_func():
    tester = str(input("What should i call you:"))
    print(tester, "This is a simulated assistant, Hello my name is Kay")

    def kay_func1():
        print("current date and time is:", datetime.datetime.now())
        x = "What can i do for you, type"
        y = "\'insort\' to sort some numbers, type \'rps\' for rock paper"
        z = "scissor's, type \'isprime\' to id prime numbers: "
        task = str(input(x + y + z))

        def in_sort():
            f = list(input('Enter some numbers no commas no spaces: '))
            d = list(input('Enter some more numbers no commas no spaces: '))
            c = f+d
            list.sort(c)
            print(c)
            kay_func1()

        def f():
            x = int(input("Enter a whole number > 2, type 0 to return: "))
            if x == 0:
                kay_func1() 
            for i in range(2, x):
                if x % i == 0 and i != x:
                    print('not prime')
                    f()
            else:
                print('prime')
                f()

        def rps_func():
            print("type \'end\' to return, playing rps type rock, paper, or scissors.")
            inpt = input(": ")
            rps = ["rock" , "paper", "scissors" ]
            comp = random.choices(rps)
            while True:
                if inpt == "rock":
                    comp = random.choices(rps)
                    print(inpt)
                    print(comp)
                    inpt = input(': ')
                elif inpt == "scissors":
                    comp = random.choices(rps)
                    print(inpt)
                    print(comp)
                    inpt = input(': ')
                elif inpt == "paper":
                    comp = random.choices(rps)
                    print(inpt)
                    print(comp)
                    inpt = input(': ')
                elif inpt == "end":
                    kay_func1()
                else:
                    print("enter rock, paper, or scissors.")
                    inpt = input(': ')

        if task == "insort":
            in_sort()
        elif task == "rps":
            rps_func()
        elif task == "isprime":
            f()
    kay_func1()

kay_func()
    