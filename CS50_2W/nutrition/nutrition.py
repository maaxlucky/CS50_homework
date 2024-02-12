fruits = [
        {"name": "apple", "calories": 130}, # key : value
        {"name": "banana", "calories": 50},
        {"name": "kiwifruit", "calories": 90},
        {"name": "pear", "calories": 100},
        {"name": "sweet cherries", "calories": 100},
        {"name": "avocado", "calories": 50},
]

item = input("Item: ")
item = item.lower()

for fruit in fruits:
    if item == fruit["name"]: # get name of fruit by key
        print(fruit["calories"])
