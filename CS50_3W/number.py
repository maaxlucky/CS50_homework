def main():
    x = get_int("What's y? ")
    print(f"x is {x}")

def get_int(prompt):
    while True: # nice pattern how to get number with exception
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            pass

main()