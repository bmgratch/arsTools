#! python3
# grogCraft.py - a program to make grogs for aging
#

import shelve, math
import pyinputplus as pyip

## function: Display a single grog
def displayGrog(grog):
    print('Name: ' + grog['name'])
    if grog['ritual'] < 0:      # only print ritual if there is a ritual
        print('Age: %s (%s) [LR %s]' % (grog['age'], grog['appAge'], str(grog['ritual'])))
    else:
        print('Age: %s (%s)' % (grog['age'], grog['appAge']))
    if grog['ageMod'] != 0:
        print('Other aging mods: %s' % str(grog['ageMod']))
    if grog['pointAge'] > 0:    # only print decrepitude if aging points exist
        decr = math.floor(((math.sqrt(8*(grog['pointAge']/5)+1)-1)/2)) # decrepitude = ((sqrt(8*(ap/5)+1)-1)/2)
        print('Decrepitude: %s (%s)' % (str(decr), grog['pointAge']) )
    if len(grog['history']) > 0:    # only print history if there is history
        print('Aging History:')
        for x in grog['history']:
            print('* ' + x)
    print()

## Create a new grog with this function
def createGrog(grogsList):
    grog = {}
    grog['name'] = ''
    while grog['name'] == '':
        grog['name'] = input("Give the grog's name:  ")
        if grog['name'] == '':
            print('Grog name cannot be blank...')
        elif grog['name'] in grogsList.keys():
            print('This grog name already exists.')
            grog['name'] = ''           
    grog['age'] = pyip.inputInt("How old is the grog?  ")
    grog['appAge'] = pyip.inputInt("How old does the grog look?  ")
    grog['pointAge'] = pyip.inputInt('How many decrepitude points acquired?  ')
    grog['ageMod'] = pyip.inputInt('Total up the lifestyle and virtue modifiers for aging:  ')
    grog['ritual'] = pyip.inputInt("And now add the grog's longevity ritual?  ")
    grog['history'] = []
    print('Thanks!\n')
    return(grog)

## function: List all grogs in your list
def listGrogs(grogList):
    if len(grogList) == 0:
        print('No grogs yet!\n')
        return

    for n in grogList.keys():
        print(n)
    print()

## function: select a grog to view from a list
def viewGrogs(grogList):
    if len(grogList) == 0:
        print('No grogs yet!\n')
        return
    print('Select a grog to view:')
    listGrogs(grogList)
    grog = input('Selection:  ').lower()
    if grog in grogList.keys():
        displayGrog(grogList[grog])
    elif grog == '':
        return
    else:
        print('Grog does not exist...')
        return

## function: delete a grog
def delGrog(grogList):
    if len(grogList) == 0:
        print('No grogs yet!\n')
        return
    deleted = input('Which grog do you want to delete?  ').lower()
    if deleted.lower() in grogList.keys():
        print('Deleting %s' % deleted)
        del grogList[deleted]
    if deleted.lower() in grogFile.keys():
        del grogFile[deleted]
    return

# Load grog files
grogFile = shelve.open('grogs')
grogs = {}
for n in grogFile.keys():
    grogs[n.lower()] = grogFile[n]
    print('Importing: ' + n)
print()

# list of functions:
menu = ['view', 'create', 'list', 'delete', 'quit']
while True:
    print(menu)
    menuSelect = input("Select from Menu:  ")   # Menu select begins
    if menuSelect.lower() in menu:
        print(menuSelect)
        print()
        if menuSelect.lower() == 'quit':
            break
        elif menuSelect.lower() == 'view':
            viewGrogs(grogs)
        elif menuSelect.lower() == 'list':
            listGrogs(grogs)
        elif menuSelect.lower() == 'create':
            newGrog = createGrog(grogs)              # grog creation
            grogs[newGrog['name'].lower()] = newGrog
        elif menuSelect.lower() == 'delete':
            delGrog(grogs)
    else:
        print('Select from the menu, please.\n')

# Begin grog input
##yn = pyip.inputYesNo("Enter new grog? (y/N) ")
##if yn == ('yes'):
##    newGrog = createGrog()
##    displayGrog(newGrog)
##    #grogs.append(newGrog)
##    grogs[newGrog['name'].lower()] = newGrog
##yn = pyip.inputYesNo("Delete a grog? (y/N) ")
##if yn == ('yes'):
##    delGrog(grogs)
##
##yn = pyip.inputYesNo("List your grog? (y/N) ")
##if yn == ('yes'):
##    print("Here's all your grogs!")
##    print('')
##    listGrogs(grogs)

# Closing grog files
for n in grogs.keys():
    print('Exporting %s...' % n)
    grogFile[n] = grogs[n]

    
grogFile.close()


