# arsTools
This is a project designed to run aging rolls on a large number of grogs and covenfolk at once.  It only tracks age and decrepitude, rather than stats, though it will print out what stats are affected when aged.

grogs.py has a class, Grog, that tracks name, age, apparent age, longevity ritual, other age modifiers, and aging points.  It can load from and save to a \*.csv file. It tracks aging history, but the aging history doesn't survive saving yet.

arsRoll.py has a method, arsRoll.roll() that rolls a non-botch stress die. (uses random.randint())

arsAge.py has a simple aging method, arsAge.ageSimple() that ages a grog given to it, using arsRoll.

grogCraft2.py is my grog handling software.  It can load from csv *(currently set to test-grogs.csv)* and save *(currently to new-test-grogs.csv)*. In the program, you can create new grogs, view and list your grogs, delete a grog, and age your grogs up (single or all).
