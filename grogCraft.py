##! python3
# grogCraft2.py - a program to make grogs for aging
# Usage: grogCraft2.py 

import csv, arsAge, sys, os
from grogs import Grog, csvGrog



# CONSTANTS
MENU = ["list all grogs",
        "view a grog",
        "create a grog",
        "delete a grog",
        "age grogs"]
MENU_CHOICES = [str(opt) for opt in range(0, len(MENU) + 1)] + [opt[0] for opt in MENU] + ['q']
COV_FOLDER = "covenants"

# Grog Input: Grog(name, age, appAge, ritual, ageMod, agingPoints)

## Grog Menu Action function
def menuAction(selection, grogList):
    if selection == '1' or selection == 'l':
        print('\t* Listing all grogs *')
        listGrogs(grogList)
    if selection == '2' or selection == 'v':
        print('\t* Viewing a single grog *')
        viewGrogs(grogList)
    if selection == '3' or selection == 'c':
        print('\t* Creating a new grog *')
        createGrog(grogList)
    if selection == '4' or selection == 'd':
        print('\t* Deleting an unneeded grog *')
        delGrog(grogList)
    if selection == '5' or selection == 'a':
        print('\t* Aging grogs *')
        ageGrog(grogList)
    if selection == '0' or selection == 'q':
        print('Quitting...')
        terminate()

    
## Create a new grog with this function
def createGrog(grogsList):
    newGrog = []
    print("Let's input a new grog!")
    name = ''
    while not name:
        name = input("What is the grog's name?  ")
    newGrog.append(name)
    age = 0
    while age < 5:
        age = getNumber("What is %s's true age? (5 years or older) " % name)
    newGrog.append(age)
    appAge, lr, agingPoints = age + 1, 1, -1
    while appAge > age or appAge < 5:
        appAge = getNumber("What is %s's apparent age? (between 5 and %s) " % (name, age))
    newGrog.append(appAge)
    while lr > 0:
        lr = getNumber("What is this grog's Longevity Ritual bonus? (remember, it should be 0 or less!) ")
    newGrog.append(lr)
    newGrog.append(getNumber("What is %s's other aging modifiers?  " % name))
    while agingPoints < 0:
        agingPoints = getNumber("How many aging points has %s acquired?  (This can't be below 0) " % name)
    newGrog.append(agingPoints)
    newGrog.append(1)
    newGrog = csvGrog(newGrog)
    print("This is your Grog:")
    newGrog.display()
    yn = ""
    while not yn.lower().startswith('y') and not yn.lower().startswith('n'):
        yn = input("Keep this %s [y/n]" % name)
    if yn.lower().startswith('y'):
        grogsList[name.lower()] = newGrog
    else:
        print('Scrapping the grog.')

def getNumber(message):
    while True:
        try:
            num = int(input(message))
        except ValueError:
            print('Please input an integer.')
            continue
        else:
            return num
            break

## function: List all grogs in your list
def listGrogs(grogList):
    print("Here's a list of your grogs:")
    for k in grogList.keys():
        print(" * %s" % k)
        
## function: select a grog to view from a list
def viewGrogs(grogList):
    listGrogs(grogList)
    grog = input("Which grog would you like to look at?  ").lower()
    if grog in grogList.keys():
        grogList[grog].display()
    else:
        print("That grog isn't in your covenant.")
        
## function: delete a grog
def delGrog(grogList):
    listGrogs(grogList)
    grog = input("Which grog would you like to delete?").lower()
    if grog in grogList.keys():
        del grogList[grog]
    else:
        print("That grog isn't in your covenant...")
## function: age a grog
def ageGrog(grogList):
    grog = input("Which grog would you like to age? ('all' for all)  ").lower()
    if grog.lower() == 'all':
        for k in grogList.keys():
            print("Aging %s..." % grogList[k].name)
            arsAge.ageSimple(grogList[k])
    elif grog in grogList.keys():
        arsAge.ageSimple(grogList[grog])
    else:
        print("That grog isn't in your covenant...")
    
## function: print the selection menu
def printMenu():
    print()
    for n, m in enumerate(MENU):
        print(" %s) [%s]%s" % (n + 1, m[0], m[1:]))
    print(" 0) [q]uit (This will quit the program entirely)")

## function: make selection from the menu
def menuSelect():
    while True:
        opt = input("Select from menu:  ").lower()
        if opt and opt[0] in MENU_CHOICES:
            return opt[0]
        else:
            print('Invalid selection.')

# Get covenants
def listCovenants():
    return [cov[:-4] for cov in os.listdir(COV_FOLDER) if cov.endswith('.tsv')]

def selectCovenant():
    print("Select active covenant from the files below:")
    covList = listCovenants()
    sel = ''
    for n, c in enumerate(covList):
        print(" %s) %s" % (n + 1, c))
    print(" %s) NEW COVENANT" % (len(covList) + 1))
    print(" 0) cancel")
    while not sel.isnumeric():
        print('Make selection:   ', end='')
        sel = input()
        if sel.isnumeric():
            if int(sel) not in range(0, len(covList) + 2):
                sel = ''
    if sel == '0':
        return None
    elif int(sel) == len(covList) + 1:
        print('Creating new covenant... select name: (enter nothing to cancel)')
        cov = input().strip()
        if len(cov) > 0:
            return cov
        else:
            return None
    return covList[int(sel) - 1]

# Load grog files
def loadCovenant(covenant):
    grogFile = open(os.path.join(COV_FOLDER, covenant + '.tsv'))
    grogReader = csv.reader(grogFile, delimiter='\t')

    cov_grogs = {}
    grogData = list(grogReader)

    for g in grogData:
        cov_grogs[g[0].lower()] = csvGrog(g)
        print('Importing: %s...' % g[0])
    print('Import complete.')
    grogFile.close()
    return cov_grogs

# Closing grog files
def saveCovenant():
    grogFile = open(os.path.join(COV_FOLDER, covenant) + '_new.tsv','w',newline='')
    grogWriter = csv.writer(grogFile, delimiter='\t')

    for k in grogs.keys():
        print(' - Exporting %s...' % k)
        grogWriter.writerow(grogs[k].grogList())
    print('Export Complete: %s' % 'new ' + covenant)
    grogFile.close()

def terminate():
    yn = ''
    print('Would you like to save the covenant?')
    while not yn.lower().startswith('y') and not yn.lower().startswith('n'):
        yn = input('(yes or no?)')
    if yn.lower().startswith('y'):
        saveCovenant()
    print('Goodbye!')
    sys.exit()

# Load the covenant or get a new one
covenant = selectCovenant()
if covenant in listCovenants():
    grogs = loadCovenant(covenant)
elif not covenant:
    terminate()
else:
    grogs = {}
    print('Creating blank covenant: ' + covenant)

# Begin covenant-grog loop
menuAct = ''
while True:
    #print menu
    printMenu()
    #get selection
    menuAct = menuSelect()
    #act on selection
    menuAction(menuAct, grogs)

