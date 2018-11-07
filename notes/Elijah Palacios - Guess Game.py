import random
a = random.randint(1, 10)
win = False
guesses_left = 5
while guesses_left > 0 and not win:
    answer = int(input("Pick a number between 1 and 10 "))
    if answer == a:
        print("You got the right number")
        print("You Win!")
        win = True
    else:
        guesses_left -= 1
    if answer > a:
        print("The answer is a lower number")
    elif answer < a:
        print("The number is higher")
    if guesses_left == 0:
        print("You lose")


