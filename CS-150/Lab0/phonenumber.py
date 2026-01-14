#this is the input
phone_number = int(input())

#This is how you would do it with modulous
for i in range(10, 0, -1):
    digit = phone_number // 10**(i-1)
    phone_number = phone_number % 10**(i-1)
    if (i == 10):
        print("(", end="")
    elif (i == 7):
        print(")", end=" ")
    elif (i == 4):
        print("-", end="")
    print(digit, end="")
