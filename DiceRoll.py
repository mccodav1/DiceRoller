# This program will simulate dice rolls
# Functionality:
#   Input aDx, where:
#       A is the number of dice to be rolled (usually omitted if 1).
#       X is the number of faces of each die.
import random


def welcome():
    print("Welcome to McConnell's dice roller!\nUsing this application, you can simulate rolling any number of dice "
          "with as many sides as you choose.")
    input("Press ENTER to continue.")


def get_dice():
    more = 'Y'
    diceList = []
    while more.upper() == 'Y':
        dice = input("Enter dice to be rolled in format 'AdX'. A represents number of dice to roll; X indicates "
                     "dice sides.")
        dice = dice.split('d')
        diceList.append(dice)
        more = input("Would you like to enter additional dice to roll? Press Y for yes or N for no.")
    index = 0
    while index < len(diceList):
        diceList[index][0] = int(diceList[index][0])
        diceList[index][1] = int(diceList[index][1])
        index += 1
    return diceList


def roll_dice(dicelist):
    allRolls = []
    for item in dicelist:
        rollsFromOneType = []
        numberOfRolls = item[0]
        numberOfFaces = item[1]
        for num in range(0, numberOfRolls):
            rollsFromOneType.append(random.randrange(1, numberOfFaces+1))
        rollsFromOneType.sort()
        allRolls.append(rollsFromOneType)
    return allRolls


def get_sum(rolls):
    sum = 0
    for item in rolls:
        for roll in item:
            sum += roll
    return sum


welcome()
diceList = get_dice()
rolls = roll_dice(diceList)
rollSum = get_sum(rolls)
index = 0
while index < len(diceList):
    print("d", diceList[index][1], " rolls:", sep="")
    print(rolls[index])
    index += 1
print("Roll sum:", rollSum)
input("Press ENTER to exit")
