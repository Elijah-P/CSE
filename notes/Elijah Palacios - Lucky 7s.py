import timeit
import random
Money = 15
Rounds = 0
print("DOESN't matter what your response was, lets start!")
Maxmoney = 0
Round_most_money = 0
timer = timeit.Timer()  # timing how long it takes to find maximum amount of money

while Money > 0:
    Dice1 = random.randint(1, 6)
    Dice2 = random.randint(1, 6)
    Money -= 1
    total = Dice1 + Dice2
    if total == 7:
        Money += 5
        Rounds += 1
        if Maxmoney < Money:
            Maxmoney = Money
            Round_most_money = Rounds
    else:
        Money += 0
        Rounds += 1
    print("You have $%d" % Money)
print("You lasted %d rounds" % Rounds)
print("The round you had the most money, which is $%d, was round %d" % (Maxmoney, Round_most_money))
print(timeit.timeit())