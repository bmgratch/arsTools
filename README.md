# arsTools
This is a project designed to run aging rolls on a large number of grogs and covenfolk at once.  It only tracks age and decrepitude, rather than stats, though it will print out what stats are affected when aged.

grogCraft.py is my covenant and grog handling script. It loads from tsv files stored in the covenants folder. In the program, you can create new grogs, view and list your grogs, delete a grog, and age a grog (single or all) by a year.

grogCraft2.py is my old grog handling software.  It can load from tsv *(currently set to test-grogs.tsv)* and save *(currently to test-grogs_new.tsv)*. In the program, you can create new grogs, view and list your grogs, delete a grog, and age your grogs up (single or all).

grogs.py has a class, Grog, that tracks name, age, apparent age, longevity ritual, other age modifiers, and aging points.  It can import and export to a list, for *.tsv or *.csv use. It tracks aging history, but the aging history doesn't survive saving yet.

arsRoll.py has a method, arsRoll.roll() that rolls a non-botch stress die. (uses random.randint())

arsAge.py has a simple aging method, arsAge.ageSimple() that ages a grog given to it, using arsRoll.

massAge.py is a python script which imports a covenant.tsv and asks you a final age to advance each individual member to. It is slightly outdated; you need to move the desired covenant.tsv from 'covenants' to share the same folder as massAge.py
