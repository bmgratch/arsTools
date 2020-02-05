# arsRoll.py - a die rolling module for Ars Magica uses

# All the simulations could be done with random.randint()
from random import randint


def roll(b=0):
    roll = randint(0,9)
    #TODO botch dice. not needed for aging
    # processing exploding dice
    mult = 1
    while roll == 1:
        mult *= 2 # double on a 1, roll again
        roll = randint(1, 10)
    return(roll * mult)
