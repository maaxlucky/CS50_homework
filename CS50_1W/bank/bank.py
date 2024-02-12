greet = input("Greeting: ")
greet = greet.lower()

if "hello" in greet:
    print("$0")

elif greet[0] == "h": # string is array of symbols so we can compare first symbol
    print("$20")

else:
    print("$100")