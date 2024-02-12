
def main():
    print_square(3)
    print_column(3)
    print_row(4)


def print_square(size):
    for i in range(size): # for each column
        for j in range(size): # for each row
            print("#", end="")
        print() # go to new string after each iteration

def print_column(height):
    print("#\n" * height, end="") # python's magic)

def print_row(width):
   print("?" * width)


main()