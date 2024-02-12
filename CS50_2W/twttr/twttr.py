vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"] # make array of vowels which we will comprate with input
text = input("Input: ")

for letter in text: # going through every letter in input
    for vowel in vowels: # now  for every letter in array
        if letter == vowel: # compraring if letter is vowel
            text = text.replace(vowel, "") # and replace this letter with empty space


print(f"{text}")