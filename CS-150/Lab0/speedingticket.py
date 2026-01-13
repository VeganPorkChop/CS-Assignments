try:
    #recieving inputs
    speed_limit = int(input("Enter the speed limit: "))
    recorded_speed = int(input("Enter the recorded speed of the car: "))

    #calculating the price paid for speeding ticket
    price = 0
    if recorded_speed <= speed_limit-10:
        price += 50
    if recorded_speed >= speed_limit+40:
        price += 300
    elif recorded_speed >= speed_limit+21:
        price += 150
    elif recorded_speed >= speed_limit+6:
        price += 75
    
    #printing the resulting speeding ticket price
    print(f"The speeding ticket price is: ${price}")
        

except (ValueError, TypeError):
    #just in case the user inputs something that is not an integer, we dont want the program to throw an ugly error
    print("Invalid input. Please enter integers values for speed.")

