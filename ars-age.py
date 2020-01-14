#! python3
# ars-age.py - a program to calculate aging rolls for grogs and covenfolk
#

import random, math, shelve
import pyinputplus as pyip

def ageSimple(grog, years=1):       # grog is a grog dict, years are number of years to age
    count = 0                       # Counter to track number of times done
    mod = grog['ritual'] + grog['ageMod']
    history = []
    while count < years:
        grog['age'] += 1            # first age up
        grog['appAge'] += 1
        mod = math.ceil(grog['age'] // 10 + mod) # generate age-based penalty

        die = arsRoll() + mod           # roll a die, add mod
        if grog['age'] < 35:
            if die <= 2:
                grog['appAge'] -= 1
                grog['history'].append('No apparent aging (%s)/ %s' % (str(grog['age']), str(die)))
                history.append('No apparent aging (%s)/ %s' % (str(grog['age']), str(die)))
        if die <= 2:
            grog['appAge'] -= 1
            grog['history'].append('No apparent aging (%s)/ %s' % (str(grog['age']), str(die)))
            history.append('No apparent aging (%s)/ %s' % (str(grog['age']), str(die)))
        elif die <= 9:
            grog['history'].append('Aged (%s)/ %s' % (str(grog['age']), str(die)))
            history.append('Aged (%s)/ %s' % (str(grog['age']), str(die)))
        elif die == 13:
            grog['pointAge'] = crisis(grog['pointAge'])
            grog['history'].append('Crisis! (%s)/ %s' % (str(grog['age']), str(die)))
            history.append('Crisis (%s)/ %s' % (str(grog['age']), str(die)))
            grog['ritual'] = 0
        elif die <= 17:
            grog['pointAge'] += 1
            grog['history'].append('Aged in stat! (%s)/ %s' % (str(grog['age']), str(die)))
            history.append('Aged in stat! (%s)/ %s' % (str(grog['age']), str(die)))
        elif die <= 21:
            grog['pointAge'] += 2
            grog['history'].append('Aged in two stats (%s)/ %s' % (str(grog['age']), str(die)))
            history.append('Aged in two stats (%s)/ %s' % (str(grog['age']), str(die)))
        else:
            grog['pointAge'] = crisis(grog['pointAge'])
            grog['history'].append('Crisis! (%s)/ %s' % (str(grog['age']), str(die)))
            history.append('Crisis! (%s)/ %s' % (str(grog['age']), str(die)))
            grog['ritual'] = 0
        count += 1
    for x in history:
        print(' * %s' % x)
    print('')
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

## menu display function    
def displayMenu():
    print('- 1 - [D]isplay loaded grogs')
    print('- 2 - [S]ingle grog aging')
    print('- 3 - [A]ll grogs aging')
    print('- 4 - [Q]uit')
    print()
    
## Grog list function
def listGrogs(grogs):
    print("PRINTING GROGS....")
    for g in grogs.keys():
        print(g)

def ageGrog(grog):
    print('Aging %s... how many years?' % grog['name'])
    yr = pyip.inputInt()
    if yr > 0:
        ageSimple(grog, yr)
    elif yr <= 0:
        print('Can only age positive, cancelled.')



## Grog display function
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
    print('')


## Load grog files
grogFile = shelve.open('grogs')
grogs = {}
for n in grogFile.keys():
    grogs[n.lower()] = grogFile[n]
    print('Importing: ' + n)
print()

#### for testing
sampleGrog = {
    'name' : "Tyro",
    'age' : 40,
    'appAge' : 40,
    'pointAge' : 1,     
    'ageMod' : -1,
    'ritual': -8,
    'history': [] }
grogs['tyro'] = sampleGrog

validMenu = ['a','s', 'd', 'q', '1', '2', '3', '4'] # for menu selection
select = 'x'
while select != ('q' or '4'):
    while select not in validMenu:
        displayMenu()
        print('Select from menu: ')
        select = input().lower()
    if select == '1' or select == 'd':          # list grogs
        print(' NEED display logic')
        listGrogs(grogs)
        select = 'x'
    elif select == '2' or select == 's':        # age a grog
        print('Which grog to age?')
        selGrog = input().lower()
        if selGrog in grogs.keys():
            print('Aging %s' % selGrog)
            ageGrog(grogs[selGrog])
        else:
            print('Grog not in list')
        select = 'x'
    elif select == '3' or select == 'a':        # age all grogs
        print('This will age every loaded grog.')
        print('Once you\'re sure, type in the number. (Put a 0 to not age)')
        yrAll = pyip.inputInt("How many years to age?  ")
        if yrAll < 1:
            print('Cancelling aging.')
        else:
            for g in grogs:
                print(' Aging %s, %s years...' % (g, yrAll))
                ageSimple(grogs[g], yrAll)
        select = 'x'
    elif select == '4' or select == 'q':
        print('Quitting now!')       # quitting
        break
    else:
        continue
print('Debug: Printing loaded grogs')
for g in grogs.keys():
    displayGrog(grogs[g])
    ## TODO: Test aging for multiple grogs.

## save and close grogs
print('Saving disabled during testing.')
##for g in grogs.keys():
##    print('Exporting %s...' % g)
##    grogFile[g] = grogs[g]
print()      
grogFile.close()
