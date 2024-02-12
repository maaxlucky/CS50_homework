
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n): # made function that check if number is even or odd
    # return True if n % 2 == 0 else False # only python's feature
    return n % 2 == 0 # even shorter
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

main()