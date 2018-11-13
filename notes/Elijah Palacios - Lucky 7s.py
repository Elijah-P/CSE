import timeit
import random
Money = 15
Rounds = 0
print("DOESN't matter what your response was, lets start!")
# maxMoney_list = list()  # don't use list, find something better.
Maxmoney = 0

timer = timeit.Timer()  # timing how long it takes to find maximum amount of money

while Money > 0:
    # maxMoney_list.append(Money)
    Dice1 = random.randint(1, 6)
    Dice2 = random.randint(1, 6)
    Money -= 1
    total = Dice1 + Dice2
    if total == 7:
        Money += 5
        Rounds += 1
        if Money
    else:
        Money += 0
        Rounds += 1
    print("You have $%d" % Money)
print("You lasted %d rounds" % Rounds)
# Maxmoney = max(maxMoney_list)
print("The maximum amount of money you had was $%d" % Maxmoney)
print(timeit.timeit())