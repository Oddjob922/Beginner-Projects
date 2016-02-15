# Dice Rolling Simulator
# Python 3.5.1
# Written by alfredmuffin

from random import randint

def roll(num_of_sides):
    return randint(1, num_of_sides)


def go_again():
    choice = input("\nWould you like to go again? (y/n) ")
    if choice == "Y" or choice == "y":
        simulator()
    elif choice == "N" or choice == "n":
        print("\nGoodbye!\n")
        return
    else:
        go_again()


def simulator():
    while True:
        try:
            sides = int(input("\nNumber of sides: "))
            rolls = int(input("Number of rolls: "))
        except ValueError:
            print("That is not a number!\n")
        else:
            break

    print("\n")
    for number in range(1, rolls + 1):
        print("Roll {0}: ".format(number) + str(roll(sides)))

    go_again()


print("\n********* Dice Rolling Simulator *********")
simulator()
