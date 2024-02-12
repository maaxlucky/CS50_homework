menu = {
        "Baja Taco": 4.25, # key: value
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
total = 0

while True:
    try:
        item = input("Item: ")
        item = item.title() # uppercase letter
        total = total + menu[item] # total summ
        print(f"Total: ${total:.2f}") # 2 digits of float number
    except KeyError: # if key : value and key does not exist in dict
        pass
    except EOFError: # exception if user press Control+D
        break
