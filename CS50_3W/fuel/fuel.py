def main():
    get_fraction()


def get_fraction():
    while True:
        try:
            fract = input("Fraction: ")
            x, y = fract.split("/")
            x = int(x)
            y = int(y)
            if x > y: # x can't be bigger then y
                continue # go to the start of cycle
            break
        except ValueError:
            pass

    z = (x / y) * 100
    z = round(z,0)
    z = int(z)

    if z <= 1:
        print("E")
    elif z >= 99:
        print("F")
    else:
        print(f"{z}%")

main()