#! python3
# ars-age.py - a program to calculate aging rolls for grogs and covenfolk
#

import random

sampleGrog = {
    'name' : "Tyro",
    'age' : 40,
    'appAge' : 0,
    'pointAge' : 0,
    'history': []}

def ageSimple(grog, mod=0):
    sampleGrog['age'] += 1          # first age up
    if grog['age'] % 10 == 0:       # generate age-based penalty
        mod = grog['age'] // 10 + mod
    else:
        mod = grog['age'] // 10 + 1 + mod
    die = arsRoll() + mod           # roll a die, add mod
    print('Aging Roll(' + str(die) + ') at mod ' + str(mod))
    if die <= 2:
        sampleGrog['appAge'] -= 1
    elif die <= 9:
        print('Aged')
    elif die == 13:
        print('Age! Crisis!')
        sampleGrog['pointAge'] = crisis(sampleGrog['pointAge'])
    elif die <= 17:
        print('Aged, old!')
        sampleGrog['pointAge'] += 1
    elif die <= 21:
        print('Aged, rather old!')
        sampleGrog['pointAge'] += 2
    else:
        print('Aged aged crisis!')
        sampleGrog['pointAge'] = crisis(sampleGrog['pointAge'])
    return(sampleGrog)

def arsRoll(b=0):
    roll = random.randint(0,9)
    # TODO process botch
    # process explode
    mult = 1
    while roll == 1:
        mult *= 2
        print('explode! x' + str(mult)) # for testing
        roll = random.randint(1, 10)
    print('rolled d10: ' + str(roll))
    return(roll * mult)

# need some way to check decrepitude for increasing
def crisis(ap):
    # formula ((sqrt(8*(ap/5)+1)-1)/2)
    if ap < 5:
        return(5)
    elif ap < 15:
        return(15)
    elif ap < 30:
        return(30)
    elif ap < 50:
        return(50)
    elif ap < 75:
        return(75)
    else:
        return(105)
    

#### for testing

##for n in range(10):
##    print(arsRoll())

for n in range(10):
    print(ageSimple(sampleGrog, 0))
    print('\n')
