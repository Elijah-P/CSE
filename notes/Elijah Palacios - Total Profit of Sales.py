import csv

different_items = {}


with open("Sales Records.csv", "r") as old_csv:
    reader = csv.reader(old_csv)
    print("Processing...")

    for row in reader:
        if row[0] == "Region":
            continue
        old_number = float(row[13])  # String
        # print(old_number)
        # Find out what type of item it is
        item_type = row[2]
        # print(item_type)
        # # Add to different_items
        try:
            different_items[item_type] += old_number
            different_items[item_type] = round(different_items[item_type], 2)
        except KeyError:
            different_items[item_type] = old_number

most_profit = max(different_items.values())


for key, value in different_items.items():
    print(key, end=": ")
    print("${:,}".format(value))


print("%s has made the most profit" % most_profit)
