def calc_energy():
    mass = int(input("What is mase? "))
    speed = pow(300000000,2) # using pow function, it returns your number and second parameter is what number's degree
    return mass * speed # calculate energy and return to main function

def main():
    print(calc_energy()) # it returns number so we just print this number


main()