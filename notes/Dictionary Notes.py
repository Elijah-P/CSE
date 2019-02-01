states = {
    "CA": "California",
    "VA": "Virgina",
    "MD": "Maryland",
    "RI": "Rhode Island",
    "NV": "Nevada"
}

print(states["CA"])
print(states["NV"])

nested_dictonary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39557045  # 39,540,000
    },
    "VA": {
        "NAME": "Virginia",
        "POPULATION": 8517685  # 8,517,685
    },
    "MD": {
        "NAME": "Maryland",
        "POPULATION": 6042718  # 6,042,718
    },
    "RI": {
        "NAME": "Rhode Island",
        "POPULATION": 1057315  # 1,057,315
    },
    "NV": {
        "NAME": "Nevada",
        "POPULATION": 3034392  # 3,034,392
    }
}

print(nested_dictonary["NV"]["POPULATION"])
print(nested_dictonary["RI"]["NAME"])

complex_dictonary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39557045,  # 39,540,000
        "CITIES": [
            "Fresno",
            "San Fransisco",
            "Los Angeles"
        ]
    },
    "VA": {
        "NAME": "Virginia",
        "POPULATION": 8517685,  # 8,517,685
        "CITIES": [
            "Richmond",
            "Norfolk",
            "Alexandria"
        ]
    },
    "MD": {
        "NAME": "Maryland",
        "POPULATION": 6042718,  # 6,042,718
        "CITIES": [
            "Bethesda",
            "Baltimore",
            "Annapolis"
        ]
    },
    "RI": {
        "NAME": "Rhode Island",
        "POPULATION": 1057315,  # 1,057,315
        "CITIES": [
            "Providence",
            "Newport",
            "Warwick"
        ]
    },
    "NV": {
        "NAME": "Nevada",
        "POPULATION": 3034392,  # 3,034,392
        "CITIES": [
            "Carson City",
            "Las Vegas",
            "Reno"
        ]
    }
}

print(complex_dictonary["RI"]["CITIES"][2])

print(complex_dictonary["VA"]["NAME"])
print(complex_dictonary["MD"]["CITIES"][0])

print(complex_dictonary.keys())
print(nested_dictonary.items())

print()
for key, value in complex_dictonary.items():
    print(key)
    print(value)
    print("-" * 20)

for state, facts in complex_dictonary.items():
    for attr, value in facts.items():
        print(attr)
        print(value)
        print("-" * 20)
    print("=" * 20)


# Other notes

# Adding to a dictionary

states["AL"] = "Alaska?" # It isn't Alaska

# Changing a dictionary Value

states["AL"] = "Alabama" # It's actually Alabama
