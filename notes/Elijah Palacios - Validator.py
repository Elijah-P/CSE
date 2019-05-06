import csv


def reverse(num: list):
    digits = (num[::-1])
    return digits


def multiply_odd_position(num: list):
    for index in range(len(num)):
        num[index] = int(num[index]
                         )
        if index % 2 == 0:
            num[index] *= 2
    return num


def num_greater_9(num: list):
    for index in range(len(num)):
        num[index] = int(num[index])
        if num[index] > 9:
            num[index] -= 9
    return num


def add_all_num(my_num: list):
    together = 0
    for index in my_num:
        together += int(index)
    return together


def validate(digits: list):
    if len(digits) == 16:
        last_digit = digits[15]
        digits.pop(15)
        reversed_digits = reverse(digits)
        multiplied = multiply_odd_position(reversed_digits)
        greater_than_9 = num_greater_9(multiplied)
        added = add_all_num(greater_than_9)
        return added % 10 == int(last_digit)
    return False


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            old_number = row[0]  # String
            digits = list(old_number)

            if validate(digits):
                writer.writerow(row)
        print("OK")



