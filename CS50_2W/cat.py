# trying while loop
# i = 0
# while i <= 2:
#     print("meow")
#     i += 1

# pythonic for loop)
# for _ in range(3):
#     print("meow")

# print("meow\n" * 3, end="") # cool pythonic =)

#loops
# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break # break from cycle
#
# for _ in range(n):
#     print("meow")


def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            # break # we can break and then again return n from function or we can return value from loop directly
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()