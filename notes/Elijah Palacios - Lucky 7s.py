import random
Money = 15
Rounds = 0
print("DOESN't matter what your response was, lets start!")
maxMoney = list
while Money > 0:
    Dice1 = random.randint(1, 6)
    Dice2 = random.randint(1, 6)
    Money -= 1
    total = Dice1 + Dice2
    if total == 7:
        Money += 5
        Rounds += 1
    else:
        Money += 0
        Rounds += 1
    print("You have $%d" % Money)
print("You lasted %d rounds" % Rounds)
