import random

def main():
    print ("Hi, I have numbers for you 'THREE' numbers you should guess this 'THREE' numbers")
    guess()

def guess():
    botnumber1 = random.randint(1,9)
    botnumber2 = random.randint(1,9)
    botnumber3 = random.randint(1,9)
    print ("Ok you should guess first number")
    pfg = int(input())
    if pfg == botnumber1:
        print ("Cool your first guess is correct!")
    else:
        print ("Oh bad your first geuss is incorrect!")
        print ("No problem lets go to second geuss!")
    psg = int(input())
    if psg == botnumber2:
        print ("Thats cool your second guess is correct!")
    else:
        print ("Oh bad your second geuss is incorrect!")
        print ("No problem lets go to third geuss!")
    ptg = int(input())
    if pfg == botnumber3:
        print ("Cool your third guess is correct!")
    else:
        print ("Oh bad your first geuss is incorrect!")
        print ("No problem lets go to final geuss!")
    print ("Ok This is final geuss you should type this 'THREE' number.")
    botnumberf = str(botnumber3) + str(botnumber2) + str(botnumber1)
    ptg = int(input())
    if ptg == botnumberf:
        print ("Cool your guess is correct")
        print ("You win the game")
    else:
        print ("Oh bad your geuss is incorrect")
        print ("You is lose the game")
main()