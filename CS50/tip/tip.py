def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}") # we round float number - his two digits after dot


def dollars_to_float(d):
    d = d.replace("$", "") # we remove dollar sign from string
    d = float(d) # input returns string, so we convert string to float
    return d


def percent_to_float(p):
    p = p.replace("%", "") # we remove percentage sign from string
    p = float(p)
    p = p / 100 # we divide to get correct percentage
    return p

main()
