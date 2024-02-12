groc_list = {}

while True:
    try:
        groc_item = input()
        groc_item = groc_item.upper()
        if groc_item in groc_list:
            groc_list[groc_item] = groc_list[groc_item] + 1 # change value of key if it repeats
        else:
            groc_list.update({groc_item:1}) # if does not repeat we apply default value: 1
    except EOFError:
        break
    except KeyError:
        pass

# sort dictionary with sorted() and items() functions
sorted_groc_list = dict(sorted(groc_list.items()))

for food in sorted_groc_list:
    print(f"{sorted_groc_list[food]} {food}")
