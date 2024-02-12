first_sum = 50
left_sum = print(f"Amount Due: {first_sum}")

while(first_sum > 0):
    substract_sum = input("Insert coin: ")
    substract_sum = int(substract_sum)
    if substract_sum == 30: # 30 cents does not exist
        print(f"Amount Due: {first_sum}") # we show how much left to user to pay
        break # break from cycle
    first_sum = first_sum - substract_sum
    if first_sum <= 0:
        print(f"Change Owed: {first_sum*-1}") # if user gave more money we show him left sum with other sign using *-1
        break
    print(f"Amount Due: {first_sum}")

