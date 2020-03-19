# grogs.py
# module designed to model grogs for aging.
import math

class Grog:
    def __init__(self, name, age, appAge, ritual, ageMod, agingPoints, ageSpeed):
        self.name = name
        self.age = age
        self.appAge = appAge
        self.ritual = ritual
        self.ageMod = ageMod
        self.agingPoints = agingPoints
        self.ageSpeed = ageSpeed
        self.history = []

    def display(self):
        print('Name: ' + self.name)
        if self.ritual < 0:      # only print ritual if there is a ritual
            print(' Age: %s (%s) [LR %s]' % (self.age, self.appAge, str(self.ritual)))
        else:
            print(' Age: %s (%s)' % (self.age, self.appAge))
        if self.ageMod != 0:
            print(' Other aging mods: %s' % str(self.ageMod))
        if self.agingPoints > 0:    # only print decrepitude if aging poitns exist
            decrepitude = math.floor(((math.sqrt(8*(self.agingPoints/5)+1)-1)/2))
            print(' Decrepitude: %s (%s)' % (str(decrepitude), self.agingPoints) )
        if self.ageSpeed != 1:
            print(' Aging Speed: %s' % self.ageSpeed)
        if len(self.history) > 0:    # only print history if there is history
            print(' Aging History:')
            for x in self.history:
                print(' * ' + x)
        print('')
        
    def grogList(self):
        return [self.name, self.age, self.appAge, self.ritual, self.ageMod, self.agingPoints, self.ageSpeed]

def dictGrog(gDict):
    newGrog = Grog(gDict['name'],
                   gDict['age'],
                   gDict['appAge'],
                   gDict['ritual'],
                   gDict['ageMod'],
                   gDict['agingPoints'],
                   gDict['ageSpeed'])
    return newGrog

def csvGrog(gList):
    newGrog = Grog(gList[0],
                int(gList[1]),
                int(gList[2]),
                int(gList[3]),
                int(gList[4]),
                int(gList[5]),
                int(gList[6]))
    return newGrog
