refactor_case = input("camelCase: ")

for i in range(len(refactor_case)):
    if refactor_case[i].isupper(): # check if letter is uppercase
        # replace uppercase letter with _ + lowercase_letter
        refactor_case = refactor_case.replace(refactor_case[i], f"_{refactor_case[i].lower()}")


print(f"snake_case: {refactor_case}")