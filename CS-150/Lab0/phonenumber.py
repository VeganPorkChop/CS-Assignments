#this is the input
phone_number = input("Please enter a 10 digit phone number: ")

#this is the error handling for the input, just incase the user cant follow instructions
try:
    #this is the type check for the input
    if (len(phone_number) != 10):
        raise KeyError("Phone number must be exactly 10 digits.")
    phone_number = int(phone_number)

    #This is how you would do it with modulous
    for i in range(10, 0, -1):
        digit = phone_number // 10**(i-1)
        phone_number = phone_number % 10**(i-1)
        if (i == 10):
            print("(", end="")
        elif (i == 7):
            print(")", end="")
        elif (i == 4):
            print("-", end="")
        print(digit, end="")

    #this is the formatted output with fstrings making phonenumber a string
    #print(f"Your phone number is formatted as: ({phone_number[0:3]}) {phone_number[3:6]}-{phone_number[6:10]}")
except (TypeError, ValueError, KeyError):
    print("The phone number you entered is invalid, please try again.")