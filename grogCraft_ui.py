##! python3
# grogCraft2.py - a program to make grogs for aging
# Usage: grogCraft2.py 

import csv, arsAge, sys
from grogs import Grog, csvGrog

# CONSTANTS
MENU = ["list all grogs",
        "view a grog"
        "create a grog",
        "delete a grog",
        "age grogs"]

if len(sys.argv) == 2:
    covenant = sys.argv[1]
else:
    covenant = 'test-grogs'
#    covenant = 'keras-nisi'    # This is my covenant!

# Grog Input: Grog(name, age, appAge, ritual, ageMod, agingPoints)

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

## function: age a grog
def ageGrog(grogList):
    pass
    
## function: print the selection menu
def printMenu():
    print()
    for n, m in enumerate(MENU):
        print(" %s) [%s]%s" % (n + 1, m[0], m[1:]))
    print(" 0) [q]uit")

## function: make selection from the menu
def menuSelect():
    pass

# Load grog files
def loadCovenant():
    grogFile = open(covenant + '.tsv')
    grogReader = csv.reader(grogFile, delimiter='\t')

    grogs = {}
    grogData = list(grogReader)

    for g in grogData:
        grogs[g[0].lower()] = csvGrog(g)
        print('Importing: %s...' % g[0])
    print('Import complete.')
    grogFile.close()
    return grogs

# Begin menu list
def menuSelect():
    pass

# Closing grog files
def saveCovenant():
    grogFile = open(covenant + '_new.tsv','w',newline='')
    grogWriter = csv.writer(grogFile, delimiter='\t')

    for k in grogs.keys():
        print(' - Exporting %s...' % k)
        grogWriter.writerow(grogs[k].grogList())
    print('Export Complete: %s' % 'new ' + covenant)
    grogFile.close()

printMenu()
