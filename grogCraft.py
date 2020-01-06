#! python3
# grogCraft.py - a program to make grogs for aging
#

import shelve

grogFile = shelve.open('grogs')
grogs = []
for n in grogFile.keys():
    print(n)

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
    
print(list(grogFile.keys()))
print("Enter new grog?")

