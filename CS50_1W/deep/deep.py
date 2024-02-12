answer = input("What is the answer to the Great Qeustion? \n")
answer = answer.lower().strip() # we make any input to lower case to make it easier to compare and delete blank spaces
if answer == "42" or  answer == "forty two" or answer == "forty-two":
    print("Yes")
else:
    print("No")