#! python3
# grogCraft.py - a program to make grogs for aging
#

import shelve, math
from grogs import Grog
import pyinputplus as pyip

# Grog Input: Grog(name, age, appAge, ritual, ageMod, agingPoints, history)
## function: Display a single grog
## part of grog class now
##def displayGrog(grog):
##    pass

## Create a new grog with this function
def createGrog(grogsList):
    pass

## function: List all grogs in your list
def listGrogs(grogList):
    pass

## function: select a grog to view from a list
def viewGrogs(grogList):
    pass

## function: delete a grog
def delGrog(grogList):
    pass

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


# Closing grog files
for n in grogs.keys():
    print('Exporting %s...' % n)
    grogFile[n] = grogs[n]
grogFile.close()


