#! python3
## massAge.py - This python module is designed to mass-age a number of grogs
## using natural rolling. It ingests a file, and asks you the final age
## of each grog in the tsv.

import csv, arsAge
from grogs import Grog, csvGrog

covenant = 'test-grogs'
#covenant = 'keras-nisi'    # My covenant!

# Load grog files
grogFile = open(covenant + '.tsv')
grogReader = csv.reader(grogFile, delimiter='\t')
grogs = {}
grogData = list(grogReader)
grogFile.close()

for g in grogData:
    grogs[g[0].lower()] = csvGrog(g)
    print('Importing: %s...' % g[0])
print('Import complete.')
grogFile.close()

# aging all grogs to current covenant total
for k in grogs.keys():
    print("How old is %s?" % grogs[k].name)
    finalAge = int(input())
    arsAge.ageSimple(grogs[k], finalAge - grogs[k].age)

for k in grogs.keys():
    grogs[k].display()

# Closing grog files
grogFile = open('new_' +covenant + '.tsv','w',newline='')
grogWriter = csv.writer(grogFile, delimiter='\t')
for k in grogs.keys():
    print(' - Exporting %s...' % k)
    grogWriter.writerow(grogs[k].grogList())
print('Export Complete: %s' % 'new_' + covenant + '.tsv')
grogFile.close()
