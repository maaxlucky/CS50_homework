houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f'{self.name} from {self.house}'

    @classmethod
    def get(cls):
        name = input('Name: ')
        house = input('House: ')
        return cls(name, house) # we return class object with name and house

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property # getter - just get house name
    def house(self):
        return self._house

    # Setter
    @house.setter # setter - if user try to change house and house is not in houses he will get error
    def house(self, house):
        if house not in houses:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = Student.get()
    # student.house = 'Number Four, Privet Drive'
    print(student)


if __name__ == '__main__':
    main()
