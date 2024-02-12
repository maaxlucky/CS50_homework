# simple way to cycle through list

# students = ["Hermione", "Harry", "Ron"]

#
# for i in range(len(students)):
#     print(i + 1, students[i])

# dictionary - new data structure!
students = [
            {"name": "Hermione", "house":"Gryffindor", "patronus": "Otter"}, # key : value key : value key : value
            {"name": "Harry", "house": "Gryffindor", "patronus":"Slag"},
            {"name": "Ron", "house": "Gryffindor", "patronus":"Jack Russell terrier"},
            {"name": "Draco", "house": "Slytherian", "patronus":None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ") # we get value by calling key