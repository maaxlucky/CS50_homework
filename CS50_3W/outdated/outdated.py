months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        month,day,year = date.split("/")
        try:
            month = int(month)
        except ValueError:
            continue
        day = int(day)
        year = int(year)
        if month > 12 or day > 31:
            continue
        print(f"{year}-{month:02}-{day:02}")
        break
    except ValueError:
        month,day,year = date.split(" ")

        if ',' in day:
            day = day.replace(",", "")
        else:
            continue

        try:
            day = int(day)
        except ValueError:
            continue

        for i in range(len(months)):
            if month == months[i]:
                month = i
        if day > 31 or month > 12:
            continue

        print(f"{year}-{month+1:02}-{day:02}")
        break
