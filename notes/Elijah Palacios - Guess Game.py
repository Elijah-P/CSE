import random
a = random.randint(1, 10)
loop = 0
#  for i in (1, 2, 3, 4, 5):
answer = int(input("Pick a number between 1 and 10 "))
if answer > a:
    print("The answer is a lower number")
if answer < a:
    print("The number is higher")
    if answer == a:
        print("You got the right number")
    if i == 5:
        print("You lose")

        print("You win!")
