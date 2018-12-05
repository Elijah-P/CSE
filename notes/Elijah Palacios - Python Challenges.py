import math
print("CHALLENGE1")
def challenge1(firstname, lastname):
    print(lastname, firstname)
challenge1("Elijah", "Palacios")
print()

print("CHALLENGE2")
def challenge2(given_number):
    if given_number % 2 == 0:
        print("This number is an even number")
    else:
        print("This number is an odd number")
challenge2(int(input("pick a even or odd number, and I'll figure out which one it is.")))
print()

print("CHALLENGE3")
def challenge3(base, height):
    print(base*height / 2)
challenge3(5, 10)
print()

print("CHALLENGE4")
def challenge4(number):
    if number > 0:
        print("This is a positive number")
    elif number < 0:
        print("This is a negative number")
    elif number == 0:
        print("This is zero")
challenge4(2)
print()

print("CHALLENGE5")
def challenge5(radius):
    print(math.pi * radius**2)
challenge5(2)
print()

print("CHALLENGE6")
def challenge6(radius):
    print(4/3 * math.pi * radius**3)
challenge6(6)
print()

print("CHALLENGE7")
def challenge7(number):
    print(number+number*number+number**3)
challenge7(2)
print()

print("CHALLENGE8")
def challenge8(number):
    if number >= 150 and number <= 2000:
        print("This number works")
    else:
        print("This number does not work")
challenge8(160)
print()

print("CHALLENGE9")
def challenge9(letter):
    vowel_list = ("a", "e", "i", "o", "u", "y")
    if letter in vowel_list:
        print("This is a vowel")
    else:
        print("This is not a vowel")
challenge9("t")
print()

print("CHALLENGE10")
def challenge10(string):
    if string == int(string):
        print("This is a number")
    else:
        print("This is not a number")
challenge10(int("7"))
