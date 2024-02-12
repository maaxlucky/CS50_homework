name = input("What's your name? ")

match name: # it works like "Switch"
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherian")
    case _:
        print("Who?")