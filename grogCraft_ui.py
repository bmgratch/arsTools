##! python3
# grogCraft2.py - a program to make grogs for aging
# Usage: grogCraft2.py 

import csv, arsAge, sys, os
from grogs import Grog, csvGrog


# CONSTANTS
MENU = ["list all grogs",
        "view a grog"
        "create a grog",
        "delete a grog",
        "age grogs"]
COV_FOLDER = "covenants"

# Grog Input: Grog(name, age, appAge, ritual, ageMod, agingPoints)

## Create a new grog with this function
def createGrog(grogsList):
    print("Currently not implemented.")
    pass

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
    print(" 0) [q]uit")

## function: make selection from the menu
def menuSelect():
    pass

# Get covenants
def listCovenants():
    return [cov[:-4] for cov in os.listdir(COV_FOLDER) if cov.endswith('.tsv')]

def selectCovenant():
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
        cov = input()
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
    #act on selection
# End
    saveCovenant()
    terminate()
