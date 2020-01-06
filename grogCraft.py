#! python3
# grogCraft.py - a program to make grogs for aging
#

import shelve, math
import pyinputplus as pyip

## function: Display a single grog
def displayGrog(grog):
    print('Name: ' + grog['name'])
    if grog['ritual'] < 0:      # only print ritual if there is a ritual
        print('Age: %s (%s) [LR %s]' % (grog['age'], grog['age'] + grog['appAge'], str(grog['ritual'])))
    else:
        print('Age: %s (%s)' % (grog['age'], grog['appAge'] + grog['appAge']))
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

## Create a new grog with this function
def createGrog():
    grog = {}
    grog['name'] = input("Give the grog's name:  ")
    grog['age'] = pyip.inputInt("How old is the grog?  ")
    appAge = pyip.inputInt("How old does the grog look?  ")
    grog['appAge'] = appAge - grog['age']
    grog['pointAge'] = pyip.inputInt('How many decrepitude points acquired?  ')
    grog['ageMod'] = pyip.inputInt('Total up the lifestyle and virtue modifiers for aging:  ')
    grog['ritual'] = pyip.inputInt("And now add the grog's longevity ritual?  ")
    grog['history'] = []
    print('Thanks!\n')
    return(grog)

## function: List all grogs in your list
def listGrogs(grogList):
    for n in grogList.keys():
        print(n)
    print()

## function: select a grog to view from a list
def viewGrogs(grogList):
    print('Select a grog to view:')
    listGrogs(grogList)

## function: delete a grog
def delGrog():
    print(' (does nothing yet)')
    pass

# Load grog files
grogFile = shelve.open('grogs')
grogs = {}
for n in grogFile.keys():
    grogs[n] = grogFile[n]
    print('Importing: ' + n)
    displayGrog(grogFile[n])
print()

#list of functions:
menu = ['view', 'create', 'list', 'delete']

# Begin grog input
yn = pyip.inputYesNo("Enter new grog? (y/N) ")
if yn == ('yes'):
    newGrog = createGrog()
    displayGrog(newGrog)
    #grogs.append(newGrog)
    grogs[newGrog['name']] = newGrog
yn = pyip.inputYesNo("Delete a grog? (y/N) ")
if yn == ('yes'):
    delGrog()

yn = pyip.inputYesNo("List your grog? (y/N) ")
if yn == ('yes'):
    print("Here's all your grogs!")
    print('')
    listGrogs(grogs)

# Closing grog files
for n in grogs.keys():
    print('Exporting %s...' % n)
    grogFile[n] = grogs[n]
    
grogFile.close()


