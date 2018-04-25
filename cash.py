from cs50 import get_float
changeOwed = 0
dimes = 0
quarters = 0
nickels = 0
pennies = 0
coinCounter = 0

while changeOwed <= 0:
    changeOwed=get_float("How much change? ")
    if changeOwed > 0:
        break

changeOwed = changeOwed*100

if changeOwed >= 25:
    quarters = changeOwed // 25
    coinCounter += quarters
    changeOwed = changeOwed % 25

if changeOwed >= 10:
    dimes = changeOwed // 10
    coinCounter += dimes
    changeOwed = changeOwed % 10

if changeOwed >= 5:
    nickels = changeOwed // 5
    coinCounter += nickels
    changeOwed = changeOwed % 5

if changeOwed >= 1:
    pennies = changeOwed // 1
    coinCounter += pennies
    changeOwed = changeOwed % 1

#print(f"{coinCounter")
print(f"{coinCounter} Coins used ");
print(f"quarters: {quarters}, dimes: {dimes}, nickels: {nickels}, pennies: {pennies}")