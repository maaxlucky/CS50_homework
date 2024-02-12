import random

houses_hp = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]


class Hat:
    houses = houses_hp

    @classmethod # using this and cls we can get variables from class
    def sort(cls, name):
        print(name, 'is in', random.choice(cls.houses))


Hat.sort("Harry")
