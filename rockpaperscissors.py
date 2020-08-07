from random import *

wins = 0
draws = 0
defeats = 0

possibilities = ["rock", "paper", "scissors"]

def findlist(element):
    for id, elem in enumerate(possibilities):
        if (element == elem):
            return id

def roundfunc():
    global rounds
    while True:
        try:
            rounds = int(input('Write down a num'))
            break
        except ValueError:
            print("Type down a num")
    finalfunc()

def finalfunc():
    global rounds, wins, draws, defeats
    while 0 != rounds:
        while True:
            yourmove = input('Rock paper or scissors')
            if not yourmove in possibilities:
                yourmove = input('Rock paper or scissors')
            else:
                break
        pcmove = choice(possibilities)
        print(pcmove)
        if findlist(yourmove) - findlist(pcmove) == 0:
            rounds -= 1
            draws += 1
            print('It is a draw')
        elif findlist(yourmove) - findlist(pcmove) == 1 or findlist(yourmove) - findlist(pcmove) == -2:
            rounds -= 1
            wins += 1
            print('You won')
        else:
            rounds -= 1
            defeats += 1
            print('You lost')


roundfunc()