import csv

different_items = ["Fruits", "Clothes", "Meat", "Beverages", "Office Supplies", "Cosmetics", "Snacks", "Personal Care",
                   "House Hold", "Vegetables", "Baby Food", "Cereal"]

for item in different_items:
    

def add_total_profit




with open("Sales Records.csv", "r") as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            old_number = row[13]  # String
            digits = list(old_number)

