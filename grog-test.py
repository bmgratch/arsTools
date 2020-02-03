# Program to test grogs functionality

import shelve, csv
from grogs import Grog, csvGrog, dictGrog

# grog format = Grog(name, age, appAge, ritual, ageMod, decrepitude, history)

tyro = Grog('tyro', 40, 40, -4, -1, 1, ['40: no apparent aging'])
#tyro.display()
nero = Grog('Nero', 25, 23, 0, 0, 0, [])
#nero.display()


grogFile = shelve.open('grogs')
grogs = {}
for grog in grogFile.keys():
    grogs[grog.lower()] = grogFile[grog]
    print('Importing:  ' + grog)
    print(grogs[grog])
#    g = dictGrog(grogs[grog])

for grog in grogs.keys():
    print('exporting %s...' % grog)
    grogFile[grog] = grogs[grog]
grogFile.close()

# CSV test
##grogCSV = open('test-grogs.csv')
##grogReader = csv.reader(grogCSV)
##grogData = list(grogReader)
##print(grogData)
##gT = csvGrog(grogData[0])
##gT.display()
