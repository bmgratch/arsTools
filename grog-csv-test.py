# Test csv import and export
import csv
from grogs import Grog, csvGrog

grogCSV = 'test-grogs.csv'

# import grogs
grogFile = open(grogCSV)
grogReader = csv.reader(grogFile)
grogs = {}
grogData = list(grogReader)
grogFile.close()

for g in grogData:
    print(' + Importing %s...' % g[0])
    grogs[g[0].lower()] = csvGrog(g)
print('Import complete.\n')

# add a grog
grogs['testy'] = Grog('Testy', 25, 25, 0, 0, 0)

# display grogs
print('Listing Grogs\n')
for k in grogs.keys():
    print(grogs[k].grogList())
    grogs[k].display()


# save changes
grogFile = open('new_'+grogCSV,'w',newline='')
grogWriter = csv.writer(grogFile)
for k in grogs.keys():
    print(' - Exporting %s...' % k)
    grogWriter.writerow(grogs[k].grogList())
print('Export Complete: %s' % 'new_'+grogCSV)
grogFile.close()
