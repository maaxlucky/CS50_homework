def convert():
    text = input()
    text = text.replace(":(", "🙁") # we replace :( symbol in our variable to emoji
    text = text.replace(":)", "🙂") # same as above
    print(text)


def main():
    convert()

main()