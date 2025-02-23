## My own Code to Test
## David Long

import random
print("The Dice Game")
print("Enter 0 to stop")
tally = 0
GrandTotal = 0
DiceRolls = [0,0,0,0,0,0]
while(True):
    
    power = int(input("Press 1 to roll the dice:"))
    if(power == 0):
        print("\n\nNice rolls!! Here are your stats:")
        print("Amount of rolls: ", tally)
        print("All dice added up: ", GrandTotal)
        print("All dice rolls: ", DiceRolls)
        break
    D0 = random.randint(1,6)
    D1 = random.randint(1,6)
    D2 = random.randint(1,6)
    D3 = random.randint(1,6)
    D4 = random.randint(1,6)
    D5 = random.randint(1,6)
    Dice = [D0, D1, D2, D3, D4, D5]

    
    print("You rolled:", Dice)
    total = D0+D1+D2+D3+D4+D5
    print("Which add to:", total)
    print("\n \n")
    if tally == 0:
        DiceRolls = Dice
        GrandTotal = total
        tally = 1
    else:
        DiceRolls.append(D0)
        DiceRolls.append(D1)
        DiceRolls.append(D2)
        DiceRolls.append(D3)
        DiceRolls.append(D4)
        DiceRolls.append(D5)
        GrandTotal = sum(DiceRolls)
        tally = tally + 1

    if(total == 36):
        print("High Score!!!")
    elif(total == 6):
        print("Wow thats rough buddy")





##TEST LAB 5
