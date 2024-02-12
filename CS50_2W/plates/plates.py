import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate_vanity): # CS05 vanity plate checker - vp checker

    numeric_part = ''

    for character in plate_vanity:
        if character.isalpha() == False: # if character is not in alphabet
            numeric_part = numeric_part + character # split alpha and numeric part in vp
            if numeric_part[0] == "0": # first number can't start with 0
                return False

    for i in range(len(plate_vanity)):
        if i > 0 and plate_vanity[i].isalpha() == True and plate_vanity[i-1].isalpha() == False: # Check if alpha is inside numeric part
            return False

    if any(char in string.punctuation for char in plate_vanity): # check if any punctuation in vp
        return False

    if len(plate_vanity) > 6 or len(plate_vanity) < 2 or plate_vanity[0].isalpha() == False or plate_vanity[1].isalpha() == False: # can't be less than 2 and more than 6
        return False
    else:
        return True

main()
