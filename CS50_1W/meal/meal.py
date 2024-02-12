def main():
    eat_time = input("What time is it? ")
    time = convert(eat_time) # we get number from convert function
    # determine what time is it rn
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12<= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    hour, minutes = time.split(":") # split time in hours and minutes
    hour = float(hour) # make string - float number
    minutes = float(minutes)
    minutes = (minutes / 100) * 1.67 # convert minutes to number
    converted_time = hour + minutes
    converted_time = round(converted_time, 2) # round 2 digits of our number
    # print(f"{converted_time:.2f}") # round float number, his 2 digits
    return converted_time


if __name__ == "__main__":
    main()
