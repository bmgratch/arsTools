# arsAge.py - aging program for Ars Magica grog tracking.
# Planning on using this as a module in grogCraft2.py

from grogs import Grog
from arsRoll import roll

# simple grog aging for non-statted grogs
def ageSimple(grog, years=1):
    pass

# processing a crisis, advancing aging points
def crisis(ap):
    pass

# default age increase?
ageTable = {
    2 : "No Apparent Aging"
    10: "1 aging point in any characteristic"
    13: "CRISIS. Gain aging points to reach next decrepitude."
    14: "1 aging point in Qik"
    15: "1 aging point in Sta"
    16: "1 aging point in Per"
    17: "1 aging point in Prs"
    18: "1 aging point each in Str and Sta"
    19: "1 aging point each in Dex and Qik"
    20: "1 aging point each in Com and Prs"
    21: "1 aging point each in Int and Per"
    22: "CRISIS. Gain aging points to reach next decrepitude."
    }
# crisis table?
# simple die + age/10 + decrepitude
crisisTable = {
    8 : "Bedridden for a week."
    9 : "Bedridden for a month."
    15: "Minor Illness. Sta 3+ or CrCo 20"
    16: "Serious Illness. Sta 6+ or CrCo 25
    17: "Major Illness. Sta 9+ or CrCo 30"
    18: "Critical Illness. Sta 12+ or CrCo 35."
    19: "Terminal Illness. CrCo 40."
    }

# Grog loading and saving should be handled by grogCraft
# tests below here.
