# arsAge.py - aging program for Ars Magica grog tracking.
# Planning on using this as a module in grogCraft2.py

import math
from grogs import Grog
from arsRoll import roll

# simple grog aging for non-statted grogs
def ageSimple(grog, years=1):
    count = 0
    history = grog.history
    while count < years:
        grog.age += 1
        grog.appAge += 1
        mod = math.ceil(grog.age / 10.0) + grog.ritual + grog.ageMod
        ageRoll= roll() + mod
        if grog.age < 35:
            if ageRoll <= 2:
                grog.appAge -= 1
                grog.history.append('(%s) %s / %s'% (str(grog.age), ageTable[2], str(ageRoll)))
            else:
                grog.history.append(('(%s) %s'% (str(grog.age), ageTable[3]))
        elif ageRoll <= 2:
            grog.appAge -= 1
            grog.history.append('(%s) %s / %s'% (str(grog.age), ageTable[2], str(ageRoll)))
        elif ageRoll <= 9:
            grog.history.append('(%s) %s / %s'% (str(grog.age), ageTable[3], str(ageRoll)))
        elif ageRoll == 13:
            cap = grog.agingPoints
            grog.agingPoints = crisis(grog.agingPoints)
            cap = grog.agingPoints - cap
            grog.history.append('(%s) %s [%s]/ %s'% (str(grog.age), ageTable[ageRoll], str(cap), str(ageRoll)))
            #grog.ritual = 0 #disabled
        elif ageRoll <= 17:
            grog.history.append('(%s) %s / %s'% (str(grog.age), ageTable[ageRoll], str(ageRoll)))
            grog.agingPoints += 1
        elif ageRoll <= 21:
            grog.history.append('(%s) %s / %s'% (str(grog.age), ageTable[ageRoll], str(ageRoll)))
            grog.agingPoints += 2
        else:
            cap = grog.agingPoints
            grog.agingPoints = crisis(grog.agingPoints)
            cap = grog.agingPoints - cap
            grog.history.append('(%s) %s [%s]/ %s'% (str(grog.age), ageTable[ageRoll], str(cap), str(ageRoll)))
            #grog.ritual = 0 #disabled
        count += 1
    for year in history:
        print(' * %s' % year)
    return grog


# processing a crisis, advancing aging points
def crisis(ap):
    # formula ((sqrt(8*(ap/5)+1)-1)/2)
    if ap < 5:
        return(5)
    elif ap < 15:
        return(15)
    elif ap < 30:
        return(30)
    elif ap < 50:
        return(50)
    elif ap < 75:
        return(75)
    else:
        return(105)

# default age increase?
ageTable = {
    2 : "No Apparent Aging",
    3 : "Age increased",
    10: "1 aging point in any characteristic",
    11: "1 aging point in any characteristic",
    12: "1 aging point in any characteristic",
    13: "CRISIS. Gain aging points to reach next decrepitude:",
    14: "1 aging point in Qik",
    15: "1 aging point in Sta",
    16: "1 aging point in Per",
    17: "1 aging point in Prs",
    18: "1 aging point each in Str and Sta",
    19: "1 aging point each in Dex and Qik",
    20: "1 aging point each in Com and Prs",
    21: "1 aging point each in Int and Per",
    22: "CRISIS. Gain aging points to reach next decrepitude:"
    }
# crisis table?
# simple die + age/10 + decrepitude
crisisTable = {
    8 : "Bedridden for a week.",
    9 : "Bedridden for a month.",
    15: "Minor Illness. Sta 3+ or CrCo 20",
    16: "Serious Illness. Sta 6+ or CrCo 25",
    17: "Major Illness. Sta 9+ or CrCo 30",
    18: "Critical Illness. Sta 12+ or CrCo 35.",
    19: "Terminal Illness. CrCo 40."
    }

# Grog loading and saving should be handled by grogCraft
# tests below here.

#tyro = Grog('Tyro the Tester', 40, 38, 0, -1, 1)
#ageSimple(tyro, 20)
#tyro.display()
