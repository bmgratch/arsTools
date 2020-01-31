# Grog menu
## Has been folded into grogCraft2.py

def printMenu():
    print(" 1) [l]ist all grogs")
    print(" 2) [v]iew a grog")
    print(" 3) [c]reate a grog")
    print(" 4) [d]elete a grog")
    print(" 0) [q]uit")
    return

def menuSelect():
    menu = '01234cdlqv'
    while True:
        printMenu()
        opt = input("Select from menu:  ").lower()
        if opt in menu:
            return(opt[0])
        else:
            print('INVALID SELECTION')

selection = menuSelect()
print(selection)
