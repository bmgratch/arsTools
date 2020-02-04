# Program to test grogs functionality
# Rolled into grogs 2

import shelve, csv
from grogs import Grog, csvGrog, dictGrog

# grog format = Grog(name, age, appAge, ritual, ageMod, decrepitude, history)

tyro = Grog('tyro', 40, 40, -4, -1, 1)
#tyro.display()
nero = Grog('Nero', 25, 23, 0, 0, 0)
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
grog2 = []
grogCSV = open('test-grogs.csv')
grogReader = csv.reader(grogCSV)
grogData = list(grogReader)
for g in grogData:
    print(g)
    gT = csvGrog(g)
    gT.display()
    grog2.append(csvGrog(g))

