#! python3
# ars-age.py - a program to calculate aging rolls for grogs and covenfolk
#

<<<<<<< Updated upstream
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
=======
import random, math, shelve
grogFile = shelve.open('grogs')

def ageSimple(grog, years=1):       # grog is a grog dict, years are number of years to age
    count = 0                       # Counter to track number of times done
    mod = grog['ritual'] + grog['age mod']
    grog['history'] = []            # clear history for easier reading
    while count < years:
        grog['age'] += 1            # first age up
        mod = math.ceil(grog['age'] // 10 + mod) # generate age-based penalty

        die = arsRoll() + mod           # roll a die, add mod
        #print('Aging Roll(' + str(die) + ') at mod ' + str(mod))  #debug
        if die <= 2:
            grog['appAge'] -= 1
            #print('No aging!')      # debug
            grog['history'].append('No apparent aging / ' + str(die))
        elif die <= 9:
            #print('Aged')           # debug
            grog['history'].append('Aged / ' + str(die))
        elif die == 13:
            #print('Age! Crisis!')   #debug
            grog['pointAge'] = crisis(grog['pointAge'])
            grog['history'].append('Crisis! / ' + str(die))
            grog['ritual'] = 0
        elif die <= 17:
            #print('Aged, old!')     # debug
            grog['pointAge'] += 1
            grog['history'].append('Aged in stat! / ' + str(die))
        elif die <= 21:
            #print('Aged, rather old!')  # debug
            grog['pointAge'] += 2
            grog['history'].append('Aged in two stats / ' + str(die))
        else:
            #print('Aged aged crisis!')  # debug
            grog['pointAge'] = crisis(grog['pointAge'])
            grog['history'].append('Crisis! / ' + str(die))
            grog['ritual'] = 0
        count += 1
    return(grog)
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream

##for n in range(10):
##    print(arsRoll())

for n in range(10):
    print(ageSimple(sampleGrog, 0))
    print('\n')
=======
sampleGrog = {
    'name' : "Tyro",
    'age' : 40,
    'appAge' : 0,
    'pointAge' : 1,     
    'age mod' : 0,
    'ritual': -8,
    'history': [] }

def displayGrog(grog):
    print('Name: ' + grog['name'])
    if grog['ritual'] < 0:      # only print ritual if there is a ritual
        print('Age: %s (%s) [LR %s]' % (grog['age'] + grog['appAge'], grog['age'], str(grog['ritual'])))
    else:
        print('Age: %s (%s)' % (grog['age'] + grog['appAge'], grog['age']))
    if grog['pointAge'] > 0:    # only print decrepitude if aging poitns exist
        decr = math.floor(((math.sqrt(8*(grog['pointAge']/5)+1)-1)/2)) # decrepitude = ((sqrt(8*(ap/5)+1)-1)/2)
        print('Decrepitude: %s (%s)' % (str(decr), grog['pointAge']) )
    if len(grog['history']) > 0:    # only print history if there is history
        print('Aging History:')
        for x in grog['history']:
            print('* ' + x)
    print('\n')

##displayGrog(sampleGrog)
##
##ageSimple(sampleGrog, 1)
##displayGrog(sampleGrog)
##
##ageSimple(sampleGrog, 5)
##displayGrog(sampleGrog)
##
##ageSimple(sampleGrog, 0)
displayGrog(sampleGrog)

grogFile.close()
>>>>>>> Stashed changes
