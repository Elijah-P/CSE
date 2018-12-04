def challenge1(firstname, lastname):
    print(lastname, firstname)
challenge1("Elijah", "Palacios")
print()


def challenge2(given_number):
    if given_number % 2 == 0:
        print("This number is an even number")
    else:
        print("This number is an odd number")
challenge2(int(input("pick a even or odd number, and I'll figure out which one it is.")))
print()


def challenge3(base, height):
    print(base*height / 2)
challenge3(5, 10)
print()


def challenge4(number):
    if number > 0:
        print("This is a positive number")
    elif number < 0:
        print("This is a negative number")
    elif number == 0:
        print("This is zero")


def challenge5(radius):
    print(3.14 * radius**2)
challenge5(2)
print()


def challenge7(number):
    print(number+number*number+number**3)
challenge7(2)
print()


def challenge8(number):
    if number >= 150 and number <= 2000:
        print("This number is valid and works")
    else:
        print("This number does not work")
challenge8(150)