# arsTools
This is a project designed to run aging rolls on a large number of grogs and covenfolk at once.  It only tracks age and decrepitude, rather than stats, though it will print out what stats are affected when aged.

grogCraft.bat is a Windows script that launches the grogCraft2.py script. It can take an argument to change the name of the covenant (and save-file) it launches. It needs the .tsv file to exist to function.

grogCraft2.py is my grog handling software.  It can load from tsv *(currently set to test-grogs.tsv)* and save *(currently to test-grogs_new.tsv)*. In the program, you can create new grogs, view and list your grogs, delete a grog, and age your grogs up (single or all).

grogs.py has a class, Grog, that tracks name, age, apparent age, longevity ritual, other age modifiers, and aging points.  It can import and export to a list, for *.tsv or *.csv use. It tracks aging history, but the aging history doesn't survive saving yet.

arsRoll.py has a method, arsRoll.roll() that rolls a non-botch stress die. (uses random.randint())

arsAge.py has a simple aging method, arsAge.ageSimple() that ages a grog given to it, using arsRoll.

massAge.py is a python script which imports a covenant.csv and asks you a final age to advance each individual member to.
