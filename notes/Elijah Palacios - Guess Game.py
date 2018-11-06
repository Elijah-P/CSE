import random
a = random.randint(1, 10)
loop = 0
while loop != 5:
    answer = int(input("Pick a number between 1 and 10 "))
    if answer > a:
        print("The answer is a lower number")
        loop += 1
    elif answer < a:
        print("The number is higher")
        loop += 1
    elif answer == a:
        print("You got the right number")
        print("You Win!")
    elif loop == 5:
        print("You lose")
