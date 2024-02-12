text = input("Expression: ")
x,y,z = text.split(" ") # split expression string into 3 variables using split method
x = float(x) # make string variables - float
z = float(z)

# just simple calculator
if y == "+":
   print(x+z)

elif y == "-":
    print(x-z)

elif y == "*":
    print(x*z)

elif y == "/":
    print(x/z)