#! python3
# ars-age.py - a program to calculate aging rolls for grogs and covenfolk
#

import random, math, shelve
grogFile = shelve.open('grogs')

def ageSimple(grog, years=1):       # grog is a grog dict, years are number of years to age
    count = 0                       # Counter to track number of times done
    mod = grog['ritual'] + grog['ageMod']
    history = []
    while count < years:
        grog['age'] += 1            # first age up
        grog['appAge'] += 1
        mod = math.ceil(grog['age'] // 10 + mod) # generate age-based penalty

        die = arsRoll() + mod           # roll a die, add mod
        #print('Aging Roll(' + str(die) + ') at mod ' + str(mod))  #debug
        if grog['age'] < 35:
            if die <= 2:
                grog['appAge'] -= 1
                grog['history'].append('No apparent aging / ' + str(die))
                history.append('No apparent aging / ' + str(die))
        if die <= 2:
            grog['appAge'] -= 1
            grog['history'].append('No apparent aging / ' + str(die))
            history.append('No apparent aging / ' + str(die))
        elif die <= 9:
            grog['history'].append('Aged / ' + str(die))
            history.append('Aged / ' + str(die))
        elif die == 13:
            grog['pointAge'] = crisis(grog['pointAge'])
            grog['history'].append('Crisis! / ' + str(die))
            history.append('Crisis / ' + str(die))
            grog['ritual'] = 0
        elif die <= 17:
            grog['pointAge'] += 1
            grog['history'].append('Aged in stat! / ' + str(die))
            history.append('Aged in stat! / ' + str(die))
        elif die <= 21:
            grog['pointAge'] += 2
            grog['history'].append('Aged in two stats / ' + str(die))
            history.append('Aged in two stats / ' + str(die))
        else:
            grog['pointAge'] = crisis(grog['pointAge'])
            grog['history'].append('Crisis! / ' + str(die))
            history.append('Crisis! / ' + str(die))
            grog['ritual'] = 0
        count += 1
    print(history)
    return(grog)

def arsRoll(b=0):
    roll = random.randint(0,9)
    # TODO process botch
    # process explode
    mult = 1
    while roll == 1:
        mult *= 2
        #print('explode! x' + str(mult)) # for testing
        roll = random.randint(1, 10)
    #print('rolled d10: ' + str(roll))  # for testing
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
    



def displayGrog(grog):
    print('Name: ' + grog['name'])
    if grog['ritual'] < 0:      # only print ritual if there is a ritual
        print('Age: %s (%s) [LR %s]' % (grog['age'], grog['appAge'], str(grog['ritual'])))
    else:
        print('Age: %s (%s)' % (grog['age'], grog['appAge']))
    if grog['ageMod'] != 0:
        print('Other aging mods: %s' % str(grog['ageMod']))
    if grog['pointAge'] > 0:    # only print decrepitude if aging poitns exist
        decr = math.floor(((math.sqrt(8*(grog['pointAge']/5)+1)-1)/2)) # decrepitude = ((sqrt(8*(ap/5)+1)-1)/2)
        print('Decrepitude: %s (%s)' % (str(decr), grog['pointAge']) )
    if len(grog['history']) > 0:    # only print history if there is history
        print('Aging History:')
        for x in grog['history']:
            print('* ' + x)
    print('\n')


## open grogs
grogFile = shelve.open('grogs')

#### for testing
sampleGrog = {
    'name' : "Tyro",
    'age' : 40,
    'appAge' : 40,
    'pointAge' : 1,     
    'ageMod' : -1,
    'ritual': -8,
    'history': [] }

displayGrog(sampleGrog)
ageSimple(sampleGrog)

## save and close grogs
grogFile.close()
