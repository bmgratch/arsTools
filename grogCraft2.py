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

## function: print the selection menu
def printMenu():
    print(" 1) [l]ist all grogs")
    print(" 2) [v]iew a grog")
    print(" 3) [c]reate a grog")
    print(" 4) [d]elete a grog")
    print(" 0) [q]uit")
    return

## function: make selection from the menu
def menuSelect():
    menu = '01234cdlqv' # string of available options from the menu
    while True:
        printMenu()
        opt = input("Select from menu:  ").lower()
        if opt in menu:
            return(opt[0])
        else:
            print('INVALID SELECTION')

# Load grog files
grogFile = shelve.open('grogs')
grogs = {}
for n in grogFile.keys():
    grogs[n.lower()] = grogFile[n]
    print('Importing: ' + n)
print()

# Begin menu list
selection = ''
while (selection != '0') and (selection != 'q'):
    selection = menuSelect()
    print(selection)    # should run until quit. Print temp.
    ## TODO actually enact choices.
    ## TODO list all
    ## Todo view one
    ## todo create
    ## todo delete

# Closing grog files
for n in grogs.keys():
    print('Exporting %s...' % n)
    grogFile[n] = grogs[n]
grogFile.close()


