import csv

different_items = {
    "Fruits": {
        "Total Profit":0,
    },
    "Clothes": {
        "Total Profit":0,
    },
    "Meat": {
        "Total Profit":0,
    },
    "Beverages": {
        "Total Profit":0,
    },
    "Office Supplies": {
        "Total Profit":0,
    },
    "Cosmetics": {
        "Total Profit":0,
    },
    "Snacks": {
        "Total Profit":0,
    },
    "Personal": {
        "Total Profit":0,
    },
    "House Hold": {
        "Total Profit":0,
    },
    "Vegetables": {
        "Total Profit":0,
    },
    "Baby Food": {
        "Total Profit":0,
    },
    "Cereal": {
        "Total Profit":0
    }
}


with open("Sales Records.csv", "r") as old_csv:
    reader = csv.reader(old_csv)
    print("Processing...")

    for row in reader:
        old_number = row[13]  # String

        # Find out what type of item it is
        item_type = row[2]
        # Add to different_items
        different_items[item_type] += old_number
        print(old_number)
