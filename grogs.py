# grogs.py
# module designed to model grogs for aging.
import math

class Grog:

    def __init__(self, name, age, appAge, ritual, ageMod, agingPoints, history):
        self.name = name
        self.age = age
        self.appAge = appAge
        self.ritual = ritual
        self.ageMod = ageMod
        self.agingPoints = agingPoints
        self.history = history

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
        if len(self.history) > 0:    # only print history if there is history
            print(' Aging History:')
            for x in self.history:
                print(' * ' + x)
        print('')

## Sample grog display for working.

##Name: tyro
## Age: 40 (40) [LR -4]
## Other aging mods: -1
## Decrepitude: 0 (1)
## Aging History:
## * 40: no apparent aging

tyro = Grog('tyro', 40, 40, -4, -1, 1, ['40: no apparent aging'])
tyro.display()
