#! python3
# grogCraft.py - a program to make grogs for aging
#

import csv
from grogs import Grog, csvGrog
import pyinputplus as pyip

covenant = 'test-grogs.csv'

# Grog Input: Grog(name, age, appAge, ritual, ageMod, agingPoints)
## function: Display a single grog
## part of grog class now
##def displayGrog(grog):
##    pass

## Create a new grog with this function
def createGrog(grogsList):
    newGrog = []
    print("Let's input a new grog!")
    name = pyip.inputStr("What is the grog's name?  ")
    newGrog.append(name)
    age = pyip.inputInt("What is %s's true age?  " % name, min=5)
    newGrog.append(age)
    newGrog.append(pyip.inputInt("What is %s's apparent age?  " % name, min=5, max=age))
    newGrog.append(pyip.inputInt("What is this grog's Longevity Ritual?  ", max=0))
    newGrog.append(pyip.inputInt("What is %s's other aging modifiers?  " % name))
    newGrog.append(pyip.inputInt("How many aging points has %s acquired?  " % name, min=0))
    newGrog = csvGrog(newGrog)
    print("This is your Grog:")
    newGrog.display()
    yn = ""
    yn = pyip.inputYesNo("Keep this %s [y/n]" % name)
    if yn == 'yes':
        grogsList[name.lower()] = newGrog
    else:
        print('Scrapping the grog.')

## function: List all grogs in your list
def listGrogs(grogList):
    print("Here's a list of your grogs:")
    for k in grogList.keys():
        print(" * %s" % k)
    

## function: select a grog to view from a list
def viewGrogs(grogList):
    listGrogs(grogList)
    grog = input("Which grog would you like to look at?  ")
    if grog.lower() in grogList.keys():
        grogList[grog].display()
    else:
        print("That grog isn't in your covenant.")
        
## function: delete a grog
def delGrog(grogList):
    print("Delete single grog") # placeholder
    pass

## function: print the selection menu
def printMenu():
    print()
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
        if opt[0] in menu:
            return(opt[0])
        else:
            print('INVALID SELECTION')

# Load grog files
grogFile = open(covenant)
grogReader = csv.reader(grogFile)
grogs = {}
grogData = list(grogReader)
grogFile.close()

for g in grogData:
    grogs[g[0].lower()] = csvGrog(g)
    print('Importing: %s...' % g[0])
print('Import complete.')
grogFile.close()

# Begin menu list
selection = ''
while (selection != '0') and (selection != 'q'):
    selection = menuSelect()
    print(selection)    # should run until quit. Print temp.
    ## TODO actually enact choices.
    ## TODO list all
    if (selection == '1' or selection == 'l'):
        listGrogs(grogs)
    ## Todo view one
    elif (selection == '2' or selection == 'v'):
        viewGrogs(grogs)
    ## todo create
    elif (selection == '3' or selection == 'c'):
        createGrog(grogs)
    ## TODO Modify?
    ## todo delete
    elif (selection == '4' or selection == 'd'):
        delGrog(grogs)

# Closing grog files
grogFile = open('new_' +covenant,'w',newline='')
grogWriter = csv.writer(grogFile)
for k in grogs.keys():
    print(' - Exporting %s...' % k)
    grogWriter.writerow(grogs[k].grogList())
print('Export Complete: %s' % 'new_' + covenant)
grogFile.close()
