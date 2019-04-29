import csv


def reverse(num: list):
    print(num[::-1])


def multiply_odd_position(num: list):
    for index in range(len(num)):
        if index % 2 == 0:
            num[index] *= 2
            if int(index) > 9:
                index -= 9



with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            old_number = row[0]  # String
            digits = list(old_number)

            if len(digits) == 16:
                last_digit = digits[15]
                digits.remove(last_digit)
                reverse(digits)
                multiply_odd_position(digits)

                writer.writerow(row)
        print("OK")